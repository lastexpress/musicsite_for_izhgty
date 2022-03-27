from django.views import View
from django.shortcuts import render
from .models import Genre, Artist, Album, Composition, Comment
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CommentForm


# class Index(View):
# 	def get(self, request, *args, **kwargs):
# 		return render(request, 'index.html')

def MainScreen(request):
	genre = Genre.objects.all()

	artist = Artist.objects.all()

	album = Album.objects.all()

	composition = Composition.objects.all()

	dic_obj = {'genre':genre,
			   'artist':artist,
			   'album':album,
			   'composition':composition}

	return render(request, 'indexex.html', dic_obj)

def GenreDetail(request, name):
	genre = get_object_or_404(Genre, slug=name)

	genres = Genre.objects.all()

	art = Artist.objects.filter(genre_id=genre)

	alb = Album.objects.filter(genre_id=genre)

	comp = Composition.objects.filter(genre_id=genre)

	dic_obj = {'genre' : genre,
			   'genres' : genres,
			   'art' : art,
			   'alb' : alb,
			   'comp' : comp}

	return render(request, 'genre/genre_detail.html', dic_obj)


def AlbumDetail(request, slug, pk=None, *args, **kwargs):
	album = get_object_or_404(Album, slug=slug)

	


	dic_obj = {'album' : album}

	return render(request, 'album/album_detail.html', dic_obj)

