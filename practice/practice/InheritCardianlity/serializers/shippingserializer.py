from rest_framework. serializers import ModelSerializer
from InheritCardianlity.models import ShippingAddress


class ShippingAddressSerializer(ModelSerializer):


    class Meta:
        model = ShippingAddress
        fields = "__all__"
