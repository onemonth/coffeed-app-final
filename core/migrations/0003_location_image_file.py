# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150305_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image_file',
            field=models.ImageField(null=True, upload_to=core.models.upload_to_location, blank=True),
            preserve_default=True,
        ),
    ]
