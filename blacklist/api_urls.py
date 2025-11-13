from django.urls import path, include
from . import apiviews

app_name = 'blacklist_api'

urlpatterns = [
    path('', apiviews.EveNoteList.as_view(), name='note_list'),
    path('<int:eve_id>/', apiviews.EveNoteRetrieve.as_view(), name='note_retrieve'),
]
