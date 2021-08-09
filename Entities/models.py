from django.db import models
from phonenumber_field import modelfields
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager



class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):    
        if not email :
            raise ValueError("Users must have an email")

        user = self.model(
            email = self.normalize_email(email),
        )      

        user.set_password (password)
        user.save(using=self._db) 
        return user 


    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
        )

        user.admin = True
        user.staff = True
        user.superuser = True

        user.save(using=self._db)
        return user



# Account model 
class Account(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60, unique=True)
    avatar = models.ImageField(null=True, blank=True)
    telephone = modelfields.PhoneNumberField(blank=True, null=True)
    cin = models.CharField(max_length=10, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_login = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = AccountManager()


    def __str__(self) -> str:
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    




# Categorie model, following the class diagramm specifications

class Categorie(models.Model):
    idCategorie = models.AutoField(primary_key=True, editable=False)
    libelleCategorie = models.CharField(max_length=256)

    def __str__(self):
        return self.libelleCategorie

    
    



# Article model, following the class diagramm specifications
class Article(models.Model):
    idArticle = models.AutoField(primary_key=True, editable=False)
    imageArticle = models.ImageField(blank=True, null=True)
    categorieArticle = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    nomArticle = models.CharField(max_length=50)
    descriptionArticle = models.CharField(max_length=256)
    quantiteArticle = models.IntegerField()
    prixArticle = models.FloatField()
    dateAjoutArticle = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomArticle





# Mode de livraison model, following the class diagramm specifications
class ModeDeLivraison(models.Model):
    idModeDeLivraison = models.AutoField(primary_key=True, editable=False)
    libelleModeDeLivraison = models.CharField(max_length=50)
    descriptionModeDeLivraison = models.CharField(max_length=256)

    def __str__(self):
        return self.libelleModeDeLivraison


# Mode de paiement model, following the class diagramm specifications
class ModeDePaiement(models.Model):
    idModeDePaiement = models.AutoField(primary_key=True, editable=False)
    libelleModeDePaiement = models.CharField(max_length=50)
    descriptionModeDePaiement = models.CharField(max_length=256)

    def __str__(self):
        return self.libelleModeDePaiement


# Commande model, following the class diagramm specifications
class Commande(models.Model):
    idCommande = models.AutoField(primary_key=True, editable=False)
    modeDeLivraisonCommande = models.ForeignKey(ModeDeLivraison, on_delete=models.CASCADE)
    modeDePaiementCommande = models.ForeignKey(ModeDePaiement, on_delete=models.CASCADE)
    dateAjoutCommande = models.DateTimeField(auto_now_add=True)
    descriptionCommande = models.CharField(max_length=256)

    def __str__(self):
        return self.dateAjoutCommande



# Facture model, following the class diagramm specifications
class Facture(models.Model):
    idFacture = models.AutoField(primary_key=True, editable=False)
    clientFacture  = models.ForeignKey(Account, on_delete=models.CASCADE)
    datePaiementFacture = models.DateTimeField(auto_now_add=True)
    prixHtFacture = models.FloatField()
    totalHtFacture = models.FloatField()
    totalTtc = models.FloatField()

    def __str__(self):
        return "Facture de " + str(self.clientFacture)


