from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cul_id = models.AutoField(primary_key=True)
    photo_url = models.URLField(max_length=400, default='', blank=True)
    alt_email = models.EmailField(max_length=100, default='', blank=True)
    college = models.CharField(max_length=100, blank=True, default='')
    phone = models.CharField(max_length=100, default='', blank=True)
    year_of_grad = models.CharField(max_length=100, default='', blank=True)
    address = models.CharField(max_length=500, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    state = models.CharField(max_length=100, default='', blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.photo_url = 'http://graph.facebook.com/{0}/picture?type=large'.format(instance.username)
    instance.profile.save()
