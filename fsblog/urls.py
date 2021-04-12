from django.urls import include, path
from . import views

urlpatterns = [
   # path("<str:name>",views.index,name = "index"),
    path("",views.home,name = "home"),
    path("create",views.create,name = "create")
]

