from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']



class ProductPositionSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = StockProduct
            fields = ['product', 'quantity', 'price']
    

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']
    
         

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        print(validated_data)
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        for position in positions:
            position['stock'] = stock
            StockProduct.objects.create(**position)
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        for position in positions:
            StockProduct.objects.update_or_create(stock=stock, product=position.get('product'),
                                                  defaults={'quantity': position.get('quantity'),
                                                            'price': position.get('price')})

        return stock
