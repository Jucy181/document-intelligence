from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from books.models import Book
from .serializers import BookSerializer



class BookListView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class BookRecommendationView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)
        recommendations = Book.objects.exclude(id=pk)[:5]
        serializer = BookSerializer(recommendations, many=True)
        return Response(serializer.data)


class BookSummaryView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)
        summary = f"This book titled '{book.title}'is written by {book.author}.It tals about {book.description}."
        return Response({
            "title": book.title,
            "summary": summary
        })
