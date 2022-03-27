# Generated by Django 4.0.1 on 2022-03-11 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название альбома')),
                ('desc', models.TextField(verbose_name='Описание альбома')),
                ('slug', models.SlugField()),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='alb_img/', verbose_name='Обложка альбома')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название жанра')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название трека')),
                ('slug', models.SlugField(null=True)),
                ('desc', models.TextField(verbose_name='Описание трека')),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='comp_img/', verbose_name='Обложка трека')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.album', verbose_name='Альбом')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Композиция',
                'verbose_name_plural': 'Композиция',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя Артиста')),
                ('slug', models.SlugField()),
                ('desc', models.TextField(verbose_name='Описание артиста')),
                ('art_img', models.ImageField(upload_to='art_img/', verbose_name='Картинка артиста')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genre', verbose_name='ЖАНР')),
            ],
            options={
                'verbose_name': 'Артист',
                'verbose_name_plural': 'Артисты',
            },
        ),
        migrations.CreateModel(
            name='AlbumComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.album')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.albumcomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.artist', verbose_name='Артист'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genre', verbose_name='Жанр'),
        ),
    ]
