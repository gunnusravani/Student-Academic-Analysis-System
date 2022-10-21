from unicodedata import name
from django.urls import path
from.import views

urlpatterns=[
    
    path('results',views.results,name='results'),
    path('',views.index,name='index'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('update',views.update, name='update'),
    #path('user_results',views.user_results, name='user_results'),
    
]