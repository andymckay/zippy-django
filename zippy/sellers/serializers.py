from rest_framework.serializers import ModelSerializer

from zippy.sellers.models import Seller


class SellerSerializer(ModelSerializer):

    class Meta:
       model = Seller
