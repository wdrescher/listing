# Generated by Django 2.0.4 on 2018-04-13 17:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='owner',
            field=models.ForeignKey(default=1, on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
