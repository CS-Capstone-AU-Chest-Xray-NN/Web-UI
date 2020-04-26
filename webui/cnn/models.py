from django.db import models


class Image(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to='images/')

    @classmethod
    def create(name, image):
        obj = cls(name=name, image=image)
        return obj
