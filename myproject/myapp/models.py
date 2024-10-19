from django.db import models

class Address(models.Model):
    s_no = models.AutoField(primary_key=True)  # Auto-incrementing serial number
    region = models.CharField(max_length=100)  # Region name
    categories = models.CharField(max_length=100)  # Categories of addresses
    postal_dtdc = models.CharField(max_length=50)  # Postal or DTDC number
    person_name = models.CharField(max_length=100)  # Name of the person
    company_name = models.CharField(max_length=100)  # Company name
    address = models.TextField()  # Full address
    phone_number = models.CharField(max_length=15)  # Phone number
    copies = models.PositiveIntegerField()  # Number of copies
    receiver_name = models.CharField(max_length=100)  # Name of the receiver
    email_id = models.EmailField()  # Email ID


class ReturnAddress(models.Model):
    return_address = models.CharField(max_length=255)
    correct_address = models.CharField(max_length=255)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('verified', 'Verified'),
        ('not_verified', 'Not Verified'),
        ('rejected', 'Rejected'),
    ])

    def __str__(self):
        return self.return_address


    def __str__(self):
        return f"{self.person_name} - {self.company_name}"
    


