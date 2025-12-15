from django.db import models

# Create your models here.

class User(AbstractBaseUser):
    # NEW FOR THE ROLES
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        OWNER = "OWNER", "Owner" 
        CUSTOMER = "CUSTOMER", "Customer"
        
    
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)    
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    company = models.CharField(max_length=250,blank=True,)
    contact_number = models.CharField(max_length=15,unique=True,)
    is_active = models.BooleanField(default=True) 
    is_superuser = models.BooleanField(default=False) # a admin user; non super-user
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.CUSTOMER)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name', 'contact_number','role','company'] # Email & Password are required by default.
    
    
    def get_email(self):
        # The user is identified by their email address
        return self.email 
    
    def __str__(self):
        return self.email
    
    
        
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    