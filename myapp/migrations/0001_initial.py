# Generated by Django 3.0.7 on 2020-08-28 09:08

from django.conf import settings
import django.contrib.postgres.fields.citext
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', django.contrib.postgres.fields.citext.CITextField(blank=True, max_length=25, unique=True)),
                ('link', models.URLField(max_length=1000)),
                ('hit', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='url', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
