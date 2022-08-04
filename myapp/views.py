from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def index(request):
	posts = Post.objects.all().order_by('-published_date')
	return render(request, 'index.html', {'posts':posts})

def about(request):
	return render(request, 'about.html', {})

def post(request):
	return render(request, 'post.html', {})

def contact(request):
	return render(request, 'contact.html', {})

def newpost(request):
	if request.method  == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('/')
	else:
		form = PostForm()

	return render(request, 'newpost.html', {'form':form})

def post_edit(request, id):
	pst = Post.objects.get(pk = id)
	if request.method =='POST':
		form = PostForm(request.POST, instance = pst)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('/')
	else:
		form = PostForm(instance = pst)
	return render(request, 'postedit.html', {'form':form})

def post_delete(request, id):
	usr = Post.objects.get(id = id)
	usr.delete()
	return redirect('/')
	

def registerUser(request):
	if request.user.is_authenticated:
		return redirect("/")
	frm = UserCreationForm()

	if request.method == 'POST':
		frm = UserCreationForm(request.POST)
		if frm.is_valid():
			frm.save()
			return redirect("login")

	return render(request, 'register.html', {'frm':frm})


def loginUser(request):
	if request.user.is_authenticated:
		return redirect("/")
	if request.method == 'POST':
		usr = request.POST.get("username")
		pwd = request.POST.get("password")
		user = authenticate(request, username = usr, password = pwd)
		if user is not None:
			login(request, user)
			return redirect("newpost")
	return render(request, 'login.html', {})


def logoutUser(request):
	logout(request)
	return redirect("/")


	