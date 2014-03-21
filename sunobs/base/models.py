from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import (BaseUserManager,
                                        AbstractBaseUser, PermissionsMixin)


class SunUserManager(BaseUserManager):
    def create_user(self, email, displayname, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=SunUserManager.normalize_email(email),
        )

        user.set_password(password)
        user.displayname = displayname
        user.save(using=self._db)
        return user

    def create_superuser(self, email, displayname, password):
        user = self.create_user(email, displayname,
                                password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class SunUser(AbstractBaseUser, PermissionsMixin):
    GROUP_NAMES = (
        ('Observer', 'Observer'),
        ('Analyst', 'Analyst'),
        ('Admin', 'Admin'),
    )
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    aavsocode = models.CharField(max_length=4, blank=True)
    displayname = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=40, blank=True)
    postal = models.IntegerField(max_length=5, null=True)
    country = models.CharField(max_length=40, blank=True)
    landline = models.CharField(max_length=14, blank=True)
    mobile = models.CharField(max_length=14, blank=True)
    group = models.CharField(max_length=8, choices=GROUP_NAMES,
                              default='Observer')
    valid = models.BooleanField(default=True)
    first_login = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['displayname']

    objects = SunUserManager()

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def email_user(self, subject, message, from_email=None, **kwargs):
        # Sends an email to this user
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_staff(self):
        # Make sure only admins can login to /admin/
        return self.is_admin


class Equipment(models.Model):
    METHODS = (
        ('Projection', 'Projection'),
        ('Direct', 'Direct'),
        ('Drawing', 'Drawing'),
        ('Photo', 'Photo'),
        ('Visual', 'Visual'),
    )
    INSTRUMENTS = (
        ('Reflector', 'Reflector'),
        ('Refractor', 'Refractor'),
        ('SCT', 'SCT'),
        ('Maksutov', 'SCT/Maksutov'),
    )
    FOCAL_TYPES = (
        ('MM', 'MM (milimeters)'),
        ('D', 'D (diameter)'),
    )
    name = models.CharField(max_length=50)
    method = models.CharField(max_length=10, choices=METHODS)
    instrument = models.CharField(max_length=9, choices=INSTRUMENTS)
    aperture = models.DecimalField(max_digits=2, decimal_places=2)
    eyepiece = models.DecimalField(max_digits=2, decimal_places=2)
    magnification = models.IntegerField(max_length=3)
    focal_length = models.IntegerField(max_length=3)
    focal_length_type = models.CharField(max_length=2, choices=FOCAL_TYPES)
    filtr = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey('SunUser')
