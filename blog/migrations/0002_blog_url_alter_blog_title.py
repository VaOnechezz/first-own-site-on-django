# Generated by Django 4.1.3 on 2022-11-24 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="url",
            field=models.URLField(blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(max_length=120),
        ),
    ]