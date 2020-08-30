from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import CITextField
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.db.models.signals import pre_save
def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify("GHYYSgjhbc")

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(alias__iexact=slug).exists()
    if qs_exists:
        new_slug = get_random_string(length=15)
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


class Url(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE,related_name='url',blank=True)
    alias = CITextField(max_length=25,blank=True,unique=True)
    link  = models.URLField(max_length=1000)
    hit = models.IntegerField(default=0)
    


    def get_absolute_url(self):
        return reverse('myapp:home')
    def __str__(self):
        return str(self.alias)+" "+str(self.link)
    
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.alias:
        instance.alias = unique_slug_generator(instance) 
pre_save.connect(pre_save_receiver, sender = Url)