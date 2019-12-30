from django.db import models
import os

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=254)
    face_img = models.ImageField(upload_to='')
    finger_img = models.ImageField(upload_to='')

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.face_img.path):
            os.remove(self.face_img.path)
        if os.path.isfile(self.finger_img.path):
            os.remove(self.finger_img.path)
        super(User, self).delete(*args, **kwargs)
