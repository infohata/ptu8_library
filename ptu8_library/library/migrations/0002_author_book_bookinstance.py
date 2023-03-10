# Generated by Django 4.1.7 on 2023-02-21 12:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(db_index=True, max_length=100, verbose_name='last name')),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='title')),
                ('summary', models.TextField(blank=True, max_length=4000, null=True, verbose_name='summary')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='library.author', verbose_name='author')),
                ('genre', models.ManyToManyField(help_text='select genre(s) for this book', to='library.genre', verbose_name='genre(s)')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for a book copy', primary_key=True, serialize=False, verbose_name='ID')),
                ('due_back', models.DateField(blank=True, db_index=True, null=True, verbose_name='due_back')),
                ('status', models.CharField(choices=[('m', 'managed'), ('r', 'reserved'), ('t', 'taken'), ('a', 'available'), ('u', 'unavailable')], default='a', max_length=1, verbose_name='status')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_instances', to='library.book', verbose_name='book')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
    ]
