from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Genre(models.Model):
	name = models.CharField(max_length=50, verbose_name='Название жанра')
	slug = models.SlugField()

	def get_absolute_url(self):
		return reverse('app:genre_detail', args=[self.slug])

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Жанр'
		verbose_name_plural = 'Жанры'


class Artist(models.Model):
	name = models.CharField(max_length=250, verbose_name='Имя Артиста')
	slug = models.SlugField()
	desc = models.TextField(verbose_name='Описание артиста')
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='ЖАНР')
	art_img = models.ImageField(upload_to='art_img/', verbose_name='Картинка артиста')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Артист'
		verbose_name_plural = 'Артисты'


class Album(models.Model):
	name = models.CharField(max_length=250, verbose_name='Название альбома')
	desc = models.TextField(verbose_name='Описание альбома')
	slug = models.SlugField()
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Артист')
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
	release_date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='alb_img/', verbose_name='Обложка альбома')

	def get_absolute_url(self):
		return reverse('app:album_detail', args=[self.slug])

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Альбом'
		verbose_name_plural = 'Альбомы'


class Comment(models.Model):
	author = models.CharField(max_length=255, verbose_name="Имя коментатора")
	comment = models.TextField(verbose_name="Текст комментария")
	album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name="альбом")
	creat_comment = models.DateTimeField(auto_now_add=True)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

	@property
	def children(self):
		return Comment.objects.filter(parent=self).order_by('-creat_comment').all()

	@property
	def is_parent(self):
		if self.parent is None:
			return True
		return False

	def __str__(self):
		return f"{self.author} | {self.album.name}"

	class Meta:
		verbose_name = "Комментарий"
		verbose_name_plural = "Комментарии"
	


class Composition(models.Model):
	name = models.CharField(max_length=250, verbose_name='Название трека')
	slug = models.SlugField(null=True)
	album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Альбом')
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
	desc = models.TextField(verbose_name='Описание трека')
	release_date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='comp_img/', verbose_name='Обложка трека')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Композиция'
		verbose_name_plural = verbose_name