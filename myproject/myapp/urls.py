from django.urls import path
from .views import (
    welcome, backup_option, custom_login, address_list, address_create, address_update, address_delete, 
    import_addresses, print_address_list, register, download_pdf, download_word,
    return_address_list, return_create_address, return_edit_address, return_delete_address,
    monthly_copies_summary, professional_list, professional_create, professional_update, professional_delete,
    classified_list, classified_create, classified_update, classified_delete,create_monthly_copies_summary,
    expert_list, expert_create, expert_update, expert_delete,edit_monthly_copies_summary, delete_monthly_copies_summary,
    customer_list, customer_create, customer_update, customer_delete, return_address_history, create_address_history,
    interview_list, interview_create, interview_update, interview_delete, magazine_details # Import the new views
)

urlpatterns = [
    path('', welcome, name='welcome'),  # Welcome page
    path('backup_option/', backup_option, name='backup_option'),
    path('address/history/', return_address_history, name='return_address_history'),
     path('address/history/create/', create_address_history, name='create_address_history'),

    path('login/', custom_login, name='login'),  # Custom login view
    path('address_list/', address_list, name='address_list'),  # Address list view
    path('create/', address_create, name='address_create'),  # Create address
    path('update/<int:pk>/', address_update, name='address_update'),  # Update address
    path('delete/<int:pk>/', address_delete, name='address_delete'),  # Delete address
    path('import/', import_addresses, name='import_form'),  # Import addresses
    path('print/', print_address_list, name='print_address_list'),  # Print address list
    path('download_pdf/', download_pdf, name='download_pdf'),  # Download address list as PDF
    path('download_word/', download_word, name='download_word'),  # Download address list as Word document
    path('register/', register, name='register'),  # Register user

    # Return address-related views
    path('return/', return_address_list, name='return_address_list'),  # List of return addresses
    path('return/create/', return_create_address, name='return_create_address'),  # Form to create a new return address
    path('return/edit/<int:pk>/', return_edit_address, name='return_edit_address'),  # Form to edit a return address
    path('return/delete/<int:pk>/', return_delete_address, name='return_delete_address'),  # Deletes a return address


    path('monthly-copies-summary/', monthly_copies_summary, name='monthly_copies_summary'),
    path('monthly-copies-summary/create/', create_monthly_copies_summary, name='create_monthly_copies_summary'),
    path('monthly-copies-summary/edit/<int:id>/', edit_monthly_copies_summary, name='edit_monthly_copies_summary'),
    path('monthly-copies-summary/delete/<int:id>/', delete_monthly_copies_summary, name='delete_monthly_copies_summary'),


   

    # Professional URLs
    path('professionals/', professional_list, name='professional_list'),
    path('professionals/create/', professional_create, name='professional_create'),
    path('professionals/update/<int:pk>/', professional_update, name='professional_update'),
    path('professionals/delete/<int:pk>/', professional_delete, name='professional_delete'),

    # Classified URLs
    path('classifieds/', classified_list, name='classified_list'),
    path('classifieds/create/', classified_create, name='classified_create'),
    path('classifieds/update/<int:pk>/', classified_update, name='classified_update'),
    path('classifieds/delete/<int:pk>/', classified_delete, name='classified_delete'),

    # Expert URLs
    path('experts/', expert_list, name='expert_list'),
    path('experts/create/', expert_create, name='expert_create'),
    path('experts/update/<int:pk>/', expert_update, name='expert_update'),
    path('experts/delete/<int:pk>/', expert_delete, name='expert_delete'),

    # Customer URLs
    path('customers/', customer_list, name='customer_list'),
    path('customers/create/', customer_create, name='customer_create'),
    path('customers/update/<int:pk>/', customer_update, name='customer_update'),
    path('customers/delete/<int:pk>/', customer_delete, name='customer_delete'),

    # Interview URLs
    path('interviews/', interview_list, name='interview_list'),
    path('interviews/create/', interview_create, name='interview_create'),
    path('interviews/update/<int:pk>/', interview_update, name='interview_update'),
    path('interviews/delete/<int:pk>/', interview_delete, name='interview_delete'),

    path('magazines/', magazine_details, name='magazine_details'),
]
