from django.db import models
from django.contrib.postgres.fields import ArrayField, CICharField


def get_skills_default():
    return []

#Maps to a "Job" table in the DB
class Job(models.Model):
    title = CICharField(max_length=500)
    skills = ArrayField(models.CharField(max_length=200), default=get_skills_default)

#Maps to a "Candidate" table in the DB
class Candidate(models.Model):
    title = CICharField(max_length=500)
    skills = ArrayField(models.CharField(max_length=200), default=get_skills_default)