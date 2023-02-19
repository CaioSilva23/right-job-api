from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response



class PaginacaoCustom(PageNumberPagination):
    page_size = 3 # registro por página 
    page_size_query_param = 'tamanho_pagina' # parametro para alterar o limite de registro por página "?tamanho_pagina='valor'" 
    max_page_size = 10 # max registro por página 

    
    def get_paginated_response(self, data):
        '''SOBRESCREVENDO O MÉDOTO get_paginated_response e personalizando a exibição das informações'''
        return Response(
            {
                'links': {
                    'total_registros': self.page.paginator.count,
                    'total_pages': int(round(self.page.paginator.count/self.page_size, 1)),
                    'next': self.get_next_link(),
                    'previuos': self.get_previous_link()
                },
                'results': data
            }
        )