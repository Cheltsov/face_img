from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import FormUser
from face.views import get_evklid
from finger.views import checkFinger
import os
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    users = User.objects.all()
    form = FormUser()
    context = {
        'photos': users,
        'form': form
    }
    return render(request, 'user/index.html', context)

def check_user(request):
    if request.method == 'POST':
        form = form = FormUser(request.POST, request.FILES)
        if form.is_valid():

            user = User.objects.filter(email=request.POST['email'])
            if len(user) > 0:
                user = user[0]
                photo_old_face = user.face_img.path
                photo_old_finger = user.finger_img.path

                print(photo_old_face)
                print(photo_old_finger)

                myfile = request.FILES['img']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                photo_new = fs.url(filename)

                print(photo_old_face.split('\\')[-1])

                if request.POST['face_or_finger'] == "1":
                    num_evd_res = get_evklid(photo_old_face, photo_new)
                    if num_evd_res < 0.55:
                        result = 1
                    else:
                        result = 0
                    context = {
                        'photo1': photo_old_face.split('\\')[-1],
                        'photo2': photo_new,
                        'num': result
                    }
                    return render(request, 'user/result.html', context)
                else:
                    result = checkFinger(photo_old_finger, photo_new)
                    print(result)
                    if result > 80:
                        result = 1
                    else:
                        result = 0
                    context = {
                        'photo1': photo_old_finger.split('\\')[-1],
                        'photo2': photo_new,
                        'num': result
                    }
                    return render(request, 'user/result.html', context)
            else:
                print('Такого пользователя нет')
                return HttpResponse("Такого пользователя нет")
        else:
            print(form.errors)
        return render(request, 'face/index.html', {'form': form})
    else:
        return redirect('/')

