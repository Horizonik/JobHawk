from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Job
from .serializers import JobSerializer
from rest_framework import viewsets


@login_required
def saml_auth(request):
    user_data = {
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }
    return JsonResponse(user_data)


@login_required
class JobView(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
