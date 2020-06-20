from django.db import models


class Job(models.Model):
    """Class for manage jobs"""
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=5000)
