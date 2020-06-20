from rest_framework import viewsets
from jobs.serializer import JobSerializer
from jobs.model import Job

class JobsViewSet(viewsets.ViewSet):
    """Viewset for view and editing jobs"""
    serializer_class = JobSerializer
    queryset = Job.objects.all()
