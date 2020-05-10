from rest_framework.response import Response
from rest_framework.views import APIView


class APIRoot(APIView):
    """
    API Root ...
    """

    def get(self, request):
        data = {
            "accounts": "http://localhost:8000/accounts/",
            "api": "http://localhost:8000/api/",
        }
        return Response(data)
