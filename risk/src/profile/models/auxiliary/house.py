from django.db import models
from django.core.validators import MaxLengthValidator
from django.utils.translation import ugettext_lazy as _

from risk.src.profile.models.domain.user import User as UserModel

class House(models.Model):
  house_id = models.AutoField(primary_key=True)
  ownership_status = models.CharField(
      validators = [
          MaxLengthValidator(50)
      ]
  )
  user_id = models.ForeignKey(
    UserModel,
    on_delete = models.SET_NULL,
    blank = True,
    null = True,
  )
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

  class Meta:
      ordering = ['-house_id', ]
      verbose_name = _('house')
      verbose_name_plural = _('houses')
