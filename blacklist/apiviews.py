from rest_framework import generics
from .models import EveNote
from .serializers import EveNoteSerializer
from .decorators import public_api_view
from django.utils.decorators import method_decorator

@method_decorator(public_api_view, name='dispatch')
class EveNoteList(generics.ListAPIView):
    queryset = EveNote.objects.filter(blacklisted=True)
    serializer_class = EveNoteSerializer
    authentication_classes = []  # No authentication required
    permission_classes = []  # No permissions required

@method_decorator(public_api_view, name='dispatch')
class EveNoteRetrieve(generics.RetrieveAPIView):
    queryset = EveNote.objects.filter(blacklisted=True)
    serializer_class = EveNoteSerializer
    authentication_classes = []  # No authentication required
    permission_classes = []  # No permissions required
    lookup_field = 'eve_id'
