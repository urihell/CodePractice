from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Organization(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    # email = models.EmailField("E-mail", blank=False, unique=True, default=None)
    # phone = PhoneNumberField(null=False, blank=False, unique=True, default=None)
    # street1 = models.CharField("Street 1", max_length=200, default=None)
    # street2 = models.CharField("Street 2", max_length=200, default=None)
    # city = models.CharField("City", max_length=200, default=None)
    # postal_code = models.CharField("Postal Code", max_length=5, default=None)
    # state = models.CharField("State", max_length=2, default=None)
    # country = models.CharField("Country", max_length=200, default=None)

    def __str__(self):
        return 'Organization Name: %s' % self.name


class Customer(models.Model):
    # first_name = models.CharField(max_length=200, default=None)
    # last_name = models.CharField(max_length=200, default=None)
    email = models.EmailField("E-mail", blank=False, unique=True)
    created_at = models.DateTimeField()
    # phone = PhoneNumberField(null=False, blank=False, unique=True, default=None)
    # street1 = models.CharField("Street 1", max_length=200, default=None)
    # street2 = models.CharField("Street 2", max_length=200, default=None)
    # city = models.CharField("City", max_length=200, default=None)
    # postal_code = models.CharField("Postal Code", max_length=5, default=None)
    # state = models.CharField("State", max_length=2, default=None)
    # country = models.CharField("Country", max_length=200, default=None)

    def __str__(self):
        # return 'Customer Name: %s %s' % (self.first_name, self.last_name)
        return 'Customer Email: %s' % self.email


class Job(models.Model):
    title = models.CharField(max_length=200)
    # description = models.CharField(max_length=200, default=None)
    # customer_first_name = Customer.first_name
    # customer_last_name = Customer.last_name
    # customer_email = Customer.email
    # customer_street1 = Customer.street1
    # customer_street2 = Customer.street2
    # customer_city = Customer.city
    # customer_postal_code = Customer.postal_code
    # customer_state = Customer.state
    # customer_country = Customer.country
    # org_name = Organization.name

    def __str__(self):
        return 'Job Title: %s' % self.title

