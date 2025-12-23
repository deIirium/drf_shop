from django.urls import path

from apps.profiles.views import ProfileView, ShippingAddressesView, ShippingAddressViewID, OrderView, OrderItemsView

urlpatterns = [
    path('', ProfileView.as_view()),
    path('shipping_addresses/', ShippingAddressesView.as_view()),
    path('shipping_addresses/detail/<str:id>/', ShippingAddressViewID.as_view()),
    path('orders/', OrderView.as_view()),
    path('orders/<str:tx_ref/', OrderItemsView.as_view()),

]