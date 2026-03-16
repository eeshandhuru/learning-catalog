from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer

# Create your views here.
class ProductCourseMappingListCreateAPIView(
        APIView):
    @swagger_auto_schema(
        operation_summary="List Product Course Mappings",
        manual_parameters=[
            openapi.Parameter(
                "product_id",
                openapi.IN_QUERY,
                description="Filter by product",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                "course_id",
                openapi.IN_QUERY,
                description="Filter by course",
                type=openapi.TYPE_INTEGER
            ),
        ],
        responses={200: ProductCourseMappingSerializer(many=True)}
    )
    def get(self, request):

        queryset = ProductCourseMapping.objects.filter(
            is_active=True
        )

        product_id = request.query_params.get(
            "product_id"
        )

        course_id = request.query_params.get(
            "course_id"
        )

        if product_id:
            queryset = queryset.filter(
                product_id=product_id
            )

        if course_id:
            queryset = queryset.filter(
                course_id=course_id
            )

        serializer = ProductCourseMappingSerializer(
            queryset,
            many=True
        )

        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create Product Course Mapping",
        request_body=ProductCourseMappingSerializer,
        responses={201: ProductCourseMappingSerializer}
    )
    def post(self, request):

        serializer = ProductCourseMappingSerializer(
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
        

class ProductCourseMappingDetailAPIView(
        APIView):

    def get_object(self, pk):

        return get_object_or_404(
            ProductCourseMapping,
            pk=pk,
            is_active=True
        )
    
    @swagger_auto_schema(
        operation_summary="Retrieve Product Course Mapping",
        responses={200: ProductCourseMappingSerializer}
    )
    def get(self, request, pk):

        mapping = self.get_object(pk)

        serializer = ProductCourseMappingSerializer(
            mapping
        )

        return Response(serializer.data)
    
    @swagger_auto_schema(
        operation_summary="Update Mapping",
        request_body=ProductCourseMappingSerializer,
        responses={200: ProductCourseMappingSerializer}
    )
    def put(self, request, pk):

        mapping = self.get_object(pk)

        serializer = ProductCourseMappingSerializer(
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
        request_body=ProductCourseMappingSerializer,
        responses={200: ProductCourseMappingSerializer}
    )
    def patch(self, request, pk):

        mapping = self.get_object(pk)

        serializer = ProductCourseMappingSerializer(
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