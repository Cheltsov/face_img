from django.shortcuts import render
from django.http import HttpResponse
from .forms import PhotoForm
from .models import Photo

from . models import Photo

import dlib
from skimage import io
from scipy.spatial import distance

# Create your views here.
def index(request):
    photos = Photo.objects.all()
    form = PhotoForm()
    context = {
        'photos': photos,
        'form': form
    }
    return render(request, 'face/index.html', context)


def add_photos(request):
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
            form.save(commit=True)
            arr_photos = Photo.objects.all().reverse()[0]

            url_img1 = arr_photos.img_1.path
            url_img2 = arr_photos.img_2.path
            num_evd_res = get_evklid(url_img1, url_img2)

            arr_photos.num_evd = num_evd_res
            arr_photos.save()
            if num_evd_res < 0.55:
                context = {
                    'photos': arr_photos,
                    'num': num_evd_res
                }
                return render(request, 'face/result.html', context)
            else:
                return HttpResponse("Не прошел")
        else:
            print(form.errors)
        return render(request, 'face/index.html', {'form': form})
    else:
        return HttpResponse('no')

def get_evklid(url_img1, url_img2):

    sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
    detector = dlib.get_frontal_face_detector()

    img = io.imread(url_img1)

    win1 = dlib.image_window()
    win1.clear_overlay()
    win1.set_image(img)

    dets = detector(img, 1)

    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))
        shape = sp(img, d)
        win1.clear_overlay()
        win1.add_overlay(d)
        win1.add_overlay(shape)

    face_descriptor1 = facerec.compute_face_descriptor(img, shape)
    print(face_descriptor1)

    img = io.imread(url_img2)
    win2 = dlib.image_window()
    win2.clear_overlay()
    win2.set_image(img)
    dets_webcam = detector(img, 1)
    for k, d in enumerate(dets_webcam):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))
        shape = sp(img, d)
        win2.clear_overlay()
        win2.add_overlay(d)
        win2.add_overlay(shape)

    face_descriptor2 = facerec.compute_face_descriptor(img, shape)

    a = distance.euclidean(face_descriptor1, face_descriptor2)
    return a

