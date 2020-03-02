import pytest
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_Create():
  User.objects.create_user('roniel', 'roniel_ramos@email.com', 'ronielpassword')
  assert User.objects.count() == 1