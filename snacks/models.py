from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack(models.Model):
    title=models.CharField(max_length=255,help_text='isert the title of snacks')
    purchaser=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description =models.TextField(blank=True)

    def str (self):
       return self.title
    def get_absolute_url(self):
        return reverse ('details',args=[self.id])