# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.urlresolvers import reverse


class MakerModel(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    name = models.CharField(
        max_length=200,
    )
    location = models.CharField(
        max_length=200,
    )

    def get_absolute_url(self):
        return reverse('sake:SakeListView')

    def __str__(self):
        return self.name


class SakeModel(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    name = models.CharField(
        max_length=200,
    )
    image = models.ImageField(
        upload_to='images/',
    )
    maker = models.ForeignKey(
        MakerModel,
        related_name='maker',
    )
    create_date = models.DateTimeField(
        auto_now=True,
    )

    def get_absolute_url(self):
        return reverse('sake:SakeDetailView',args=(self.uuid,))

    def __str__(self):
        return self.name


class SakeTypeModel(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )
    sake = models.ForeignKey(
        SakeModel,
        related_name='sake'
    )

    FRUITY = 'FU'
    SPICY = 'SP'
    FRESH = 'FE'
    RICH = 'RI'
    AROMA_CHOICES = (
        (FRUITY, 'fruity'),
        (SPICY, 'spicy'),
        (FRESH, 'fresh'),
        (RICH, 'rich'),
    )
    aroma = models.CharField(
        max_length=2,
        choices=AROMA_CHOICES,
        default=FRUITY,
    )

    SWEET = 'SW'
    DRY = 'DR'
    SOUR = 'SO'
    TASTE_CHOICES = (
        (SWEET, 'fruity'),
        (DRY, 'spicy'),
        (SOUR, 'fresh'),
        (RICH, 'rich'),
    )
    taste = models.CharField(
        max_length=2,
        choices=TASTE_CHOICES,
        default=SWEET,
    )

    def get_absolute_url(self):
        return reverse('sake:SakeListView')
