from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import ZipAirlinesSerializer


class ZipAirlinesView(APIView):

    def post(self, request, format=None):
        serializer = ZipAirlinesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
