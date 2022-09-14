from rest_framework.generics import (ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView)
from articles.models import Articles
from .serialzers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# @api_view(['GET', 'POST'])
# def students_list(request):
#     if request.method == 'GET':
#         data = Articles.objects.all()

#         serializer = ArticleSerializer(data, context={'request': request}, many=True)

#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
            
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT', 'DELETE'])
# def students_detail(request, pk):
#     try:
#         student = Articles.objects.get(pk=pk)
#     except Articles.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = ArticleSerializer(student, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ArticleView(CreateAPIView):
#     parser_classes = (FormParser,MultiPartParser, FileUploadParser )

#     queryset = Articles.objects.all()
#     serializer = ArticleSerializer(queryset, many=True)

#     def post(self, request, *args, **kwargs):
#         articles_serializer = ArticleSerializer(request.POST, request.FILES)
#         if articles_serializer.is_valid():
#              articles_serializer.save()
#              return Response(articles_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#              print('error ', articles_serializer.errors)
#              return Response(articles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArticleListView(ListAPIView):
#        queryset = Articles.objects.all()
#        serializer_class = ArticleSerializer

# class ArticleDetailView(RetrieveAPIView):
#       queryset = Articles.objects.all()
#       serializer_class = ArticleSerializer

# class ArticleCreateView(CreateAPIView):
#       queryset = Articles.objects.all()
#       serializer_class = ArticleSerializer

# class ArticleUpdateView(UpdateAPIView):
#       queryset = Articles.objects.all()
#       serializer_class = ArticleSerializer

# class ArticleDeleteView(DestroyAPIView):
#       queryset = Articles.objects.all()
#       serializer_class = ArticleSerializer
    
class ArticleViewSet(viewsets.ModelViewSet):
    
    #parser_classes = (FormParser,MultiPartParser, FileUploadParser )
    permission_classes = []

    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()
    
   
    
class ArticleCreateView(CreateAPIView):
    permission_classes = []
    #parser_classes = (FormParser,MultiPartParser, FileUploadParser )
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()
    #serializer = ArticleSerializer(queryset, many=True)


    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(True, status=200)


class ArticlesViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Articles.objects.all()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Articles.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
