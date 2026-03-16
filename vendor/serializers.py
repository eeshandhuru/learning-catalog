from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        exclude = ['is_active']
        read_only_fields = ['created_at', 'updated_at']