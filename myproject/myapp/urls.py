from django.urls import path
from .views import welcome, custom_login, create_return_address, address_list, address_create, address_update, address_delete, import_addresses, return_address_list, print_address_list, register, download_pdf, download_word
urlpatterns = [
    path('', welcome, name='welcome'),  # Welcome page
    path('login/', custom_login, name='login'),  # Custom login view
    path('address_list/', address_list, name='address_list'),  # Address list view
    path('create/', address_create, name='address_create'),  # Create address
    path('update/<int:pk>/', address_update, name='address_update'),  # Update address
    path('delete/<int:pk>/', address_delete, name='address_delete'),  # Delete address
    path('import/', import_addresses, name='import_form'),  # Import addresses
    path('print/', print_address_list, name='print_address_list'),
    path('download_pdf/', download_pdf, name='download_pdf'),
    path('download_word/', download_word, name='download_word'),
    path('register/', register, name='register'), 
    path('return-addresses/', return_address_list, name='return_address_list'),
    path('create-return-address/', create_return_address, name='create_return_address'),
  ]

