# from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import CreateAPIView ,ListAPIView
from articles.models import Articles
from .serialzers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.shortcuts import render

from rest_framework import status

# class ArticleView(CreateAPIView):
#     #parser_classes = (MultiPartParser, FormParser)

#     def get(self, request, *args, **kwargs):
#         queryset = Articles.objects.all()
#         serializer = ArticleSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         articles_serializer = ArticleSerializer(request.POST, request.FILES)
#         if articles_serializer.is_valid():
#             articles_serializer.save()
#             return Response(articles_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print('error abdullah', articles_serializer.errors)
#             return Response(articles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class ArticleListView(ListAPIView):
#       queryset = Articles.objects.all()
#       serializer_class = ArticleSerializer

# class ArticleDetailView(RetrieveAPIView):
#      queryset = Articles.objects.all()
#      serializer_class = ArticleSerializer

# class ArticleCreateView(CreateAPIView):
#      queryset = Articles.objects.all()
#      serializer_class = ArticleSerializer

# class ArticleUpdateView(UpdateAPIView):
#      queryset = Articles.objects.all()
#      serializer_class = ArticleSerializer

# class ArticleDeleteView(DestroyAPIView):
#      queryset = Articles.objects.all()
#      serializer_class = ArticleSerializer
    
from rest_framework import viewsets

class ArticleViewSet(viewsets.ModelViewSet):
    parser_classes = (FormParser,MultiPartParser, FileUploadParser )

    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()
    def post(self, request, *args, **kwargs):
        articles_serializer = ArticleSerializer(data=request.POST)#,data=request.data, data=request.FILES)
        if articles_serializer.is_valid():
            articles_serializer.save()
            return Response(articles_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error abdullah', articles_serializer.errors)
            return Response(articles_serializer.errors, status=status.HTTP_400_BAD_REQUEST)