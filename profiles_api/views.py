# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    # Test Api View

    def get(self, request, format=None):
        # returns a list of features

        an_apiview = [
            'my name is hitesh',
            'i\'m a software devloper',
            'currently working in pune',
            'companuy name is capgemini'
        ] 

        return Response({'message' : 'Hello!', 'an_apiview' : an_apiview})
    
    