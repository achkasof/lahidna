# Generated by Django 4.0.4 on 2022-05-05 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='photo',
            field=models.ImageField(blank=True, default='static/src/upload/profile.png', max_length=200, upload_to='static/src/upload/', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='blogger',
            name='photo',
            field=models.ImageField(blank=True, default='static/src/upload/profile.png', max_length=200, upload_to='static/src/upload/', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='photo',
            field=models.ImageField(blank=True, default='static/src/upload/profile.png', max_length=200, upload_to='static/src/upload/', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='personality',
            name='photo',
            field=models.ImageField(blank=True, default='static/src/upload/profile.png', max_length=200, upload_to='static/src/upload/', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, default='static/src/upload/profile.png', max_length=200, upload_to='static/src/upload/', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='scientist',
            name='photo',
            field=models.ImageField(blank=True, default='static/src/upload/profile.png', max_length=200, upload_to='static/src/upload/', verbose_name='photo'),
        ),
    ]
