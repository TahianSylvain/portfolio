from django.db import models
from django.contrib.auth.models import User


class Mega(models.Model):
    zip = models.FileField(blank=True)


class Surf(models.Model):
    owner = models.OneToOneField(to=User,
        on_delete=models.CASCADE)
    subject = models.CharField(max_length=12)
    mess = models.TextField()
    rating = models.PositiveSmallIntegerField(default=3)
    objects = models.Manager()

    class Meta:
        pass

    def __str__(self):
        return self.subject
