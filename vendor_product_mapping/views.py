from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer

# Create your views here.
class VendorProductMappingListCreateAPIView(
        APIView):
    @swagger_auto_schema(
        operation_summary="List Vendor Product Mappings",
        manual_parameters=[
            openapi.Parameter(
                "vendor_id",
                openapi.IN_QUERY,
                description="Filter by vendor",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                "product_id",
                openapi.IN_QUERY,
                description="Filter by product",
                type=openapi.TYPE_INTEGER
            ),
        ],
        responses={200: VendorProductMappingSerializer(many=True)}
    )
    def get(self, request):

        queryset = VendorProductMapping.objects.filter(
            is_active=True
        )

        vendor_id = request.query_params.get(
            "vendor_id"
        )

        product_id = request.query_params.get(
            "product_id"
        )

        if vendor_id:
            queryset = queryset.filter(
                vendor_id=vendor_id
            )

        if product_id:
            queryset = queryset.filter(
                product_id=product_id
            )

        serializer = VendorProductMappingSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create Vendor Product Mapping",
        request_body=VendorProductMappingSerializer,
        responses={201: VendorProductMappingSerializer}
    )
    def post(self, request):

        serializer = VendorProductMappingSerializer(
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
        

class VendorProductMappingDetailAPIView(
        APIView):

    def get_object(self, pk):

        return get_object_or_404(
            VendorProductMapping,
            pk=pk,
            is_active=True
        )
    
    @swagger_auto_schema(
        operation_summary="Retrieve Vendor Product Mapping",
        responses={200: VendorProductMappingSerializer}
    )
    def get(self, request, pk):

        mapping = self.get_object(pk)

        serializer = VendorProductMappingSerializer(
            mapping
        )

        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_summary="Update Mapping",
        request_body=VendorProductMappingSerializer,
        responses={200: VendorProductMappingSerializer}
    )
    def put(self, request, pk):

        mapping = self.get_object(pk)

        serializer = VendorProductMappingSerializer(
            mapping,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=400
        )

    @swagger_auto_schema(
        operation_summary="Partial Update Mapping",
        request_body=VendorProductMappingSerializer,
        responses={200: VendorProductMappingSerializer}
    )
    def patch(self, request, pk):

        mapping = self.get_object(pk)

        serializer = VendorProductMappingSerializer(
            mapping,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=400
        )
        
    @swagger_auto_schema(
        operation_summary="Delete Mapping",
        responses={204: "Mapping deleted"}
    )
    def delete(self, request, pk):

        mapping = self.get_object(pk)

        mapping.is_active = False
        mapping.save()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )