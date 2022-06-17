from django.test import TestCase
from django.contrib.auth import get_user_model

from users import admin

USER_MODEL = get_user_model()



class UserManagerTests(TestCase):

    def test_create_user(self):
        user = USER_MODEL.objects.create_user(
            email='user@email.com',
            password='foo'
        )

        self.assertEqual(user.email, 'user@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        # check if user username, first_name, last_name are None

        self.assertIsNone(user.username)
        self.assertIsNone(user.last_name)

    def test_create_superuser(self):
        admin = USER_MODEL.objects.create_superuser(
            email='admin@email.com',
            password='foo'
        )

        self.assertEqual(admin.email, 'admin@email.com')
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

         # check if user username, first_name, last_name are None
        
        self.assertIsNone(admin.username)
        self.assertIsNone(admin.last_name)