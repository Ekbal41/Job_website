# Generated by Django 4.1.1 on 2022-11-18 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoruser', '0009_alter_testimonial_prof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='prof',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
