from django.http import HttpRequest, HttpResponseForbidden,JsonResponse
from rest_framework.response import Response
from django.utils.deprecation import MiddlewareMixin


def auth_or_readonly_middleware(get_response):

    def auth_or_readonly(request: HttpRequest):

        # print(f'****\n{request.user},{request.user.is_authenticated}\n****')
        if request.method not in ['GET','HEAD','OPTIONS']:
            if request.path in ['/signup/','/token/','/comments/']:
             # signup/login form url - comments form url
                return get_response(request)
            else:
                if not request.user.is_authenticated:
                    return JsonResponse(data={'Access denied':'Authentication is required.'})

                return get_response(request)

        else:
            return get_response(request)


    return auth_or_readonly
                

class AuthenticatedOrReadOnlyMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request) :
        response = self.get_response
        return response(request)

    def process_request(self,request):
        response = self.get_response
        # print('//////*********\n',request.user.is_authenticated)

        if request.method not in ['GET','HEAD','OPTIONS']:
            if request.path in ['/signup/','/token/','/comments/']: # signup/login form url - comments form url
                return response(request)

            else:
                if not request.user.is_authenticated:
                    return JsonResponse(data={'Access denied':'Authentication is required.'})
                return response(request)
                