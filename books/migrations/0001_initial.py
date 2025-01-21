# Generated by Django 5.0.1 on 2024-01-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booktitle', models.CharField(max_length=50)),
                ('bookdetail', models.CharField(max_length=300)),
                ('bookauthor', models.CharField(max_length=50)),
                ('bookimage', models.ImageField(upload_to='book_images/')),
                ('bookpath', models.FileField(upload_to='book_path/')),
            ],
        ),
    ]
