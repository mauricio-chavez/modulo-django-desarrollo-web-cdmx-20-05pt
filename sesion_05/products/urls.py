"""Products app URL config"""

from django.urls import path
from rest_framework import urlpatterns

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'product', views.ProductViewset, basename='product')

urlpatterns = router.urls


# urlpatterns = [
#     path('product', views.ProductList.as_view(), name='products'),
#     path('product/<int:pk>', views.ProductRetrieve.as_view(), name='product'),
# ]
