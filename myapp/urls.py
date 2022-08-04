from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name = "index"),
	path('about/', about, name = "about"),
	path('post/', post, name = "post"),
	path('contact/', contact, name = "contact"),
	path('newpost/', newpost, name = "newpost"),
	path('post_edit/<int:id>', post_edit, name = "post_edit"),
	path('post_delete/<int:id>', post_delete, name = "post_delete"),
	path('register/', registerUser, name = "register"),
	path('login/', loginUser, name = "login"),
	path('logout/', logoutUser, name = "logout"),


]