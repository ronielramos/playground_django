from django.test import TestCase

from risk.src.profile.models.domain.user import User as UserModel

class UserTestCase(TestCase):
  def setUp(self):
    self.user = UserModel(
        dependents_tally=5,
        income=300000,
        marital_status='married'
    )

  def test_user_have_dependents_tally(self):
    '''
    User must have dependents_tally value
    '''

    self.assertEqual(self.user.dependents_tally,
                     5, 'dependents_tally must have value equals to setup user but had ' + str(self.user.dependents_tally))

  def test_user_have_income(self):
    '''
    User must have income value
    '''
    self.assertEqual(self.user.income, 300000,
                     'income must have value equals to setup user "300000" but had ' + str(self.user.income))

  def test_user_have_marital_status(self):
    '''
    User must have marital_status as married
    '''
    self.assertEqual(self.user.marital_status, 'married',
                     'marital_status must have value equals to setup user "married" but had ' + str(self.user.marital_status))
