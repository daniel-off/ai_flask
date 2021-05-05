from django.db import models

from django_app.storage_backends import PublicMediaStorage, PrivateMediaStorage


class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=PublicMediaStorage())


class UploadPrivate(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(storage=PrivateMediaStorage())


class Member(models.Model):
        username =models.CharField(max_length=100)
        link = models.CharField(max_length=100)
        pozitivita=models.CharField(max_length=100)


        def __str__(self):
            return self.username +" "+ self.pozitivita+" "+ self.link