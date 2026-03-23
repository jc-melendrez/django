from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import Brands
from .serializer import BrandsSerializer

class BrandsViewSet(viewsets.ModelViewSet):        
    queryset=Brands.objects.all()
    serializer_class=BrandsSerializer

   

@api_view(['GET', 'POST'])
def brands_list(request):
    if request.method == 'GET':
        items = Brands.objects.all()
        serializer = BrandsSerializer(items, any=True)
        return  Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BrandsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def brands_detail(request, pk):
    try:
        item = Brands.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BrandsSerializer(item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BrandsSerializer(item, data=request.data)
        if serializer.isvalid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)