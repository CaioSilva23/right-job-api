from rest_framework.views import APIView
from ..services import tecnologia_services
from ..serializers import tecnologia_serializers
from rest_framework.response import Response
from rest_framework import status
from ..entidades import tecnologia
from rest_framework.permissions import IsAuthenticated




# CLASSE COM MÉTODOS Q NÃO RECEBEM PARAMETRO
class TecnologiasList(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request, format=None):
        '''MÉTODO RESPOSÁVEL LISTAR TODAS AS TECNOLOGIAS'''
        tecnologias = tecnologia_services.listar_tecnologias()
        serializer = tecnologia_serializers.TecnologiaSerializers(tecnologias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        '''MÉTODO RESPOSÁVEL CADASTRAR UMA NOVA TECNOLOGIA'''
        serializer = tecnologia_serializers.TecnologiaSerializers(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            nova_tecnologia = tecnologia.Tecnologia(nome=nome)
            tecnologia_services.cadastrar_tecnologia(nova_tecnologia)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CLASSE COM MÉTODOS Q RECEBEM PARAMETRO
class TecnologiaDetail(APIView):
    
    def get(self, request, id, format=None):
        '''MÉTODO RESPOSÁVEL POR RETORNAR UMA TECNOLOGIA POR ID'''
        tecnologia = tecnologia_services.listar_tecnologia_id(id)
        serializer = tecnologia_serializers.TecnologiaSerializers(tecnologia, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)        

    def put(self, request, id, format=None):
        '''MÉTODO RESPOSÁVEL POR EDITAR UMA TECNOLOGIA POR ID'''
        antiga_tecnologia = tecnologia_services.listar_tecnologia_id(id)
        serializer = tecnologia_serializers.TecnologiaSerializers(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data['nome']
            nova_tecnolgia = tecnologia.Tecnologia(nome=nome)
            tecnologia_services.editar_tecnologia(antiga_tecnologia, nova_tecnolgia)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        '''MÉTODO RESPOSÁVEL POR REMOVER UMA TECNOLOGIA POR ID'''
        tecnologia_services.remover_tecnologia(id)
        return Response(status=status.HTTP_204_NO_CONTENT)

