from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User, UserChr
import random

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
        self.assertEqual(response.status_code, 200)

class UserSignOutViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {'username':'john', 'password':'password1!'}
        cls.user = User.objects.create_user('john', 'password1!')
        
    
    def test_login(self):
        url = reverse("user_auth_view")
        response = self.client.post(url, self.user_data)
        self.assertEqual(response.status_code, 200)
    
    def test_signout(self):
        url = reverse("user_signout_view")
        response = self.client.post(url, self.user_data)
        self.assertEqual(response.status_code, 204)

class UserChrViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {'username':'john', 'password':'password1!'}
        cls.user = User.objects.create_user('john', 'password1!')
        
    
    def setUp(self):
        self.access_token = self.client.post(reverse('user_auth_view'), self.user_data).data['access']

    def test_userchr_get_no_content(self):
        self.user_id = 1
        self.user = User.objects.get(id=1)
        self.user.user_chr_check = False
        print(self.user.user_chr_check)
        print(2345)
        url = reverse("user_chr_view", args=[self.user_id])
        response = self.client.get(
            path = url,
            data = {'user' : self.user,
                },
            HTTP_AUTHORIZATON = f'Bearer {self.access_token}'
        )
        print(response.data)
        self.assertEqual(response.status_code, 204)


    def test_userchr_post(self):
        self.user_id = 1
        url = reverse("user_chr_view", args=[self.user_id])
        mbti_list = ['ENFP', 'ENFJ', 'ENTP', 'ENTJ', 'ESFP', 'ESFJ', 'ESTP', 'ESTJ', 'INFP', 'INFJ', 'INTP', 'INTJ', 'ISFP', 'ISFJ', 'ISTP', 'ISTJ']
        response = self.client.post(
            path = url, 
            data = {
                'user_id' : 1,
                'mbti' : random.choice(mbti_list),
                'gender' : random.choice(['W', 'M']),
                'age' : random.randrange(10, 80)
            },
            HTTP_AUTHORIZATON = f'Bearer {self.access_token}'
            )
            
        self.assertEqual(response.status_code, 200)
    


class UserChrChangeViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {'username':'john', 'password':'password1!'}
        cls.user = User.objects.create_user('john', 'password1!')
        mbti_list = ['ENFP', 'ENFJ', 'ENTP', 'ENTJ', 'ESFP', 'ESFJ', 'ESTP', 'ESTJ', 'INFP', 'INFJ', 'INTP', 'INTJ', 'ISFP', 'ISFJ', 'ISTP', 'ISTJ']
        cls.user_chr = UserChr.objects.create(
            user_id = 1,
            mbti = random.choice(mbti_list),
            gender = random.choice(['W', 'M']),
            age = random.randrange(10, 80)
        )
    
    def setUp(self):
        self.access_token = self.client.post(reverse('user_auth_view'), self.user_data).data['access']

    def test_userchr_put(self):
        self.user_id = 1
        url = reverse("user_chr_change_view", args=[self.user_id])
        mbti_list = ['ENFP', 'ENFJ', 'ENTP', 'ENTJ', 'ESFP', 'ESFJ', 'ESTP', 'ESTJ', 'INFP', 'INFJ', 'INTP', 'INTJ', 'ISFP', 'ISFJ', 'ISTP', 'ISTJ']
        response = self.client.put(
            path = url, 
            user = UserChr.objects.get(user_id=1),
            data = {
                'user_id' : 1,
                'mbti' : random.choice(mbti_list),
                'gender' : random.choice(['W', 'M']),
                'age' : random.randrange(10, 80)
            },
            HTTP_AUTHORIZATON = f'Bearer {self.access_token}'
            )
            
        self.assertEqual(response.status_code, 200)

