import uuid

from django.db import models

from .user import User
from image_utils.compress.compress_image import compress_image


class UserPhoto(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to='photos/users/',
        null=True
    )
    thumbnail = models.ImageField(
        upload_to='photos/users/thumbnails/',
        blank=True, null=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        if str(self.photo.path) == str(self.photo.file):
            print('return true when on new file uploaded!')
        else:
            self.photo = compress_image.resize(700, self.photo)
            self.thumbnail = compress_image.resize(300, self.photo)
        super(UserPhoto, self).save(*args, **kwargs)

    def __str__(self):
        return self.thumbnail.url
