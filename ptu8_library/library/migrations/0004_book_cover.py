# Generated by Django 4.1.7 on 2023-02-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_author_description_alter_bookinstance_due_back'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='library/covers/', verbose_name='cover'),
        ),
    ]
