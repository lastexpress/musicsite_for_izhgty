from django.contrib import admin

from .models import Genre, Artist, Album, Composition, Comment

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display = ('name',)
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
	list_display = ('name',)
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
	list_display = ('name',)
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
	list_display = ('name',)
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Comment)