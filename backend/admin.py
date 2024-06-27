from django.contrib import admin
from backend.models import Number
from backend.models import Pokemon

# Register your models here.

class NumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'letter')  
    search_fields = ('number', 'letter') 

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'pokedex_number', 'primary_type') 
    search_fields = ('name', 'pokedex_number')  

admin.site.register(Number, NumberAdmin)
admin.site.register(Pokemon, PokemonAdmin)