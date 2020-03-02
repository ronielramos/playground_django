from django.db import models
from django.core.validators import MaxLengthValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _

class User(models.Model):
  user_id = models.AutoField(primary_key = True)
  dependents_tally = models.IntegerField(
      default = 0, 
      validators = [
        MinValueValidator(0, message = 'Min value is 0')
      ]
  )
  income = models.IntegerField(
      default = 0,
      validators = [
        MinValueValidator(0, message = 'Min value is 0')
      ]
  )
  marital_status = models.CharField(max_length=30)
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-user_id', ]
    verbose_name = _('user')
    verbose_name_plural = _('users')
