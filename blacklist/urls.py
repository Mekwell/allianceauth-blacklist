# In blacklist/urls.py

from django.urls import path, include
# from django.urls import re_path  # No longer needed, we can use path
from . import views

app_name = 'blacklist'

urlpatterns = [
    # --- API URLS ---
    path('api/', include('blacklist.api_urls')),

    # --- YOUR EXISTING APP URLS (Updated to 'path') ---
    path('set/', views.blacklist_set_search_character, name='set'),
    path('notes/', views.note_board, name='note_board'),
    path('blacklist/', views.blacklist, name='blacklist'),
    path('search_names/', views.search_names, name='search_names'),

    # Modal/Action URLs
    path('get_add_note/<int:eve_id>/', views.get_add_evenote, name='modal_add'),
    path('get_comments/<int:evenote_id>/', views.get_evenote_comments, name='modal_comment'),
    path('get_edit_note/<int:evenote_id>/', views.get_edit_evenote, name='modal_edit'),
    path('get_add_comment/<int:evenote_id>/', views.get_add_comment, name='modal_add_comment'),
    path('add_comment/<int:note_id>/', views.add_comment, name='add_comment'),
    path('add_note/<int:eve_id>/', views.add_note, name='add_note'),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
]