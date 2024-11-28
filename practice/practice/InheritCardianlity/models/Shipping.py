from django.db import models
from .Address import Address
from .User import User


class ShippingAddress(Address):
    shipping = models.ForeignKey(User, on_delete=models.CASCADE, related_name="shipping_address")