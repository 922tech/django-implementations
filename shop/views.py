from django.http import Http404, HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Product, ProductBrand, ProductCategory
from rest_framework.permissions import DjangoObjectPermissions
from time import time
from rest_framework.response import Response
from djangoProject4.custome_module import my_filter


class ProductCRUD(ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    # permission_classes = [DjangoObjectPermissions]
    lookup_field = 'slug'

    # def get_permissions(self):
    #     if self.action not in ['GET','HEAD','OPTIONS']:
    #         return [DjangoObjectPermissions()]
    #     return [AllowAny()]


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            _filter = lambda x:my_filter(x, ['id', 'title', 'image', 'brand','price','is_active'])  
            data =  [_filter(i) for i in serializer.data if not i['is_delete']]
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        serializer.data =  my_filter(serializer["results"],['id', 'title', 'thumbnail', 'category'])
        return Response(serializer.data)

