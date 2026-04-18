from django.urls import path
from .views import BookListView,BookDetailView, BookRecommendationView, BookSummaryView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/recommend/', BookRecommendationView.as_view(), name='book-recommend'),
    path('books/<int:pk>/summary/', BookSummaryView.as_view(), name='book-summary'),
]
