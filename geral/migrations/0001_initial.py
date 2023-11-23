# Generated by Django 4.2.4 on 2023-11-16 17:23

import django.contrib.auth.models
from django.db import migrations, models
import geral.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produto', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('fab', models.CharField(max_length=254)),
                ('quantidade', models.PositiveIntegerField()),
                ('valor', models.PositiveIntegerField(default=None, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=geral.models.upload_media)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_user', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nomeUser', models.TextField(max_length=255)),
                ('emailUser', models.EmailField(max_length=255, unique=True)),
                ('senhaUser', models.CharField(max_length=255)),
                ('idadeUser', models.IntegerField()),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]