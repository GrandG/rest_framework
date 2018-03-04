from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status


# @api_view(['GET', 'POST'])
# def snippet_list(request, format=None):
#     if request.method == 'GET':
#         snippet_list = Snippet.objects.all()
#         serializer = SnippetSerializer(snippet_list, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == 'POST':
#         data = request.data
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) 
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, id, format=None):
#     try:
#         snippet = Snippet.objects.get(id=id)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == 'PUT':
#         data = request.data
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#     if request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# from now on, use class base view instead

class SnippetList(APIView):
    def get(self, request, *args, **kwargs):
        snippet = Snippet.objects.all()
        serializer = SnippetSerializer(snippet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
            return snippet
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        snippet = self.get_object(pk)
        data = request.data
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)