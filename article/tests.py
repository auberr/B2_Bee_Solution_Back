from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from article.models import Category, Solution, Rating, Article, Comment



class MakeWorryViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {'username':'john', 'password':'password1!'}
        cls.user = User.objects.create_user('john', 'password1!')

        #유저 데이터 112개 만들기
        for user_id in range(1,113):
            User.objects.create_user(
                username=f'john{user_id}', password=f'password1!{user_id}'
            )

        category_list = ['일상','취미','취업','음식']
        for category in category_list:
            Category.objects.create(
                category=category
            )
        
        for solution_data in range(1, 50):
            Solution.objects.create(
                user=User.objects.get(id=solution_data), wise='wise', category=category.set()
            )
        
        print(Solution.objects.get(1))

        # for rating in range(113):
        #     Rating.objects.create(
        #         user=rating, solution=rating, rating=2
        #     )

        
    def test_created_worry(self):
        reponse = self.client.post(
            path=reverse("make_worry"),
            data=self.worry_data,
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )
        self.assertEqual(reponse.status_code, 200)

        #솔루션이랑 매칭되는 워리 만들기




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