from django.test import TestCase

from DbExcelClick import CollegeSerializer
from onlineapp.models import *

class collegeTestCase(TestCase):
    def setUp(self):
        College.objects.create(name='Hard', location='Hard', acronym='Hard', contact='Hard')

        College.objects.create(name='Joe', location='Joe', acronym='Joe', contact='Joe')

        College.objects.create(name='Hit', location='Hit', acronym='Hit', contact='Hit')

    def test01(self):
        self.assertEqual(CollegeSerializer(College.objects.get(name='Hit')).data,
                         {'name': 'Hit', 'location': 'Hit', 'acronym': 'Hit', 'contact': 'Hit', })

    def test02(self):
        self.assertEqual(CollegeSerializer(College.objects.get(name='Joe')).data,
                            {'name': 'Joe', 'location': 'Joe', 'acronym': 'Joe', 'contact': 'Joe', })

    def test03(self):
        self.assertEqual(CollegeSerializer(College.objects.get(name='Joe')).data,
                         {'name': 'Joe', 'location': 'Joe', 'acronym': 'Joe', 'contact': 'Joe', })


# Create your tests here.

