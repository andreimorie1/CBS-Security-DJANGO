from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path("dashboard/", views.index, name="index"),
    path("staff/", views.staff, name="staff"),
    path("staff/detail/<int:pk>/", views.staff_details, name="staff_detail"),
    path("product/", views.product, name="product"),
    path("product/delete/<int:pk>", views.product_delete, name="product_delete"),
    path("product/update/<int:pk>", views.product_update, name="product_update"),
    path("order/", views.order, name="order"),
]
