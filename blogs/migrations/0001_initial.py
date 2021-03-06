# Generated by Django 2.2 on 2019-04-12 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('excerpt', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=125)),
                ('users_id', models.IntegerField(default=0, max_length=11)),
                ('tag', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=1, max_length=6)),
                ('category_id', models.IntegerField(default=0, max_length=11)),
                ('created_at', models.DateTimeField(verbose_name='date created_at')),
                ('updated_at', models.DateTimeField(verbose_name='date updated_at')),
            ],
        ),
    ]
