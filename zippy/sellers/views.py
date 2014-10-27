from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from zippy.sellers.models import Seller
from zippy.sellers.serializers import SellerSerializer


class SellerViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Seller.objects.filter()
    serializer_class = SellerSerializer
