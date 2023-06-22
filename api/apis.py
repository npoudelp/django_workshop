from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import blood_doner as doner_data
from api.serializers import blood_doner_serializers


@api_view(['GET', 'POST'])
def blood_doner(request):
    if request.method == 'GET':
        doners = doner_data.objects.all().order_by('-id')
        serializer = blood_doner_serializers(doners, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = blood_doner_serializers(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.data, status=204)


@api_view()
def index(request):
    return Response('message''Test from api..')


@api_view(['GET', 'PUT', 'DELETE'])
def view_doner(request, id):
    try:
        doner = doner_data.objects.get(id=id)
    except doner_data.DoesNotExist:
        return Response({'data':"Doner doesnot exist.."}, status=404)
    
    if request.method == 'GET':            
        searializer = blood_doner_serializers(doner)
        return Response(data= searializer.data)
    elif request.method == 'PUT':
        searializer = blood_doner_serializers(doner, data=request.data)
        if(searializer.is_valid(raise_exception=True)):
            searializer.save()
            return Response(searializer.data)
    elif request.method == "DELETE":
        doner.delete()
        return Response(data=None, status=204)
    else:
        return Response({'data':"Doner doesnot exist.."}, status=404)