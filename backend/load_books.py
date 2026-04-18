import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from books.models import Book
from rag.vector_store import add_books, collection

# Clear old data (important)
try:
    collection.delete(where={})
except:
    pass

books = Book.objects.all()

for book in books:
    try:
        print("Adding:", book.description)
        add_books(book.id, book.description)
    except Exception as e:
        print("ERROR:", e)

print("Total stored:", collection.count())