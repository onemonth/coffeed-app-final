from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models import Avg
from geoposition.fields import GeopositionField

import os
import uuid

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)

RATING_CHOICES = (
    (0, 'None'),
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),
    )

YESNO_CHOICES = (
    (0, 'No'),
    (1, 'Yes')
    )

PLURAL_CHOICES = (
    (0, 'None'),
    (1, 'Minimal'),
    (2, 'Some'),
    (3, 'Ample')
    )

WIFI_CHOICES = (
    (0, 'None'),
    (1, 'Spotty'),
    (2, 'Strong')
    )

COFFEE_CHOICES = (
    (0, 'None'),
    (1, 'Truck Stop'),
    (2, 'Good'),
    (3, 'Really Good'),
    (4, 'Great'),
    )

def upload_to_location(instance, filename):
    blocks = filename.split('.')
    ext = blocks[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    instance.title = blocks[0]
    return os.path.join('uploads/', filename)

# Create your models here.

class Location(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    position = GeopositionField(null=True, blank=True)
    hours = models.TextField(null=True, blank=True)
    image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)
    wifi = models.IntegerField(choices=WIFI_CHOICES, null=True, blank=True)
    seating = models.IntegerField(choices=PLURAL_CHOICES, null=True, blank=True)
    outlets = models.IntegerField(choices=PLURAL_CHOICES, null=True, blank=True)
    bathrooms = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    coffee = models.IntegerField(choices=COFFEE_CHOICES, null=True, blank=True)
    alcohol = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    outdoor = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    food = models.IntegerField(choices=YESNO_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname="location_detail", args=[self.id])

    def get_average_rating(self):
        average = self.review_set.all().aggregate(Avg('rating'))['rating__avg']
        if average == None:
            return average
        else:
            return int(average)

    def get_reviews(self):
        return self.review_set.all()


class Review(models.Model):
    location = models.ForeignKey(Location)
    user = models.ForeignKey(User)
    description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)







