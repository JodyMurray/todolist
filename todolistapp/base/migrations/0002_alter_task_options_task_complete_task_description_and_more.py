# Generated by Django 4.2.5 on 2023-09-19 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete']},
        ),
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='Task', max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
