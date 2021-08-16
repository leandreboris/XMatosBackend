from django.db import models

# Create your models here.


from phonenumber_field import modelfields
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Handling Users Accounts
class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None, first_name=None, last_name=None, last_ip=None, avatar=None, *args, **kwargs):    
        if not username :
            raise ValueError("Users must have an username")
        
        

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            last_ip = last_ip,
            avatar = avatar,
        )      

        user.set_password (password)
        user.save(using=self._db) 
        return user 

    def create_provider(self, email, username, password, cin, adresse, telephone, first_name=None, last_name=None, last_ip=None, avatar=None, *args, **kwargs):
        if not cin :
            raise ValueError("Providers must have a cin")
        if not adresse :
            raise ValueError("Providers must have an adresse")
        if not telephone :
            raise ValueError("Providers must have a telephone")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            cin = cin,
            adresse = adresse, 
            telephone = telephone,
            first_name = first_name,
            last_name = last_name,
            last_ip = last_ip,
            avatar = avatar,
        )

        user.set_password (password)
        user.is_staff = True
        user.is_fournisseur = True

        user.save(using=self._db)

        return user



    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.is_provider = True

        user.save(using=self._db)

        return user


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 



# User model 
class User(AbstractBaseUser):

    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    adresse = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=60, unique=True)
    avatar = models.ImageField(null=True, blank=True)
    telephone = modelfields.PhoneNumberField()
    cin = models.CharField(max_length=10)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    last_ip = models.CharField(max_length=15, blank=True,null=True)
    is_local = models.BooleanField(default=True)

    is_login = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_provider = models.BooleanField(default=False)

    objects = UserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']



    def __str__(self) :
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

