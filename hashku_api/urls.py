from django.conf.urls import url
from hashku_api import views

urlpatterns = (
    url(r'^go$', views.thingy),
)
