from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import GrindPost, GrindComment, DailyPrompt, DailyAnswer
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import never_cache
from django.utils import timezone
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register_view')
        
        User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        messages.success(request, "registration successful")
        return redirect('login_view')
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('grind_feed') #before it was 'home_view'
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect(login_view)

@login_required(login_url="login")
def home_view(request):
    return render(request, 'grind_page.html')

def create_grind_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            text = request.POST.get('text', '').strip()
            if not text:
                return redirect('grind_feed')
            tag = request.POST.get('tags')
            GrindPost.objects.create(user=request.user,content=text, tag=tag)
            return redirect('grind_feed')
        return render(request, 'grind_page.html')
    else:
        return redirect('login_view')
    
@never_cache
def grind_feed(request):
    grind_list = GrindPost.objects.all()
    return render(request, 'grind_page.html', {'grinding' : grind_list})

def respect_post(request,post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(GrindPost, id=post_id)
        post.respect_count += 1
        post.save()
        return redirect('grind_feed')
    else:
        return redirect('login_view')

def add_comment(request, post_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            text = request.POST.get('text', '').strip()
            if text:
                post = get_object_or_404(GrindPost, id=post_id)
                GrindComment.objects.create(post=post, user=request.user, text=text)
        return redirect('grind_feed')
    else:
        return redirect('login_view')
    
def daily_question(request):
    today = timezone.localdate()
    prompt = DailyPrompt.objects.filter(date=today).first()

    user_answered = False
    if prompt and request.user.is_authenticated:
        user_answered = DailyAnswer.objects.filter(prompt=prompt, user=request.user).exists()
    answers = prompt.answers.all() if prompt else []
    return render(request,'daily_question.html',{
        'prompt' : prompt,
        'answers' : answers,
        'user_answered' : user_answered,
    })

def submit_daily_answer(request,prompt_id):
    if not request.user.is_authenticated:
        return redirect('login_view')
    if request.method == 'POST':
        text = request.POST.get('text','').strip()
        prompt = get_object_or_404(DailyPrompt, id = prompt_id)
        already_answered = DailyAnswer.objects.filter(prompt=prompt, user=request.user).exists()
        if text and not already_answered:
            DailyAnswer.objects.create(prompt=prompt, user=request.user, text=text)
    return redirect('daily_question')