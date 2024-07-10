from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Customer, Product, SaleHeader
from .serializer import CustomerSerializer, ProductSerializer, SaleHeaderSerializer

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SaleHeaderViewSet(viewsets.ModelViewSet):
    queryset = SaleHeader.objects.all()
    serializer_class = SaleHeaderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            sale_header = serializer.save()  # Guarda el encabezado de venta y retorna el objeto creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)