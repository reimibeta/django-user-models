import uuid

from django.db import models

from .user import User
from image_utils.compress_image import compress_image


class UserPhoto(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to='photos/users/{}/'.format(uuid.uuid4()),
        null=True
    )
    thumbnail = models.ImageField(
        upload_to='photos/users/thumbnails/{}/'.format(uuid.uuid4()),
        blank=True, null=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        # print(self.photo.path)
        # print(self.photo.file)
        if str(self.photo.path) == str(self.photo.file):
            print('return true when on new file uploaded!')
        else:
            img = compress_image()
            # self.thumbnail = img.image(self.photo, 'thumbnail_{}'.format(uuid.uuid4().hex[:8].upper()))
            self.photo = img.image(self.photo, width=700)
            self.thumbnail = img.image(self.photo, width=300)
            # self.photo.name = '{}{}'.format(RandomString.ustring(), compress_image.ext(self.photo))
        super(UserPhoto, self).save(*args, **kwargs)

    def __str__(self):
        return self.thumbnail.url
