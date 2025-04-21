from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Geliştirme'),
        ('ai', 'Yapay Zeka'),
        ('app', 'Uygulama Geliştirme'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='web')

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SupportMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    reason = models.CharField(max_length=100)
    message = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.reason}"

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    certificate = models.ImageField(upload_to='certificates/', blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    certificate = models.ImageField(upload_to='certificates/', blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author} - {self.post.title}"