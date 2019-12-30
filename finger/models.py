from django.db import models
import os

# Create your models here.
class Fphoto(models.Model):
    img_1 = models.ImageField(upload_to='')
    img_2 = models.ImageField(upload_to='')
    num_evd = models.FloatField(null=True)

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.img_1.path):
            os.remove(self.img_1.path)
        if os.path.isfile(self.img_2.path):
            os.remove(self.img_2.path)
        super(Fphoto, self).delete(*args, **kwargs)
