from django.http.response import Http404
from django.shortcuts import render
from Nestapp.serializer import AuthorSerializer ,BookSerializer
from  Nestapp.models import Author
from  Nestapp.models import Book
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
# Authentication Lib
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions


# Create your views here.
from rest_framework.views import APIView


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # Authentication
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated,DjangoModelPermissions]

# class AuthorDetailView(APIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

class AuthorDetailView(APIView):
    def get_object(self,pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        course = self.get_object(pk)
        serializer = AuthorSerializer(course)
        return Response(serializer.data)

    def put(self,request,pk):
        course = self.get_object(pk)
        serializer = AuthorSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

