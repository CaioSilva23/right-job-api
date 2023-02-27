from rest_framework.views import APIView
from ..serializers import vaga_serializers
from rest_framework.response import Response
from rest_framework import status
from ..pagination import PaginacaoCustom
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from ..models import Vaga


class VagaList(APIView):
    #permission_classes = [IsAuthenticated,]


    def get(self, request, format=None):
        '''MÉTODO RESPOSÁVEL LISTAR TODAS AS VAGAS'''
        pagination = PaginacaoCustom()
        vagas = get_list_or_404(Vaga)
        resultado = pagination.paginate_queryset(vagas, request)
        serializer = vaga_serializers.VagaSerializers(resultado, many=True)
        return pagination.get_paginated_response(serializer.data) # PAGINAÇÃO
        #return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        '''MÉTODO RESPOSÁVEL CADASTRAR UMA NOVAS VAGAS'''
        serializer = vaga_serializers.VagaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VagaDetail(APIView):

    def get(self, request, id, format=None):
        '''MÉTODO RESPOSÁVEL POR RETORNAR UMA VAGA POR ID'''
        vaga = get_object_or_404(Vaga, id=id)
        serializer = vaga_serializers.VagaSerializers(vaga, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        vaga =get_object_or_404(Vaga, id=id)
        serializer = vaga_serializers.VagaSerializers(data=request.data, instance=vaga)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        '''MÉTODO RESPOSÁVEL POR REMOVER UMA VAGA POR ID'''
        vaga = get_object_or_404(Vaga, id=id)
        vaga.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
