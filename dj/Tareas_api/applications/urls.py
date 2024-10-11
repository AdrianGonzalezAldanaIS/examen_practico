from django.urls import path, include
from rest_framework import routers
from applications.Tareas import views

router= routers.DefaultRouter()
router.register(r'tareas', views.TareaViewSet)

urlpatterns = [
    path('', include(router.urls))
]










