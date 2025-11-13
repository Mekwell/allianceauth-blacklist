from rest_framework import generics
from .models import EveNote
from .serializers import EveNoteSerializer

class EveNoteList(generics.ListAPIView):
    queryset = EveNote.objects.filter(blacklisted=True)
    serializer_class = EveNoteSerializer
    authentication_classes = []  # No authentication required
    permission_classes = []  # No permissions required

class EveNoteRetrieve(generics.RetrieveAPIView):
    queryset = EveNote.objects.filter(blacklisted=True)
    serializer_class = EveNoteSerializer
    authentication_classes = []  # No authentication required
    permission_classes = []  # No permissions required
    lookup_field = 'eve_id'
