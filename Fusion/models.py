from django.core.validators import RegexValidator
from django.db import models
from django.db.models import *


class VendorRegistraion(models.Model):
    name = CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    email = EmailField()
    name_of_business = CharField(max_length=50)
    org_choices = (
        ('a', 'Sole Proprietorship'),
        ('b', 'Partnership'),
        ('c', 'C Corporation'),
        ('d', 'S Corporation'),
        ('e', 'LLC (Limited Liability Company'),
        ('f', 'Nonprofit'),
    )

    type_of_legal_organization = CharField(choices=org_choices, max_length=1)

    FEIN_regex = RegexValidator(regex=r'^\d{9}$', message="FEIN Code must be 9 digits")
    FEIN_code = models.CharField(validators=[FEIN_regex], max_length=9, blank=True)

    NAICS_regex = RegexValidator(regex=r'^\d{6}$', message="NAICS Code must be 6 digits")
    NAICS_code = models.CharField(validators=[NAICS_regex], max_length=6, blank=True)

    industry_choices = (
        ('a', 'Consumer Goods'),
        ('b', 'Financials'),
        ('c', 'Food & Beverage'),
        ('d', 'Healthcare'),
        ('e', 'Infrastructure'),
        ('f', 'Renewable Resources & Alternative Energy'),
        ('g', 'Resource Transformation'),
        ('h', 'Service'),
        ('i', 'Technology & Communications'),
        ('j', 'Transportation'),
        ('k', 'Other'),
    )
    industry_type = CharField(choices=industry_choices, max_length=1)

    mailing_address = CharField(max_length=50)
    physical_location = CharField(max_length=50)
    short_business_description = CharField(max_length=300)
    chief_compliance_officer = BooleanField()
    chief_compliance_officer_name = CharField(max_length=50)
    chief_compliance_officer_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    chief_compliance_officer_email = EmailField()

    certificate_choices = (
        ('0', 'None'),
        ('a', 'ISO 14001:2015'),
        ('b', 'ISO 14002-1:2019'),
        ('c', 'ISO 14004:2016'),
        ('d', 'ISO 14005:2019'),
        ('e', 'ISO 14006:2020'),
        ('f', 'ISO 14007:2019'),
        ('g', 'ISO 14008:2019'),
        ('h', 'ISO 14009:2020'),
        ('i', 'Other'),
    )
    certificate = CharField(choices=certificate_choices, max_length=1)
    willing_to_obtain_certificate = CharField(max_length=3)
    follow_26000 = CharField(max_length=3)
    CBCE = CharField(max_length=3)
    follow_37000 = CharField(max_length=3)
    CGC = CharField(max_length=3)




    def __str__(self):
        return self.title

