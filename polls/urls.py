from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('list/', views.polls_list, name='polls_list'),
    path('<int:poll_id>/', views.polls_detail, name='detail'),
    path('<int:poll_id>/poll_vote/', views.poll_vote, name='poll_vote'),
]
