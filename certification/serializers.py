from rest_framework import serializers
from .models import Certification

class CertificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certification
        exclude = ['is_active']
        read_only_fields = ['created_at', 'updated_at']