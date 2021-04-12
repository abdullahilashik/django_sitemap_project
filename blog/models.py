from django.db import models
from django.urls import reverse
from django.contrib.sitemaps import ping_google

class Blog(models.Model):
    title = models.CharField(max_length=250, blank=False)
    content = models.TextField(max_length=2000, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, force_insert=False, force_update=False):
        super().save(force_insert,force_update)
        try:
            ping_google()
        except:
            pass

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('/details/', args=[str(self.id)])