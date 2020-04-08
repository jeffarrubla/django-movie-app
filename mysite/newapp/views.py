from django.shortcuts import render
from .models import Movies
# Create your views here.

def movie_list(request):
	movies_objects = Movies.objects.all()
	return render(request,'newapp/movie_list.html',{'movies_objects':movies_objects})
