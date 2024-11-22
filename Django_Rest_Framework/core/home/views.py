from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import PeopeSerializer

@api_view(['GET', "POST"])
def index(request):
    if request.method=="GET":
        return Response()
    return Response()

@api_view(['GET', "POST"])
def person(request):
    if request.method=="GET":
        objects = Person.objects.all()
        serializer= PeopeSerializer(objects, many=True)
        return Response(serializer.data)
    else:
        data=request.data
        serializer=PeopeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    return Response(serializer.errors)