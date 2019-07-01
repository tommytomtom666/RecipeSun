"""
Definition of models.
"""

from django.db import models

# Create your models here.


# Different ingridients
class CookingIngridient(models.Model):
    def __str__(self):
        return self.name
    ci_nameDe = models.CharField(max_lenght=200)
    ci_weigtht = models.IntegerField('[g]')
    ci_price = models.IntegerField('[€]')
    ci_allergenic = models.CharField()  # Hier besser nur Optionen
    ci_season = models.CharField() # mehrere Monate durch Beistrich getrennt
    ci_supplier = # Aus anderer Datenbank
