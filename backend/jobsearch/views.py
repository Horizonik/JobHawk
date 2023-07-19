from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *


class ReactView(APIView):
    serializer_class = ReactSerializer

    def get(self, request):
        output = [
            {
                "id": output.id,
                "title": output.title,
                "company": output.company,
                "location": output.location,
                "description": output.description,
                "requirements": output.requirements,
                "related_keywords": output.related_keywords,
                "url": output.url,
            }
            for output in Job.objects.all()
        ]

        return Response(output)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)