# Generated by Django 4.1.5 on 2023-06-09 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0008_alter_author_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='tel',
            field=models.IntegerField(default='(234) ', null=True),
        ),
    ]