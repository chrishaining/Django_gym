from django.test import TestCase
from my_gym.models import *
# Create your tests here.
class MemberTestCase(TestCase):
    def setUp(self):
        self.member1 = Member.objects.create(first_name = "Ron", last_name = "Jones")
    
    def test_member_saved(self):
        self.assertGreater(self.member1.pk, 0)

    