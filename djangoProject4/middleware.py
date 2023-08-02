from django.http import JsonResponse
 

class AuthenticatedOrReadOnlyMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request) :
        response = self.get_response
        return response(request)

    def process_request(self,request):
        response = self.get_response

        if request.method not in ['GET','HEAD','OPTIONS']:
            if request.path in ['/signup/','/token/','/comments/']: # signup/login form url - comments form url
                return response(request)

            else:
                if not request.user.is_authenticated:
                    return JsonResponse(data={'Access denied':'Authentication is required.'})
                return response(request)
                
