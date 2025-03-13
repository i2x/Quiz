from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [

    #public

    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/reset/', views.reset_votes, name='reset_votes'),  # URL สำหรับ Reset


    #private
    path('private', views.private_index, name='private_index'),
    path('private/<int:question_id>/', views.private_detail, name='private_detail'),
    path('private/<int:question_id>/vote/', views.private_vote, name='private_vote'),
    path('private/<int:question_id>/results/', views.private_results, name='private_results'),
    path('private/<int:question_id>/reset/', views.private_reset_votes, name='private_reset_votes'),  # URL สำหรับ Reset





]
