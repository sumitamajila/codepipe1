# Generated by Django 4.1.5 on 2023-01-24 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("certification", "0002_certificationdetails_feedback_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="certificationdetails",
            name="ratings",
            field=models.FloatField(blank=True, null=True),
        ),
    ]