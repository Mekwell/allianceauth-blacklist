from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .models import EveNote
from .serializers import EveNoteSerializer

class EveNoteList(generics.ListAPIView):
    queryset = EveNote.objects.filter(blacklisted=True)
    serializer_class = EveNoteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = []  # No permissions required, only a valid token

class EveNoteRetrieve(generics.RetrieveAPIView):
    queryset = EveNote.objects.filter(blacklisted=True)
    serializer_class = EveNoteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = []  # No permissions required, only a valid token
    lookup_field = 'eve_id'
