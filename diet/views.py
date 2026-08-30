from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import DietEntry
from .serializers import DietEntrySerializer


class DietListCreateView(generics.ListCreateAPIView):
    serializer_class = DietEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DietEntry.objects.filter(
            user=self.request.user
        ).order_by("-consumed_at")

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
class DietDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DietEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DietEntry.objects.filter(
            user=self.request.user
        )