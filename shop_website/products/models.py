from django.db import models

# Create your models here.
class product(models.Model):
  title = models.CharField(max_length = 120) # max_length is required
  description = models.TextField(blank=True)
  price = models.DecimalField(decimal_places = 2, max_digits=1000, null=True)
  summary = models.TextField(default='')
  commit_test = models.CharField(max_length = 120)

  def __str__(self):
    return self.title
  