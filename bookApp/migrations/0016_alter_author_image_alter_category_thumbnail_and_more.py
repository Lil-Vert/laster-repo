# Generated by Django 4.1.5 on 2023-06-11 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0015_alter_author_image_alter_category_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(null=True, upload_to='myApp/image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to='myApp/image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(null=True, upload_to='myApp/image'),
        ),
    ]
