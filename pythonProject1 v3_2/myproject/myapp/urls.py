from django.urls import path
from . import views
from .views import CreateProduct, UpdateProduct, DeleteProduct

urlpatterns = [
    path('', views.index, name='home'),
    path('products', views.ProductList.as_view(), name='products'),
    path('percents', views.PercentList.as_view(), name='percents'),
    path('profits', views.profit, name='profits'),
    path('createproduct/', CreateProduct.as_view(), name='createproduct'),
    path('updateproduct/<int:pk>/', UpdateProduct.as_view(), name='updateproduct'),
    path('deleteproduct/<int:pk>/', DeleteProduct.as_view(), name='deleteproduct'),

    path('register', views.RegisterList.as_view(), name='register'),
    path('createregister/', views.CreateRegister.as_view(), name='createregister'),
    path('createregistersell/', views.CreateRegisterSell.as_view(), name='createregistersell'),
    path('createpercent/', views.CreatePercent.as_view(), name='createpercent'),

]
