from rest_framework import serializers
from .models import VendorProductMapping


class VendorProductMappingSerializer(
        serializers.ModelSerializer):

    class Meta:
        model = VendorProductMapping

        exclude = ["is_active"]
        read_only_fields = ['created_at', 'updated_at']
        
    def validate(self, data):

        if data.get("primary_mapping"):

            vendor = data.get("vendor")

            exists = VendorProductMapping.objects.filter(
                vendor=vendor,
                primary_mapping=True,
                is_active=True
            ).exists()

            if exists:
                raise serializers.ValidationError(
                    "Primary mapping already exists for this vendor."
                )

        return data
    