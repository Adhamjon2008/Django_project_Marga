# Generated by Django 4.1 on 2022-09-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0002_xabar_yuborish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('matn', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Xodimlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='media')),
                ('lavozim', models.CharField(max_length=30)),
                ('ism', models.CharField(max_length=30)),
                ('malumot', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Xabar_yuborish',
        ),
    ]