from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from drf_yasg.utils import swagger_auto_schema

from .models import Vendor
from .serializers import VendorSerializer

# Create your views here.
class VendorListCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="List Vendors",
        responses={200: VendorSerializer(many=True)}
    )
    def get(self, request):

        vendors = Vendor.objects.filter(is_active = True)

        serializer = VendorSerializer(
            vendors,
            many=True
        )

        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create Vendor",
        request_body=VendorSerializer,
        responses={
            201: VendorSerializer,
            400: "Invalid input"
        }
    )
    def post(self, request):

        serializer = VendorSerializer(
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
    

class VendorDetailAPIView(APIView):

    def get_object(self, pk):

        return get_object_or_404(
            Vendor,
            pk=pk,
            is_active = True
        )

    @swagger_auto_schema(
        operation_summary="Retrieve Vendor",
        responses={200: VendorSerializer}
    )
    def get(self, request, pk):

        vendor = self.get_object(pk)

        serializer = VendorSerializer(vendor)

        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update Vendor",
        request_body=VendorSerializer,
        responses={200: VendorSerializer}
    )
    def put(self, request, pk):

        vendor = self.get_object(pk)

        serializer = VendorSerializer(
            vendor,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    @swagger_auto_schema(
        operation_summary="Partial Update Vendor",
        request_body=VendorSerializer,
        responses={200: VendorSerializer}
    )
    def patch(self, request, pk):

        vendor = self.get_object(pk)

        serializer = VendorSerializer(
            vendor,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    @swagger_auto_schema(
        operation_summary="Delete Vendor",
        responses={204: "Vendor deleted"}
    )
    def delete(self, request, pk):

        vendor = self.get_object(pk)

        vendor.is_active = False
        vendor.save()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )