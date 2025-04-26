from django.test import TestCase
from django.urls import reverse
from .models import Project, ContactMessage, Education, Achievement, Post, SupportMessage
from django.utils.text import slugify

class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Test Project",
            description="This is a test project.",
            image="project_images/test_image.jpg",
            category="web"
        )

    def test_project_str(self):
        self.assertEqual(str(self.project), "Test Project")

    def test_project_creation(self):
        project = Project.objects.get(title="Test Project")
        self.assertEqual(project.description, "This is a test project.")
        self.assertEqual(project.category, "web")

class ContactMessageModelTest(TestCase):
    def setUp(self):
        self.message = ContactMessage.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            message="This is a test message."
        )

    def test_contact_message_creation(self):
        message = ContactMessage.objects.get(name="John Doe")
        self.assertEqual(message.email, "john.doe@example.com")
        self.assertEqual(message.message, "This is a test message.")

    def test_contact_message_str(self):
        self.assertEqual(str(self.message), "John Doe")

class EducationModelTest(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            institution="Selçuk Üniversitesi",
            degree="Makine",
            start_year=2007,
            end_year=2009
        )

    def test_education_str(self):
        self.assertEqual(str(self.education), "Makine - Selçuk Üniversitesi")

    def test_education_creation(self):
        education = Education.objects.get(institution="Selçuk Üniversitesi")
        self.assertEqual(education.degree, "Makine")
        self.assertEqual(education.start_year, 2007)

class AchievementModelTest(TestCase):
    def setUp(self):
        self.achievement = Achievement.objects.create(
            title="Python Sertifikası",
            year=2025
        )

    def test_achievement_str(self):
        self.assertEqual(str(self.achievement), "Python Sertifikası")

    def test_achievement_creation(self):
        achievement = Achievement.objects.get(title="Python Sertifikası")
        self.assertEqual(achievement.year, 2025)

class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Test Blog Post",
            content="This is a test blog post.",
            slug=slugify("Test Blog Post")
        )

    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Blog Post")

    def test_post_creation(self):
        post = Post.objects.get(slug=slugify("Test Blog Post"))
        self.assertEqual(post.title, "Test Blog Post")
        self.assertEqual(post.content, "This is a test blog post.")

class ViewTests(TestCase):
    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_projects_page_view(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)

    def test_blog_page_view(self):
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view(self):
        post = Post.objects.create(
            title="Test Post",
            content="Test content",
            slug=slugify("Test Post")
        )
        response = self.client.get(reverse('post_detail', args=[post.slug]))
        self.assertEqual(response.status_code, 200)


class SupportMessageModelTest(TestCase):
    def setUp(self):
        self.message = SupportMessage.objects.create(
            name="Jane Doe",
            phone="1234567890",
            email="jane.doe@example.com",
            reason="technical",
            message="This is a test support message."
        )

    def test_support_message_str(self):
        self.assertEqual(str(self.message), "Jane Doe - technical")