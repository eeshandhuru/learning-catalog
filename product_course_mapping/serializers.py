from rest_framework import serializers
from .models import ProductCourseMapping


class ProductCourseMappingSerializer(
        serializers.ModelSerializer):

    class Meta:
        model = ProductCourseMapping

        exclude = ["is_active"]
        read_only_fields = ['created_at', 'updated_at']
        
    def validate(self, data):

        if data.get("primary_mapping"):

            product = data.get("product")

            exists = ProductCourseMapping.objects.filter(
                product=product,
                primary_mapping=True,
                is_active=True
            ).exists()

            if exists:
                raise serializers.ValidationError(
                    "Primary mapping already exists for this product."
                )

        return data
    