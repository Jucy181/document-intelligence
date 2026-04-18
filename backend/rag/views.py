from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Import safely (this will work once vector_store is fixed)
try:
    from .vector_store import simple_search
except ImportError:
    simple_search = None


class AskView(APIView):
    """
    Simple RAG-style API endpoint
    """

    def post(self, request):
        query = request.data.get("query")

        if not query:
            return Response(
                {"error": "Query is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # If vector search exists
        if simple_search:
            result = simple_search(query)
        else:
            # fallback so project does not crash
            result = f"Search function not implemented yet. You asked: {query}"

        return Response(
            {
                "query": query,
                "answer": result
            },
            status=status.HTTP_200_OK
        )