from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from drf_yasg.utils import swagger_auto_schema

from .models import Course
from .serializers import CourseSerializer

# Create your views here.
class CourseListCreateAPIView(APIView):
    @swagger_auto_schema(
        operation_summary="List Courses",
        responses={200: CourseSerializer(many=True)}
    )
    def get(self, request):

        courses = Course.objects.filter(is_active = True)

        serializer = CourseSerializer(
            courses,
            many=True
        )

        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create Course",
        request_body=CourseSerializer,
        responses={
            201: CourseSerializer,
            400: "Invalid input"
        }
    )
    def post(self, request):

        serializer = CourseSerializer(
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
    

class CourseDetailAPIView(APIView):

    def get_object(self, pk):

        return get_object_or_404(
            Course,
            pk=pk,
            is_active = True
        )

    @swagger_auto_schema(
        operation_summary="Retrieve Course",
        responses={200: CourseSerializer}
    )
    def get(self, request, pk):

        course = self.get_object(pk)

        serializer = CourseSerializer(course)

        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update Course",
        request_body=CourseSerializer,
        responses={200: CourseSerializer}
    )
    def put(self, request, pk):

        course = self.get_object(pk)

        serializer = CourseSerializer(
            course,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    @swagger_auto_schema(
        operation_summary="Partial Update Course",
        request_body=CourseSerializer,
        responses={200: CourseSerializer}
    )
    def patch(self, request, pk):

        course = self.get_object(pk)

        serializer = CourseSerializer(
            course,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)

    @swagger_auto_schema(
        operation_summary="Delete Course",
        responses={204: "Course deleted"}
    )
    def delete(self, request, pk):

        course = self.get_object(pk)

        course.is_active = False
        course.save()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )