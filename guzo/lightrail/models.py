"""
Ethiopian Transport API
Models
"""

__author__ = "Dawit Nida (dawit@dawitnida.com)"
__date__ = "Date: 18-11-2017"
__version__ = "Version: 1.0.0"
__Copyright__ = "Copyright: @dawitnida"

from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator
import random
from audit_log.models import AuthStampedModel
import uuid
from guzo.lightrail.model_utils import Choices
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator
from django.utils.encoding import smart_text

salt = 'das54sFsdfVsTplfsNmf'


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=timezone.now(), editable=False, )
    updated_date = models.DateTimeField(auto_now=timezone.now(), )
    entry_status = models.IntegerField(choices=Choices.ENTRY_STATUSES, default=1, )
    slug = models.SlugField(default=random.randrange(10), blank=True, null=True, max_length=100, )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, )

    class Meta:
        abstract = True


class Technical(BaseModel, AuthStampedModel):
    system_length = models.CharField(max_length=100, )
    track_gauge = models.CharField(max_length=100, )
    top_speed = models.CharField(max_length=100, )
    electrification = models.CharField(max_length=100, )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.system_length)
        super(Technical, self).save(*args, **kwargs)

    def __str__(self):
        return smart_text(self.track_gauge)


class Service(BaseModel, AuthStampedModel):
    name = models.CharField(max_length=100, )
    locale = models.CharField(max_length=100, )
    number_of_lines = models.PositiveSmallIntegerField()
    number_of_stations = models.PositiveSmallIntegerField()
    transit_type = models.CharField(max_length=100, )
    budget = models.IntegerField(default=0, blank=True, )
    daily_ridership = models.IntegerField(default=0, )
    operation_start_date = models.DateField()
    operators = models.CharField(max_length=100, )
    number_of_vehicles = models.PositiveSmallIntegerField()
    technical = models.OneToOneField(Technical, blank=True, null=True, )

    class Meta:
        ordering = ("name", "number_of_stations", "number_of_lines",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return smart_text(self.name)


class Station(BaseModel, AuthStampedModel):
    code = models.CharField(max_length=6,
                            validators=[
                                RegexValidator(regex='^.{6}$', message='Length has to be 6', code='nomatch')])
    name = models.CharField(max_length=100, )
    street_address = models.CharField(max_length=100, blank=True, null=True, )
    place = models.IntegerField(choices=Choices.PLACE, default=1, )
    longitude = models.FloatField(blank=True, null=True, )
    latitude = models.FloatField(blank=True, null=True, )
    operational_status = models.IntegerField(choices=Choices.OPERATIONAL_STATUSES, default=1, )
    ticket_sale = models.BooleanField(default=True)
    service = models.ForeignKey(Service, default=1, )

    class Meta:
        unique_together = ("code",)
        ordering = ("name", "code",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Station, self).save(*args, **kwargs)

    def __str__(self):
        return smart_text(self.name)


class Media(BaseModel, AuthStampedModel):
    gallery_type = models.IntegerField(choices=Choices.SOCIAL_MEDIA, default=1, )
    image_data = models.ImageField(upload_to='gallery', )
    caption = models.CharField(max_length=60, default='', )
    video_url = models.CharField(max_length=100, blank=True, default='', validators=[URLValidator()], )
    service = models.ForeignKey(Service, blank=True, null=True, )
    station = models.ForeignKey(Station, blank=True, null=True, )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.station)
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return smart_text(self.station)


class PriceQuota(BaseModel, AuthStampedModel):
    quota_code = models.CharField(max_length=4,
                                  validators=[
                                      RegexValidator(regex='^.{4}$', message='Length has to be 4', code='nomatch')])
    description = models.TextField(max_length=100, blank=True, )

    class Meta:
        unique_together = ("quota_code",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.quota_code)
        super(PriceQuota, self).save(*args, **kwargs)

    def __str__(self):
        return smart_text(self.quota_code)

    @classmethod
    def get_description(cls, quota_code):
        try:
            description = cls.objects.filter(quota_code=quota_code)
            return description
        except IndexError:
            return None
