from rest_framework import serializers
from .models import Customer, Product, SaleDetail, SaleHeader

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = '__all__'

class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = '__all__'
        extra_kwargs = {
            'sale_header': {'required': False}
        }

class SaleHeaderSerializer(serializers.ModelSerializer):
    details = SaleDetailSerializer(many=True, required=False)  # Permite la creación de detalles junto con el encabezado

    class Meta:
        model = SaleHeader
        fields = '__all__'

    def create(self, validated_data):
        details_data = validated_data.pop('details', [])  # Extrae los datos de detalles del valid_data
        sale_header = SaleHeader.objects.create(**validated_data)  # Crea el encabezado de venta

        for detail_data in details_data:
            SaleDetail.objects.create(sale_header=sale_header, **detail_data)  # Crea cada detalle asociado al encabezado

        return sale_header