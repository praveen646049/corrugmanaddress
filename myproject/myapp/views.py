from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from .models import Address
from .models import ReturnAddress
from django.contrib import messages
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from docx import Document
from django.db.models import Q
import pandas as pd
from django.contrib.auth.models import User 
import time
from django.contrib.auth import login
from django.db import OperationalError
import logging
import html 



# def pdf_address_list(request):
#     addresses = Address.objects.all()  # Fetch all addresses
#     context = {
#         'addresses': addresses,
#     }
#     pdf = render_to_pdf('addresses/pdf_address_list.html', context)  # Render PDF
#     return HttpResponse(pdf, content_type='application/pdf')  # Return PDF response


# def print_address_list(request):
#     addresses = Address.objects.all()  # Fetch all addresses or apply filters as needed
#     template_path = 'addresses/print_address_list.html'  # Adjust to your template path
#     context = {'addresses': addresses}
    
#     # Render the template
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="address_list.pdf"'
    
#     # Create PDF
#     template = render(request, template_path, context)
#     pisa_status = pisa.CreatePDF(template, dest=response)
    
#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html.escape(pisa_status.err) + '</pre>')
    
#     return response

# def download_pdf(request):
#     # Get selected addresses from the form
#     selected_ids = request.POST.getlist('selected_addresses')
    
#     if not selected_ids:
#         return HttpResponse('No addresses selected to download.')
    
#     # Fetch the selected addresses
#     addresses = Address.objects.filter(pk__in=selected_ids)

#     # Create PDF response
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="address_list.pdf"'

#     # Render the PDF
#     template_path = 'addresses/print_address_list.html'  # Adjust the path to your template
#     template = render(request, template_path, {'addresses': addresses})
    
#     pisa_status = pisa.CreatePDF(template.content, dest=response)

#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html.escape(pisa_status.err) + '</pre>')
#     return response



# def download_address_list_word(request):
#     addresses = Address.objects.all()  # Fetch all addresses
#     document = Document()
#     document.add_heading('Address List', level=1)

#     for address in addresses:
#         document.add_paragraph(f'S.No: {addresses.index(address) + 1}')
#         document.add_paragraph(f'Person Name: {address.person_name}')
#         document.add_paragraph(f'Company Name: {address.company_name}')
#         document.add_paragraph(f'Address: {address.address}')
#         document.add_paragraph(f'Phone Number: {address.phone_number}')
#         document.add_paragraph('')  # Add a blank line between addresses

#     response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
#     response['Content-Disposition'] = 'attachment; filename="address_list.docx"'
#     document.save(response)
#     return response

# 

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        is_admin = request.POST.get('is_admin') == 'True'

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif password != password_confirm:
            messages.error(request, "Passwords do not match.")
        else:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.is_staff = is_admin
                user.save()
                messages.success(request, 'Registration successful! You can now log in.')
                login(request, user)  # Automatically log in the user after registration
                return redirect('address_list')  # Redirect to the address list
            except Exception as e:
                messages.error(request, str(e))

    return render(request, 'registration/register.html')

# @login_required
# def address_list(request):
#     addresses = Address.objects.all()
#     is_admin = request.user.is_staff  # Assuming 'is_staff' indicates admin

#     return render(request, 'addresses/address_list.html', {
#         'addresses': addresses,
#         'is_admin': is_admin,
#     })




def download_pdf(request):
    selected_ids = request.POST.getlist('selected_addresses')

    if not selected_ids:
        return HttpResponse('No addresses selected to download.')

    addresses = Address.objects.filter(pk__in=selected_ids)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="address_list.pdf"'

    # Create PDF logic
    template_path = 'addresses/print_address_list.html'  # Adjust as necessary
    context = {'addresses': addresses}
    template = render(request, template_path, context)
    pisa_status = pisa.CreatePDF(template, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html.escape(pisa_status.err) + '</pre>')

    return response

def download_word(request):
    # Get selected addresses from the form
    selected_ids = request.POST.getlist('selected_addresses')

    if not selected_ids:
        return HttpResponse('No addresses selected to download.')

    # If no specific addresses are selected, fetch all addresses
    addresses = Address.objects.all() if selected_ids == ['all'] else Address.objects.filter(pk__in=selected_ids)

    # Create a Word document
    doc = Document()
    doc.add_heading('Address List', level=1)

    # Add a table to the document
    table = doc.add_table(rows=1, cols=2)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'S.No'
    hdr_cells[1].text = 'Details'

    for address in addresses:
        row_cells = table.add_row().cells
        row_cells[0].text = str(address.s_no)
        details = (
            f"{address.person_name}\n"
            f"{address.company_name}\n"
            f"{address.address}\n"
            f"{address.phone_number}\n"
        )
        row_cells[1].text = details

    # Response setup
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename="address_list.docx"'
    doc.save(response)

    return response


def welcome(request):
    return render(request, 'welcome.html')

def is_admin(user):
    return user.is_admin


def print_address_list(request):
    addresses = Address.objects.all()  # Fetch all addresses
    return render(request, 'addresses/print_address_list.html', {'addresses': addresses})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Retry logic for database access
        for _ in range(5):  # Retry up to 5 times
            try:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('address_list')  # Redirect to address list after login
                else:
                    return render(request, 'registration/login.html', {'error': 'Invalid username or password'})
            except OperationalError:
                time.sleep(1)  # Wait a second before retrying
    return render(request, 'registration/login.html')

# @login_required
# def address_list(request):
#     addresses = Address.objects.all()
#     return render(request, 'addresses/address_list.html', {'addresses': addresses})

##################################

@login_required
def address_list(request):
    search_query = request.GET.get('search', '')
    search_field = request.GET.get('field', '')

    addresses = Address.objects.all()

    if search_query and search_field:
        # Use icontains for case-insensitive partial matching
        filter_kwargs = {f"{search_field}__icontains": search_query}
        addresses = addresses.filter(**filter_kwargs)

    return render(request, 'addresses/address_list.html', {
        'addresses': addresses,
        'request': request,
    })

@login_required
def return_address_list(request):
    return_addresses = ReturnAddress.objects.all()  # Adjust as necessary

    return render(request, 'addresses/return_address_list.html', {
        'return_addresses': return_addresses,
    })

@login_required
def create_return_address(request):
    if request.method == 'POST':
        return_address = request.POST.get('return_address')
        correct_address = request.POST.get('correct_address')
        reason = request.POST.get('reason')

        # Create a new return address instance and save it
        ReturnAddress.objects.create(
            return_address=return_address,
            correct_address=correct_address,
            reason=reason
        )
        return redirect('return_address_list')  # Redirect to the return address list after creation

    # Handle GET request by rendering the form template
    return render(request, 'addresses/create_return_address.html') 
# @login_required
# def address_create(request):
#     if request.method == 'POST':
#         address = Address(
#             region=request.POST.get('region'),
#             categories=request.POST.get('categories'),
#             postal_dtdc=request.POST.get('postal_dtdc'),
#             person_name=request.POST.get('person_name'),
#             company_name=request.POST.get('company_name'),
#             address=request.POST.get('address'),
#             phone_number=request.POST.get('phone_number'),
#             copies=request.POST.get('copies'),
#             receiver_name=request.POST.get('receiver_name'),
#             email_id=request.POST.get('email_id'),
#         )
#         address.save()
#         return redirect('address_list')
#     return render(request, 'addresses/address_form.html')

# @login_required
# def address_list(request):
#     addresses = Address.objects.all()
    
#     # Handle search query
#     search_query = request.GET.get('search', '')
#     if search_query:
#         addresses = addresses.filter(
#             Q(region__icontains=search_query) |
#             Q(categories__icontains=search_query) |
#             Q(company_name__icontains=search_query) |
#             Q(person_name__icontains=search_query) |
#             Q(address__icontains=search_query) |
#             Q(email_id__icontains=search_query)
#         )
    
#     # Pagination
#     paginator = Paginator(addresses, 10)  # Show 10 addresses per page
#     page_number = request.GET.get('page')
#     addresses = paginator.get_page(page_number)
#     is_admin = request.user.is_staff

#     return render(request, 'addresses/address_list.html', {
#         'addresses': addresses,
#         'is_admin': is_admin,
#     })

# @login_required
# def address_update(request):
#     address = get_object_or_404(Address)
#     if request.method == 'POST':
#         address.region = request.POST.get('region')
#         address.categories = request.POST.get('categories')
#         address.postal_dtdc = request.POST.get('postal_dtdc')
#         address.person_name = request.POST.get('person_name')
#         address.company_name = request.POST.get('company_name')
#         address.address = request.POST.get('address')
#         address.phone_number = request.POST.get('phone_number')
#         address.copies = request.POST.get('copies')
#         address.receiver_name = request.POST.get('receiver_name')
#         address.email_id = request.POST.get('email_id')
#         address.save()
#         return redirect('address_list')
#     return render(request, 'addresses/address_form.html', {'address': address})

# def address_list(request):
#     search_query = request.GET.get('search', '')
#     field = request.GET.get('field', 's_no')  # Default sort field

#     addresses = Address.objects.all()

#     if search_query:
#         addresses = addresses.filter(
#             # Update based on the fields you want to search
#             Q(return_address__icontains=search_query) | 
#             Q(correct_address__icontains=search_query) | 
#             Q(reason__icontains=search_query)
#         )

#     paginator = Paginator(addresses, 10)  # Show 10 addresses per page
#     page_number = request.GET.get('page')
#     addresses = paginator.get_page(page_number)

#     context = {
#         'addresses': addresses,
#         'request': request,
#     }
#     return render(request, 'address_list.html', context)


def address_update(request, pk):
    address = get_object_or_404(Address, pk=pk)

    if request.method == 'POST':
        # Update the address fields directly from POST data
        address.region = request.POST.get('region', address.region)
        address.categories = request.POST.get('categories', address.categories)
        address.postal_dtdc = request.POST.get('postal_dtdc', address.postal_dtdc)
        address.person_name = request.POST.get('person_name', address.person_name)
        address.company_name = request.POST.get('company_name', address.company_name)
        address.address = request.POST.get('address', address.address)
        address.phone_number = request.POST.get('phone_number', address.phone_number)
        address.copies = request.POST.get('copies', address.copies)
        address.receiver_name = request.POST.get('receiver_name', address.receiver_name)
        address.email_id = request.POST.get('email_id', address.email_id)
        
        address.save()  # Save the updated address
        messages.success(request, "Address updated successfully.")
        return redirect('address_list')  # Adjust to your actual address list view

    return render(request, 'addresses/update_form.html', {'address': address})

# @login_required
# # @user_passes_test(is_admin)
# def address_delete(request, pk):
#     address = get_object_or_404(Address, pk=pk)
#     address.delete()
#     return redirect('address_list')


def address_delete(request, pk):
    address = get_object_or_404(Address, pk=pk)

    if request.method == 'POST':
        address.delete()
        messages.success(request, "Address deleted successfully.")
        return redirect('address_list')  # Adjust to your actual address list view

    return render(request, 'addresses/confirm_delete.html', {'address': address})

