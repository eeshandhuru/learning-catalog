from rest_framework import serializers
from .models import CourseCertificationMapping


class CourseCertificationMappingSerializer(
        serializers.ModelSerializer):

    class Meta:
        model = CourseCertificationMapping

        exclude = ["is_active"]
        read_only_fields = ['created_at', 'updated_at']
        
    def validate(self, data):

        if data.get("primary_mapping"):

            course = data.get("course")

            exists = CourseCertificationMapping.objects.filter(
                course=course,
                primary_mapping=True,
                is_active=True
            ).exists()

            if exists:
                raise serializers.ValidationError(
                    "Primary mapping already exists for this course."
                )

        return data
    