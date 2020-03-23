# Generated by Django 3.0.4 on 2020-03-22 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmedia', '0003_copy_media_permissions_to_collections'),
        ('flex', '0006_auto_20200322_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='featured_media',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
    ]