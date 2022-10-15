from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ads.premissions import SelectionChangePermissions
from selections.models import Selection
from selections.serializers import (SelectionListSerializer,
                                    SelectionRetrieveSerializer,
                                    SelectionSerializer)


class SelectionListView(generics.ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionListSerializer


class SelectionCreateView(generics.CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated]


class SelectionRetrieveView(generics.RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionRetrieveSerializer


class SelectionUpdateView(generics.UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionChangePermissions]


class SelectionDestroyView(generics.DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated, SelectionChangePermissions]
