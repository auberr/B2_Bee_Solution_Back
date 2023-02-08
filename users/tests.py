from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class UserCreateViewTestCase(APITestCase):
    def test_registration(self):
        url = reverse("user_create_view")
        user_data = {
            "username" : "testuser",
            "password" : "password1!",
            "password2" : "password1!",
        }

        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 201)


class UserAuthViewTestCase(APITestCase):
    # self.data = {'username': 'testuser', 'password':'password1!'}
    # self.user = User.objects.create_user('testuser', 'password1!')
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {'username':'john', 'password':'password1!'}
        cls.user = User.objects.create_user('john', 'password1!')

        # for user_id in range(113):
        #     User.objects.create_user(
        #         username=f'john{user_id}', password=f'password1!{user_id}'
        #     )
        
    
        
    def test_login(self):
        url = reverse("user_auth_view")
        response = self.client.post(url, self.user_data)
        self.assertEqual(response.status_code, 200)
            
    def test_get_user_data(self):
        access_token = self.client.post(reverse('user_auth_view'), self.user_data).data['access']
        response = self.client.get(path=reverse("user_auth_view"), HTTP_AUTHORIZATION=f"Bearer {access_token}")
        print(response.data)
        self.assertEqual(response.status_code, 200)