from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from drf_yasg.utils import swagger_auto_schema

from .models import Certification
from .serializers import CertificationSerializer

# Create your views here.
class CertificationListCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="List Certifications",
        responses={200: CertificationSerializer(many=True)}
    )
    def get(self, request):

        certifications = Certification.objects.filter(is_active = True)

        serializer = CertificationSerializer(
            certifications,
            many=True
        )

        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create Certification",
        request_body=CertificationSerializer,
        responses={
            201: CertificationSerializer,
            400: "Invalid input"
        }
    )
    def post(self, request):

        serializer = CertificationSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

class CertificationDetailAPIView(APIView):

    def get_object(self, pk):

        return get_object_or_404(
            Certification,
            pk=pk,
            is_active = True
        )

    @swagger_auto_schema(
        operation_summary="Retrieve Certification",
        responses={200: CertificationSerializer}
    )
    def get(self, request, pk):

        certification = self.get_object(pk)

        serializer = CertificationSerializer(certification)

        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update Certification",
        request_body=CertificationSerializer,
        responses={200: CertificationSerializer}
    )
    def put(self, request, pk):

        certification = self.get_object(pk)

        serializer = CertificationSerializer(
            certification,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    @swagger_auto_schema(
        operation_summary="Partial Update Certification",
        request_body=CertificationSerializer,
        responses={200: CertificationSerializer}
    )
    def patch(self, request, pk):

        certification = self.get_object(pk)

        serializer = CertificationSerializer(
            certification,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    @swagger_auto_schema(
        operation_summary="Delete Certification",
        responses={204: "Certification deleted"}
    )
    def delete(self, request, pk):

        certification = self.get_object(pk)

        certification.is_active = False
        certification.save()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )