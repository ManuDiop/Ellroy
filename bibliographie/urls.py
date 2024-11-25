from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login_view, name='login'), 
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('livre/<int:livre_id>/', views.detail_livre, name='detail_livre'),
    path('commentaire/<int:commentaire_id>/delete/', views.delete_comment, name='delete_comment'),
]   