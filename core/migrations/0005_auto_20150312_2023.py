# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='alcohol',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='bathrooms',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='coffee',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Truck Stop'), (2, b'Good'), (3, b'Really Good'), (4, b'Great')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='food',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='outdoor',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='outlets',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='seating',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Minimal'), (2, b'Some'), (3, b'Ample')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='wifi',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'None'), (1, b'Spotty'), (2, b'Strong')]),
            preserve_default=True,
        ),
    ]
