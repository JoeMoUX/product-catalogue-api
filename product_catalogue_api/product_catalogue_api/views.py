from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def not_found(request, unknown_path):
    return Response({'unknown_path': unknown_path}, status=status.HTTP_404_NOT_FOUND)