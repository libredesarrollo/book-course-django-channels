from django.urls import path, include
from . import views, api

urlpatterns = path('api/login', api.login),
urlpatterns += path('api/logout', api.logout),
urlpatterns += path('api/alerts', api.alerts),
urlpatterns += path('api/rooms', api.rooms),
urlpatterns += path('dashboard/create', views.create),

