from ..serializers import usuario_serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UsuarioList(APIView):
    def post(self, request, format=None):
        serializer = usuario_serializers.UsuarioSerizalizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'Success': 'Usuário cadastrado com sucesso!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)