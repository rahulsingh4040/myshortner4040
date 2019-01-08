from django.db import models
from .utils import create_shortcode
from django.conf import settings
from .validators import validate_url
from django_hosts.resolvers import reverse

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

# Create your models here.
class KirrURL(models.Model):
	url = models.CharField(max_length=220, validators=[validate_url])
	shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.url)

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode=="":
			self.shortcode = create_shortcode(self)
		if not "http://" in self.url:
			url = "http://" + self.url
		super(KirrURL, self).save(*args, **kwargs)

	def get_short_url(self):
		url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='https')
		return url_path

