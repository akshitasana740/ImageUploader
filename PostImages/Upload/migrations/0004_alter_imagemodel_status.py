# Generated by Django 4.2 on 2023-06-30 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0003_imagemodel_delete_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='status',
            field=models.CharField(max_length=200),
        ),
    ]
