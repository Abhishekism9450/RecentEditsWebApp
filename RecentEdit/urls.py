from django.conf.urls import url
from django.urls import path
# from . import views
from RecentEdit.views import HomeView

urlpatterns= [
    url(r'^$',HomeView.as_view() , name='home'),
        

    ]
