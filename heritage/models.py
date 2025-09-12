# Django model for Monastery
# Fields: name (CharField), location (CharField), description (TextField),
# established_year (IntegerField), latitude (FloatField), longitude (FloatField),
# image (ImageField, upload_to="monasteries/")
from django.db import models
from django.utils.translation import gettext_lazy as _

class Monastery(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    established_year = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to="monasteries/", blank=True, null=True)
    vr_image = models.ImageField(upload_to="monasteries/vr/", blank=True, null=True)
    vr_video = models.FileField(upload_to="monasteries/vr/", blank=True, null=True)
    streetview_embed = models.TextField(null=True, blank=True)
     
    class Meta:
        verbose_name = _("Monastery")
        verbose_name_plural = _("Monasteries")
        ordering = ['name']

    def __str__(self):
        return self.name
    
    
    # Django model for Event
# Fields: monastery (ForeignKey to Monastery), title (CharField),
# date (DateField), description (TextField), ticket_price (DecimalField)
class Event(models.Model):
    monastery = models.ForeignKey("Monastery", on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ['-date']
        
    def __str__(self):
        return self.title
