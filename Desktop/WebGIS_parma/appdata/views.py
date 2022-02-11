from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,viewsets
from .serializers import ProveSerializer
from .models import prove_geognostiche


# Create your views here.
class ProveView(viewsets.ModelViewSet):       # add this
    serializer_class = ProveSerializer          # add this
    queryset = prove_geognostiche.objects.all()

def front(request):
    context = { }
    return render(request, "index.html", context)

@api_view(['GET', 'POST'])
def prove(request):

    if request.method == 'GET':
        prove = prove_geognostiche.objects.all()
        serializer = ProveSerializer(prove, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def prove_detail(request, pk):
    try:
        prove = prove_geognostiche.objects.get(pk=pk)
    except prove_geognostiche.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        prove.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)