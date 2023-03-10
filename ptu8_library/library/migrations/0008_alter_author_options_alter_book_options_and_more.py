# Generated by Django 4.1.7 on 2023-03-03 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_bookreview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': 'author', 'verbose_name_plural': 'authors'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title'], 'verbose_name': 'book', 'verbose_name_plural': 'books'},
        ),
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'verbose_name': 'book instance', 'verbose_name_plural': 'book instances'},
        ),
        migrations.AlterModelOptions(
            name='bookreview',
            options={'ordering': ['-created_at'], 'verbose_name': 'book review', 'verbose_name_plural': 'book reviews'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'genre', 'verbose_name_plural': 'genres'},
        ),
    ]
