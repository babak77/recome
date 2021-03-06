# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-19 20:07
from __future__ import unicode_literals

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
            name='Gener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='gener')),
                ('desccription', models.CharField(blank=True, max_length=200, null=True, verbose_name='gener description')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='title')),
                ('pub_date', models.DateField(blank=True, null=True)),
                ('wikiPageUrl', models.CharField(blank=True, max_length=300, null=True, verbose_name='wikipedia page')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('gener', models.ManyToManyField(related_name='movieGener', to='movies.Gener')),
                ('likes', models.ManyToManyField(blank=True, related_name='movieLikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=200, unique=True, verbose_name='Full name')),
                ('firstname', models.CharField(max_length=200, verbose_name='first name')),
                ('lastname', models.CharField(max_length=200, verbose_name='last name')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('place_of_birth', models.CharField(blank=True, max_length=200, null=True)),
                ('place_of_death', models.CharField(blank=True, max_length=200, null=True)),
                ('wikiPediaPage_ID', models.CharField(blank=True, max_length=200, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movieUserRating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='WorkedOn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Person')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Role')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='staff',
            field=models.ManyToManyField(through='movies.WorkedOn', to='movies.Person'),
        ),
    ]
