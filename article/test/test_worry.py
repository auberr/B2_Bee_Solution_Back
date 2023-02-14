from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User, UserChr
from article.models import Category, Solution, Rating, Article, Comment
import random
from faker import Faker

class MakeWorryViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.faker = Faker()
        mbti_list = ['ENFP', 'ENFJ', 'ENTP', 'ENTJ', 'ESFP', 'ESFJ', 'ESTP', 'ESTJ', 'INFP', 'INFJ', 'INTP', 'INTJ', 'ISFP', 'ISFJ', 'ISTP', 'ISTJ']
        
        for i in range(1,100):
            cls.user = User.objects.create_user(
                username=cls.faker.name(), password='password1!'
            )
            
            cls.user_chr = UserChr.objects.create(
                user_id = i,
                mbti = random.choice(mbti_list),
                gender = random.choice(['W', 'M']),
                age = random.randrange(10, 80)
            )
            
        cls.user_id = 1
        cls.user_data = {'username':User.objects.get(id = cls.user_id), 'password':'password1!'}
        
        category_list = ['일상','취미','취업','음식']
        for cate in category_list:
            cls.category = Category.objects.create(
                category=cate
            )
            for _ in range(10):
                cls.solution = cls.category.connected_solution.create(
                    user_id = random.randrange(1, 100),
                    wise = cls.faker.sentence()
                )
            
        
        for _ in range(100):
            cls.rating = Rating.objects.create(
                user_id = random.randrange(1,100),
                solution_id = random.randrange(1, 40),
                rating = random.choice([0, 2, 4])
            )
    
    def setUp(self):
        self.access_token = self.client.post(reverse('user_auth_view'), self.user_data).data['access']

        
    def test_created_worry(self):
        url = reverse('make_worry')
        category = random.choice(['일상', '취미', '취업', '음식'])
        response = self.client.post(
            path = url,
            data = {'category': category,
                    'content': self.faker.sentence(),
                    'mbti': UserChr.objects.get(user_id=self.user_id).mbti},
            HTTP_AUTHORIZATION = f'Bearer {self.access_token}'
        )
        print(response.data)
        self.assertEqual(response.status_code, 200)