@login_required
def import_addresses(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('file')
        if excel_file:
            # Check if the uploaded file is an Excel file
            if not excel_file.name.endswith(('.xls', '.xlsx')):
                messages.error(request, "Please upload a valid Excel file.")
                return redirect('import_addresses')

            try:
                # Read the Excel file
                df = pd.read_excel(excel_file)

                # Initialize counters for imported and updated addresses
                imported_count = 0
                updated_count = 0

                # Loop through the rows in the DataFrame
                for index, row in df.iterrows():
                    # Check for duplicates based on the address field
                    existing_address = Address.objects.filter(address=row['address']).first()

                    if existing_address:
                        # Update existing record with new data
                        existing_address.region = row['region']
                        existing_address.categories = row['categories']
                        existing_address.postal_dtdc = row['postal_dtdc']
                        existing_address.person_name = row['person_name']
                        existing_address.company_name = row['company_name']
                        existing_address.phone_number = row['phone_number']
                        existing_address.copies = row['copies']
                        existing_address.receiver_name = row['receiver_name']
                        existing_address.email_id = row['email_id']
                        existing_address.save()
                        updated_count += 1
                    else:
                        # Create a new Address object
                        Address.objects.create(
                            region=row['region'],
                            categories=row['categories'],
                            postal_dtdc=row['postal_dtdc'],
                            person_name=row['person_name'],
                            company_name=row['company_name'],
                            address=row['address'],
                            phone_number=row['phone_number'],
                            copies=row['copies'],
                            receiver_name=row['receiver_name'],
                            email_id=row['email_id'],
                        )
                        imported_count += 1

                # Provide user feedback about the import process
                messages.success(request, f"Imported {imported_count} new addresses and updated {updated_count} existing addresses.")
                return redirect('address_list')  # Redirect to address list after import

            except Exception as e:
                messages.error(request, "Error reading the Excel file. Please check the file format.")
                return redirect('import_addresses')

    return render(request, 'addresses/import_form.html')

@login_required
def address_create(request):
    if request.method == 'POST':
        # Extract data from the form
        address_data = {
            'region': request.POST.get('region'),
            'categories': request.POST.get('categories'),
            'postal_dtdc': request.POST.get('postal_dtdc'),
            'person_name': request.POST.get('person_name'),
            'company_name': request.POST.get('company_name'),
            'address': request.POST.get('address'),
            'phone_number': request.POST.get('phone_number'),
            'copies': request.POST.get('copies'),
            'receiver_name': request.POST.get('receiver_name'),
            'email_id': request.POST.get('email_id'),
        }

        # Check if the address already exists
        if Address.objects.filter(address=address_data['address']).exists():
            messages.error(request, "This address already exists. Please enter a new address.")
            return render(request, 'addresses/address_form.html', {'data': address_data})

        # If the address does not exist, create a new one
        Address.objects.create(**address_data)
        messages.success(request, "Address created successfully.")
        return redirect('address_list')

    return render(request, 'addresses/address_form.html')

# @login_required
# def import_addresses(request):
#     if request.method == 'POST':
#         excel_file = request.FILES.get('file')
#         if excel_file:
#             # Check if the uploaded file is an Excel file
#             if not excel_file.name.endswith(('.xls', '.xlsx')):
#                 messages.error(request, "Please upload a valid Excel file.")
#                 return redirect('import_addresses')

#             try:
#                 # Read the Excel file
#                 df = pd.read_excel(excel_file)

#                 # Initialize counters for imported and duplicate addresses
#                 success_count = 0
#                 duplicate_count = 0

#                 # Loop through the rows in the DataFrame
#                 for index, row in df.iterrows():
#                     # Check for duplicates based on multiple fields
#                     existing_address = Address.objects.filter(
#                         region=row['region'],
#                         categories=row['categories'],
#                         address=row['address'],
#                         phone_number=row['phone_number']  # Include other fields as needed
#                     ).first()

#                     if not existing_address:
#                         try:
#                             # Create a new Address object
#                             Address.objects.create(
#                                 region=row['region'],
#                                 categories=row['categories'],
#                                 postal_dtdc=row['postal_dtdc'],
#                                 person_name=row['person_name'],
#                                 company_name=row['company_name'],
#                                 address=row['address'],
#                                 phone_number=row['phone_number'],
#                                 copies=row['copies'],
#                                 receiver_name=row['receiver_name'],
#                                 email_id=row['email_id'],
#                             )
#                             success_count += 1
#                         except Exception as e:
#                             # Log the error or handle it as needed
#                             continue
#                     else:
#                         duplicate_count += 1

#                 # Provide user feedback about the import process
#                 messages.success(request, f"Imported {success_count} addresses successfully. {duplicate_count} duplicates were skipped.")
#                 return redirect('address_list')  # Redirect to address list after import

#             except Exception as e:
#                 messages.error(request, "Error reading the Excel file. Please check the file format.")
#                 return redirect('import_addresses')

#     return render(request, 'addresses/import_form.html')


# @login_required
# @user_passes_test(is_admin)
# @login_required
# def import_addresses(request):
#     if request.method == 'POST':
#         excel_file = request.FILES.get('file')
#         if excel_file:
#             # Check if the uploaded file is an Excel file
#             if not excel_file.name.endswith(('.xls', '.xlsx')):
#                 messages.error(request, "Please upload a valid Excel file.")
#                 return redirect('import_addresses')

#             try:
#                 # Read the Excel file
#                 df = pd.read_excel(excel_file)

#                 # Initialize counters for imported and duplicate addresses
#                 success_count = 0
#                 duplicate_count = 0

#                 # Loop through the rows in the DataFrame
#                 for index, row in df.iterrows():
#                     address_value = row['address']
#                     # Check if the address already exists
#                     if not Address.objects.filter(address=address_value).exists():
#                         try:
#                             # Create a new Address object
#                             Address.objects.create(
#                                 region=row['region'],
#                                 categories=row['categories'],
#                                 postal_dtdc=row['postal_dtdc'],
#                                 person_name=row['person_name'],
#                                 company_name=row['company_name'],
#                                 address=address_value,
#                                 phone_number=row['phone_number'],
#                                 copies=row['copies'],
#                                 receiver_name=row['receiver_name'],
#                                 email_id=row['email_id'],
#                             )
#                             success_count += 1
#                         except Exception as e:
#                             # Log the error or handle it as needed
#                             continue
#                     else:
#                         duplicate_count += 1

#                 # Provide user feedback about the import process
#                 messages.success(request, f"Imported {success_count} addresses successfully. {duplicate_count} duplicates were skipped.")
#                 return redirect('address_list')  # Redirect to address list after import

#             except Exception as e:
#                 messages.error(request, "Error reading the Excel file. Please check the file format.")
#                 return redirect('import_addresses')

#     return render(request, 'addresses/import_form.html')
# def import_addresses(request):
#     if request.method == 'POST':
#         excel_file = request.FILES.get('file')
#         if excel_file:
#             # Read the Excel file
#             df = pd.read_excel(excel_file)

#             # Loop through the rows and create Address objects
#             for index, row in df.iterrows():
#                 Address.objects.create(
#                     region=row['region'],
#                     categories=row['categories'],
#                     postal_dtdc=row['postal_dtdc'],
#                     person_name=row['person_name'],
#                     company_name=row['company_name'],
#                     address=row['address'],
#                     phone_number=row['phone_number'],
#                     copies=row['copies'],
#                     receiver_name=row['receiver_name'],
#                     email_id=row['email_id'],
#                 )
#             return redirect('address_list')  # Redirect to address list after import

#     return render(request, 'addresses/import_form.html')
