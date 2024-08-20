from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('product/new/', views.ProductView.as_view(), name='product-new'),
    path('service/support/', views.ServiceView.as_view(), name='service-support'),
    path('info/project-info/', views.InfoView.as_view(), name='info'),
]