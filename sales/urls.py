from django.urls import path, include
from rest_framework import routers
from sales import views

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet, 'customers')
router.register(r'products', views.ProductViewSet)
router.register(r'sales', views.SaleHeaderViewSet)
urlpatterns = [
    path("", include(router.urls)),
   
]