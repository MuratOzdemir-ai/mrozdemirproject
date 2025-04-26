from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Project, Education, Achievement, Post, Comment
from .forms import ContactForm, SupportMessageForm, CommentForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def home_view(request):
    projects_count = Project.objects.count()
    certificates_count = Achievement.objects.count()
    return render(request, 'portfolio/home.html', {
        'projects_count': projects_count,
        'certificates_count': certificates_count
    })

@login_required
def projects_view(request):
    category = request.GET.get('category')
    search_query = request.GET.get('q')
    projects = Project.objects.all()
    if category:
        projects = projects.filter(category=category)
    if search_query:
        projects = projects.filter(title__icontains=search_query)
    return render(request, 'portfolio/projects.html', {'projects': projects})

def project_detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Ajax kontrolü
                return JsonResponse({'message': 'Mesajınız gönderildi!'})
            messages.success(request, 'Mesajınız başarıyla gönderildi!')
            return redirect('home')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'error': 'Form hatalı!'}, status=400)
            messages.error(request, 'Lütfen formu doğru doldurun.')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})

def thank_you_view(request):
    return render(request, 'portfolio/thank_you.html')

def education_and_achievements_view(request):
    educations = Education.objects.all()
    achievements = Achievement.objects.all()
    return render(request, 'portfolio/education_and_achievements.html', {
        'educations': educations,
        'achievements': achievements
    })

def support_message_view(request):
    if request.method == 'POST':
        form = SupportMessageForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Destek talebiniz gönderildi!'})
            messages.success(request, 'Destek talebiniz başarıyla gönderildi!')
            return redirect('home')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'error': 'Form hatalı!'}, status=400)
            messages.error(request, 'Lütfen formu doğru doldurun.')
    else:
        form = SupportMessageForm()
    return render(request, 'portfolio/support_message.html', {'form': form})

def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'portfolio/blog.html', {'posts': posts})

def blog_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(approved=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Yorumunuz gönderildi, onay bekliyor.')
            return redirect('blog_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'portfolio/blog_detail.html', {'post': post, 'comments': comments, 'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Kullanıcı giriş yaptıktan sonra yönlendirilmesini istediğiniz sayfa
    else:
        form = AuthenticationForm()

    return render(request, 'portfolio/login.html', {'form': form})
