from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    userDocument = models.CharField(max_length=255, unique=True, null=False)
    creditCardToken = models.CharField(max_length=255, unique=True, null=False)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
class Meta:
    db_table = "user"
    verbose_name = "Usuários"
    sensitive_fields = ["userDocument", "creditCardToken"]      