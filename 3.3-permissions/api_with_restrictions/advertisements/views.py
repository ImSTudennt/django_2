from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from django_filters.rest_framework import DjangoFilterBackend, DateFromToRangeFilter
from advertisements.filters import AdvertisementFilter
from advertisements.permissions import IsOwnerOrReadOnly


class AdvertisementViewSet(ModelViewSet):

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['creator_id']
    filterset_class = AdvertisementFilter
    permission_classes = IsOwnerOrReadOnly

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly(), IsAuthenticated()]
        return []
