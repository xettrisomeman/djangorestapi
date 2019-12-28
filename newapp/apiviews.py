from rest_framework import viewsets

from .serializers import (
    TheorySerializer,
    ScientistSerializer
)

from .models import (
    Theory,
    Scientist
)

class TheoryViewSet(viewsets.ModelViewSet):
    serializer_class = TheorySerializer
    queryset = Theory.objects.all()


class ScientistViewSet(viewsets.ModelViewSet):
    serializer_class = ScientistSerializer
    queryset = Scientist.objects.all()

