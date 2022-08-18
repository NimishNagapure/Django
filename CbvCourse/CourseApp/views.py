from django.shortcuts import render
from CourseApp.models import Course
from CourseApp.serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from  django.http import Http404
# Create your views here.

from rest_framework import generics , mixins
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
# from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# creating custom class instead of using global or default pagination 
 
class CoursePagination(PageNumberPagination):
    page_size = 2


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePagination
    # pagination_class = LimitOffsetPagination
    # Filter
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name','rating']
    # Filter by fields
    filter_backends = [filters.SearchFilter]
    search_fields = ['^id','^name']
    # filters_backends = [filters.OrderingFilter]
    # ordering_fields = ['name','rating']
    

# Create with help of Generics
#
# class CourseList(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
# class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer


# Created views with help of mixins
#
# class CourseList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
#
# class CouresDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#         return self.update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)



# class based views  for serializers 


# class CourseList(APIView):

#     def get(self,request):
#         course = Course.objects.all()
#         serializer = CourseSerializer(course,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

# class CouresDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Course.objects.get(pk=pk)
#         except Course.DoesNotExist:
#             raise Http404

#     def get(self,request,pk):
#         course = self.get_object(pk)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)

#     def put(self,request,pk):
#         course = self.get_object(pk)
#         serializer = CourseSerializer(course,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,request,pk):
#         course = self.get_object(pk)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

