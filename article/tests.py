# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status
# from users.models import User, UserChr
# from article.models import Category, Solution, Rating, Article, Comment
# import random
# from faker import Faker

# class MakeWorryViewTestCase(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.faker = Faker()
#         mbti_list = ['ENFP', 'ENFJ', 'ENTP', 'ENTJ', 'ESFP', 'ESFJ', 'ESTP', 'ESTJ', 'INFP', 'INFJ', 'INTP', 'INTJ', 'ISFP', 'ISFJ', 'ISTP', 'ISTJ']
        
#         for i in range(1,110):
#             cls.user = User.objects.create_user(
#                 username=cls.faker.name(), password='password1!'
#             )
            
#             cls.user_chr = UserChr.objects.create(
#                 user_id = i,
#                 mbti = random.choice(mbti_list),
#                 gender = random.choice(['W', 'M']),
#                 age = random.randrange(10, 80)
#             )
            
#         cls.user_id = 1
#         cls.user_data = {'username':User.objects.get(id = cls.user_id), 'password':'password1!'}
        
#         category_list = ['일상','취미','취업','음식']
#         for cate in category_list:
#             cls.category = Category.objects.create(
#                 category=cate
#             )
#             for _ in range(10):
#                 cls.solution = cls.category.connected_solution.create(
#                     user_id = random.randrange(1, 100),
#                     wise = cls.faker.sentence()
#                 )
            
        
#         for _ in range(100):
#             cls.rating = Rating.objects.create(
#                 user_id = random.randrange(1,100),
#                 solution_id = random.randrange(1, 40),
#                 rating = random.choice([0, 2, 4])
#             )
    
#     def setUp(self):
#         self.access_token = self.client.post(reverse('user_auth_view'), self.user_data).data['access']

        
#     def test_created_worry(self):
#         url = reverse('make_worry')
#         category = random.choice(['일상', '취미', '취업', '음식'])
#         response = self.client.post(
#             path = url,
#             data = {'category': category,
#                     'content': self.faker.sentence(),
#                     'mbti': UserChr.objects.get(user_id=self.user_id).mbti},
#             HTTP_AUTHORIZATION = f'Bearer {self.access_token}'
#         )
#         print(response.data)
#         self.assertEqual(response.status_code, 200)





# class Command(BaseCommand):
#     help = "이 커맨드를 통해 랜덤한 테스트 유저 데이터를 만듭니다."

#     def add_arguments(self, parser):
#             parser.add_argument(
#             "--total",
#             default=2,
#             type=int,
#             help="몇 명의 유저를 만드나"
#         )
    
#     def handle(self, *args, **options):
#         total = options.get("total")
#         seeder = Seed.seeder()
#         seeder.add_entity(
#             User,
#             total,
#             {
#                 "username": lambda x: seeder.faker.name(),
#                 "password" : lambda x: seeder.faker.password()
#             }
#         )
#         seeder.execute()
#         self.stdout.write(self.style.SUCCESS(f"{total}명의 유저가 작성되었습니다."))




# # 이미지 업로드
# from django.test.client import MULTIPART_CONTENT, encode_multipart, BOUNDARY
# from PIL import Image
# import tempfile

# def get_temporary_image(temp_file):
#     size = (500, 500)
#     color = (255, 0, 0, 0)
#     image = Image.new("RGBA", size, color)
#     image.save(temp_file, 'png')
#     return temp_file


# class SolutionCreateTestCase(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user_data = {'username':'john', 'password':'password1!'}
#         cls.user = User.objects.create_user('john', 'password1!')
    
#     def setUp(self):
#         self.access_token = self.client.post(reverse('user_auth_view'), self.user_data).data['access']
    
#     def test_fail_if_not_logged_in(self):
#         url = reverse("make_worry")
#         reponse = self.client.get(url)
#         self.assertEqual(reponse.status_code, 401)
    
#     def test_created_worry(self):
#         reponse = self.client.post(
#             path=reverse("make_worry"),
#             data=self.worry_data,
#             HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
#         )
#         self.assertEqual(reponse.status_code, 200)
    
#     def test_make_solution(self):
#         temp_file = tempfile.NamedTemporaryFile()
#         temp_file.name = "image.png"
#         image_file = get_temporary_image(temp_file)
#         image_file.seek(0)
#         self.make_solution_data = {'solution_image':image_file, 'wise':'abcdefg', 'article_id':2 }
#         response = self.client.post(
#             path = reverse("make_solution"),
#             data = encode_multipart(data = self.make_solution_data, boundary=BOUNDARY),
#             content_type=MULTIPART_CONTENT,
#             HTTP_AUTHORIZATION= f"Bearer {self.access_token}"
#         )
#         self.assertEqual(response.status_code, 200)