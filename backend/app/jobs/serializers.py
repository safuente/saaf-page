from rest_framework import serializers
from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):
    """Serializer for job object"""

    class Meta:
        model = Job
        fields = ('title', 'summary')
