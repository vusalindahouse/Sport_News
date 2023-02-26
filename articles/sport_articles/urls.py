from django.urls import path

from .views import  TennisPage, HockeyPage, FootballPage, MainPage, BoxPage, BiatlonPage, BasketbolPage, AutoPage, VolleybalPage
from . import views
urlpatterns = [
    path('', MainPage.as_view(), name='base'),
    path('football/', FootballPage.as_view(), name='football'),
    path('hockey/', HockeyPage.as_view(), name='hockey'),
    path('tennis/', TennisPage.as_view(), name='tennis'),
    path('basketbol', BasketbolPage.as_view(), name='basketbol'),
    path('volleyball', VolleybalPage.as_view(), name='volleyball'),
    path('auto', AutoPage.as_view(), name='auto'),
    path('box/', BoxPage.as_view(), name='box'),
    path('biatlone/', BiatlonPage.as_view(), name='biatlone'),
    #path('search/', Search.as_view(), name='search')
    path('search/', views.searchBar, name='search'),
    path('login', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.log_out, name='logout'),

]