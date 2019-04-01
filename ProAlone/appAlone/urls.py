from django.conf.urls import url
from appAlone import views

urlpatterns = [
    url(r'^$',views.users,name='users'),
]
