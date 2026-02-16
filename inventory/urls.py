from django.urls import path
from .views import LoginAPIView
from .views import CategoryListAPIView
from .views import AddProductAPIView, ProductListAPIView
from .views import StorageListAPIView
from .views import ProductImageUploadAPIView
from .views import DepartmentListAPIView
from .views import LocationListAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
     path('categories/', CategoryListAPIView.as_view()),
      path('product/add/', AddProductAPIView.as_view()),
    path('product/list/', ProductListAPIView.as_view()),
    path('storage/list/', StorageListAPIView.as_view()),
    path('product/images/upload/', ProductImageUploadAPIView.as_view()),
     path('departments/', DepartmentListAPIView.as_view()),
     path('locations/', LocationListAPIView.as_view()),
]
