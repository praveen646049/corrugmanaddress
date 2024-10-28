# from django.db import models
# from django.contrib.auth.models import User

# class Address(models.Model):
#     s_no = models.AutoField(primary_key=True)  # This will act as the auto-incrementing primary key
#     region = models.CharField(max_length=100)  # Region name
#     categories = models.CharField(max_length=100)  # Categories of addresses
#     postal_dtdc = models.CharField(max_length=50)  # Postal or DTDC number
#     person_name = models.CharField(max_length=100)  # Name of the person
#     company_name = models.CharField(max_length=100)  # Company name
#     address = models.TextField()  # Full address
#     phone_number = models.CharField(max_length=15)  # Phone number
#     copies = models.IntegerField()  # Number of copies
#     receiver_name = models.CharField(max_length=100)  # Name of the receiver
#     email_id = models.EmailField()  # Email ID

#     def __str__(self):
#         return f"{self.person_name} - {self.company_name}"
    
# class AddressRecord(models.Model):
#     STATUS_CHOICES = [
#         ('verified', 'Verified'),
#         ('not_verified', 'Not Verified'),
#         ('rejected', 'Rejected'),
#     ]

#     s_no = models.IntegerField()
#     return_address = models.CharField(max_length=255)
#     confirm_address = models.CharField(max_length=255)
#     reason = models.TextField()
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_verified')

#     def __str__(self):
#         return f'{self.s_no} - {self.return_address}'
    


# class MonthlyCopiesSummary(models.Model):
#     year = models.IntegerField(default=1)
#     start_month = models.IntegerField(default=1)
#     end_month = models.IntegerField(default=1)  # Set a default value here
#     total_copies = models.IntegerField(default=1)

#     def __str__(self):
#         return f"{self.year} - {self.start_month} to {self.end_month}"
    

# class AddressHistory(models.Model):
#     ACTION_CHOICES = [
#         ('create', 'Create'),
#         ('edit', 'Edit'),
#         ('delete', 'Delete'),
#     ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who made the change
#     action = models.CharField(max_length=10, choices=ACTION_CHOICES)  # Action taken
#     address_record = models.ForeignKey(Address, on_delete=models.CASCADE)  # Related Address
#     timestamp = models.DateTimeField(auto_now_add=True)  # When the action was taken

#     def __str__(self):
#         return f"{self.user.username} - {self.address_record} - {self.action} - {self.timestamp}"

# class AddressRecordHistory(models.Model):
#     ACTION_CHOICES = [
#         ('create', 'Create'),
#         ('edit', 'Edit'),
#         ('delete', 'Delete'),
#     ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who made the change
#     action = models.CharField(max_length=10, choices=ACTION_CHOICES)  # Action taken
#     address_record = models.ForeignKey(AddressRecord, on_delete=models.CASCADE)  # Related AddressRecord
#     timestamp = models.DateTimeField(auto_now_add=True)  # When the action was taken

#     def __str__(self):
#         return f"{self.user.username} - {self.address_record} - {self.action} - {self.timestamp}"

# class MonthlyCopiesSummaryHistory(models.Model):
#     ACTION_CHOICES = [
#         ('create', 'Create'),
#         ('edit', 'Edit'),
#         ('delete', 'Delete'),
#     ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who made the change
#     action = models.CharField(max_length=10, choices=ACTION_CHOICES)  # Action taken
#     summary_record = models.ForeignKey(MonthlyCopiesSummary, on_delete=models.CASCADE)  # Related Summary
#     timestamp = models.DateTimeField(auto_now_add=True)  # When the action was taken

#     def __str__(self):
#         return f"{self.user.username} - {self.summary_record} - {self.action} - {self.timestamp}"

    


# class Professional(models.Model):
#     s_no = models.AutoField(primary_key=True)
#     customer_name = models.CharField(max_length=255)
#     company_name = models.CharField(max_length=255)
#     designation = models.CharField(max_length=255)
#     edition = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.customer_name} - {self.designation}"

# class Classified(models.Model):
#     s_no = models.AutoField(primary_key=True)
#     customer_name = models.CharField(max_length=255)
#     company_name = models.CharField(max_length=255)
#     designation = models.CharField(max_length=255)
#     edition = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.customer_name} - {self.designation}"

# class Expert(models.Model):
#     s_no = models.AutoField(primary_key=True)
#     customer_name = models.CharField(max_length=255)
#     company_name = models.CharField(max_length=255)
#     designation = models.CharField(max_length=255)
#     edition = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.customer_name} - {self.designation}"

# class Customer(models.Model):
#     s_no = models.AutoField(primary_key=True)
#     customer_name = models.CharField(max_length=255)
#     company_name = models.CharField(max_length=255)
#     designation = models.CharField(max_length=255)
#     edition = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.customer_name} - {self.designation}"

# class Interview(models.Model):
#     s_no = models.AutoField(primary_key=True)
#     customer_name = models.CharField(max_length=255)
#     company_name = models.CharField(max_length=255)
#     designation = models.CharField(max_length=255)
#     edition = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.customer_name} - {self.designation}"




from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    s_no = models.AutoField(primary_key=True)
    region = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    postal_dtdc = models.CharField(max_length=50)
    person_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    copies = models.IntegerField(default=1)  # Can remain as IntegerField
    receiver_name = models.CharField(max_length=100)
    email_id = models.EmailField()

    def __str__(self):
        return f"{self.person_name} - {self.company_name}"

class AddressRecord(models.Model):
    STATUS_CHOICES = [
        ('verified', 'Verified'),
        ('not_verified', 'Not Verified'),
        ('rejected', 'Rejected'),
    ]

    s_no = models.AutoField(primary_key=True)
    return_address = models.CharField(max_length=255)
    confirm_address = models.CharField(max_length=255)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_verified')

    def __str__(self):
        return f'{self.s_no} - {self.return_address}'

class MonthlyCopiesSummary(models.Model):
    year = models.IntegerField(default=1)
    start_month = models.IntegerField(default=1)
    end_month = models.IntegerField(default=1)
    total_copies = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.year} - {self.start_month} to {self.end_month}"

class AddressHistory(models.Model):
    ACTION_CHOICES = [
        ('create', 'Create'),
        ('edit', 'Edit'),
        ('delete', 'Delete'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    address_record = models.ForeignKey(Address, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.address_record} - {self.action} - {self.timestamp}"

class AddressRecordHistory(models.Model):
    ACTION_CHOICES = [
        ('create', 'Create'),
        ('edit', 'Edit'),
        ('delete', 'Delete'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    address_record = models.ForeignKey(AddressRecord, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.address_record} - {self.action} - {self.timestamp}"

class MonthlyCopiesSummaryHistory(models.Model):
    ACTION_CHOICES = [
        ('create', 'Create'),
        ('edit', 'Edit'),
        ('delete', 'Delete'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    summary_record = models.ForeignKey(MonthlyCopiesSummary, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.summary_record} - {self.action} - {self.timestamp}"

class Professional(models.Model):
    s_no = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    edition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer_name} - {self.designation}"

class Classified(models.Model):
    s_no = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    edition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer_name} - {self.designation}"

class Expert(models.Model):
    s_no = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    edition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer_name} - {self.designation}"

class Customer(models.Model):
    s_no = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    edition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer_name} - {self.designation}"

class Interview(models.Model):
    s_no = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    edition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.customer_name} - {self.designation}"
