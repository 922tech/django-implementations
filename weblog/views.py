
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework.permissions import DjangoObjectPermissions,IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from djangoProject4.custome_module import my_filter
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
# from django.core.cache import cache

    
# def get_post(request,slug):
    # if not cache.get(slug):
    #     p = get_object_or_404(Post,slug=slug)
    #     cache.set(slug, p)
    #     return HttpResponse('<h1>Post from db</h1>')
    # else:
    #     return HttpResponse('<h1>Post from cache</h1>')
    # p = get_object_or_404(Post,slug=slug)
    # return HttpResponse('<h1>Post from db</h1>')
        

@api_view(['GET','POST'])
def log_user(request:HttpRequest):

    if request.method == 'POST':
        # print('*****\n{request.user}*****\n')
        model = Post.objects
        kwargs = request.data
        return Response(str({'user':(request.user),'ip':request.META['REMOTE_ADDR']}))

    if request.method == 'GET':
        # print(f'*****\n{request.user}\n*****')

        k  = {'user':repr(request.user),'is_auth':request.user.is_authenticated,'ip':request.META['REMOTE_ADDR']}
        return JsonResponse(k,safe=False)


class CategoryCrud(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ('create', 'update', 'delete'):
            return DjangoObjectPermissions()
        return [permission() for permission in self.permission_classes]


class PostCRUD(ModelViewSet):
    queryset = Post.objects.filter(is_visible=True)
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views +=1
        instance.save()
        return super().retrieve(request, *args, **kwargs)
    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        _filter = lambda x:my_filter(x, ['id', 'title', 'thumbnail', 'category','slug'])  
 
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data =  [_filter(i) for i in serializer.data]
            # print(data)
            
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)        
        data =  [_filter(i) for i in serializer.data]
        return Response(data)
