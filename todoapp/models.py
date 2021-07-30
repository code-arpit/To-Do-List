from django.db import models
from django.urls import reverse

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(null=False)

    def get_detail_url(self):
        return reverse('detail', kwargs={'my_item':self.id})
