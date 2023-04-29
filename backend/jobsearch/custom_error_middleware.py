from django.http import HttpResponseRedirect


class CustomErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 404:
            return HttpResponseRedirect('/error/404')
        elif response.status_code == 500:
            return HttpResponseRedirect('/error/500')
        elif response.status_code == 502:
            return HttpResponseRedirect('/error/502')
        return response
