from django.db import models
from django.core.urlresolvers import reverse

import os
import uuid

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
	hours = models.TextField(null=True, blank=True)
	image_file = models.ImageField(upload_to=upload_to_location, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse(viewname="location_list", args=[self.id])
