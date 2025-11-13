from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from .models import EveNote
from .serializers import EveNoteSerializer

class EveNoteList(generics.ListAPIView):
    queryset = EveNote.objects.filter(blacklisted=True)
    serializer_class = EveNoteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

class EveNoteRetrieve(generics.RetrieveAPIView):
    queryset = EveNote.objects.filter(blacklisted=True)
    serializer_class = EveNoteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    lookup_field = 'eve_id'
