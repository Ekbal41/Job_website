# Generated by Django 4.1.1 on 2022-11-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoruser', '0010_alter_testimonial_prof_alter_testimonial_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
