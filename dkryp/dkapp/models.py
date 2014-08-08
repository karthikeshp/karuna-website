import os

from django.conf import settings
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

EVENT_CATEGORY = (
    ('none', 'None'),                
    ('cat1', 'cat1'),
    ('cat2', 'cat2'),
    ('cat3', 'cat3'),    
)

PRODUCT_CATEGORY = (
    ('none', 'None'),                
    ('cat1', 'cat1'),
    ('cat2', 'cat2'),
    ('cat3', 'cat3'),    
)

class Event(models.Model):
    title = models.CharField(max_length=100, default='untitled', help_text='Enter the event title')
    category = models.CharField(max_length=20, default='none', choices=EVENT_CATEGORY, help_text='Select the type of category')
    description = models.TextField(null=True, blank=True, help_text="Event description")
    organiser = models.CharField(max_length=50, null=True, blank=True, default='', help_text='Name of organiser')
    venue = models.CharField(max_length=100, null=True, blank=True, default='', help_text='Venue of event')
    date_of_event = models.DateTimeField(help_text='Date of event contacted')

    def __unicode__(self):
        return self.title

class Gallery(models.Model):
    event = models.ForeignKey(Event)
    picture = models.FileField(upload_to='gallery', null=True, blank=True, help_text='Choose picture of the event')

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __unicode__(self):
        if '/' in str(self.picture):
            return str(self.picture).split('/')[-1]
        else:
            return str(self.picture)

@receiver(post_delete, sender=Gallery)
def delete_image_too(sender, instance, **kwargs):
    os.remove(os.path.join(settings.MEDIA_ROOT, str(instance.picture)))

class Product(models.Model):
    name = models.CharField(max_length=100, default='noproduct', help_text='Enter the product name')
    category = models.CharField(max_length=20, default='none', choices=PRODUCT_CATEGORY, help_text='Select the type of product')
    description = models.TextField(null=True, blank=True, help_text="Product description")
    picture = models.FileField(upload_to='product', null=True, blank=True, help_text='Choose picture of the product')
    launched = models.DateField(help_text='Date of product launched')