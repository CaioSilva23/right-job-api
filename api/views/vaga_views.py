from rest_framework.views import APIView
from ..serializers import vaga_serializers
from ..services import vaga_services
from rest_framework.response import Response
from rest_framework import status
from ..entidades.vaga import Vaga
from ..pagination import PaginacaoCustom
from rest_framework.permissions import IsAuthenticated


class VagaList(APIView):
    permission_classes = [IsAuthenticated,]


    def get(self, request, format=None):
        '''MÉTODO RESPOSÁVEL LISTAR TODAS AS VAGAS'''
        pagination = PaginacaoCustom()
        vagas = vaga_services.listar_vagas()
        resultado = pagination.paginate_queryset(vagas, request)
        serializer = vaga_serializers.VagaSerializers(resultado, many=True)
        return pagination.get_paginated_response(serializer.data)
        #return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        '''MÉTODO RESPOSÁVEL CADASTRAR UMA NOVAS VAGAS'''
        serializer = vaga_serializers.VagaSerializers(data=request.data)
        if serializer.is_valid():
            titulo = serializer.validated_data['titulo']
            descricao = serializer.validated_data['descricao']
            salario = serializer.validated_data['salario']
            tipo_contratacao = serializer.validated_data['tipo_contratacao']
            local = serializer.validated_data['local']
            quantidade = serializer.validated_data['quantidade']
            contato = serializer.validated_data['contato']
            tecnologias = serializer.validated_data['tecnologias']

            vaga_nova = Vaga(titulo=titulo, 
                            descricao=descricao, 
                            salario=salario, 
                            tipo_contratacao=tipo_contratacao, 
                            local=local, 
                            quantidade=quantidade,
                            contato=contato,
                            tecnologias=tecnologias)
            vaga_services.cadastrar_vaga(vaga_nova)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VagaDetail(APIView):

    def get(self, request, id, format=None):
        '''MÉTODO RESPOSÁVEL POR RETORNAR UMA VAGA POR ID'''
        vaga = vaga_services.listar_vaga_id(id)
        serializer = vaga_serializers.VagaSerializers(vaga, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        vaga_antiga = vaga_services.listar_vaga_id(id)
        serializer = vaga_serializers.VagaSerializers(data=request.data)
        if serializer.is_valid():
            titulo = serializer.validated_data['titulo']
            descricao = serializer.validated_data['descricao']
            salario = serializer.validated_data['salario']
            tipo_contratacao = serializer.validated_data['tipo_contratacao']
            local = serializer.validated_data['local']
            quantidade = serializer.validated_data['quantidade']
            contato = serializer.validated_data['contato']
            tecnologias = serializer.validated_data['tecnologias']
            
            vaga_nova = Vaga(titulo=titulo, 
                            descricao=descricao, 
                            salario=salario, 
                            tipo_contratacao=tipo_contratacao, 
                            local=local, 
                            quantidade=quantidade,
                            contato=contato,
                            tecnologias=tecnologias)
            vaga_services.editar_vaga(vaga_antiga=vaga_antiga, vaga_nova=vaga_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        '''MÉTODO RESPOSÁVEL POR REMOVER UMA VAGA POR ID'''
        vaga_services.remover_vaga(id)
        return Response(status=status.HTTP_204_NO_CONTENT)
