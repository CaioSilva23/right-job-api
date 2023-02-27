from rest_framework.views import APIView
from ..serializers import tecnologia_serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404
from ..models import Tecnologia
from ..pagination import PaginacaoCustom



# CLASSE COM MÉTODOS Q NÃO RECEBEM PARAMETRO
class TecnologiasList(APIView):

    #permission_classes = [IsAuthenticated,]

    def get(self, request, format=None):
        '''MÉTODO RESPOSÁVEL LISTAR TODAS AS TECNOLOGIAS'''
        pagination = PaginacaoCustom()
        tecnologias = get_list_or_404(Tecnologia)
        resultado = pagination.paginate_queryset(tecnologias, request)
        serializer = tecnologia_serializers.TecnologiaSerializers(resultado, many=True)
        return pagination.get_paginated_response(serializer.data)
        #return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        '''MÉTODO RESPOSÁVEL CADASTRAR UMA NOVA TECNOLOGIA'''
        serializer = tecnologia_serializers.TecnologiaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CLASSE COM MÉTODOS Q RECEBEM PARAMETRO
class TecnologiaDetail(APIView):
    
    def get(self, request, id, format=None):
        '''MÉTODO RESPOSÁVEL POR RETORNAR UMA TECNOLOGIA POR ID'''
        tecnologia = get_object_or_404(Tecnologia, id=id)
        serializer = tecnologia_serializers.TecnologiaSerializers(tecnologia, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)        

    def put(self, request, id, format=None):
        '''MÉTODO RESPOSÁVEL POR EDITAR UMA TECNOLOGIA POR ID'''
        tecnologia = get_object_or_404(Tecnologia, id=id)
        serializer = tecnologia_serializers.TecnologiaSerializers(data=request.data, instance=tecnologia)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        '''MÉTODO RESPOSÁVEL POR REMOVER UMA TECNOLOGIA POR ID'''
        tecnologia = get_object_or_404(Tecnologia, id=id)
        tecnologia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

