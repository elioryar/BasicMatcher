# Generated by Django 4.0 on 2021-12-14 15:33

import app.models
import django.contrib.postgres.fields
import django.contrib.postgres.fields.citext
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_candidate_skills_alter_job_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.citext.CICharField(max_length=200), default=app.models.get_skills_default, size=None),
        ),
        migrations.AlterField(
            model_name='job',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.citext.CICharField(max_length=200), default=app.models.get_skills_default, size=None),
        ),
    ]