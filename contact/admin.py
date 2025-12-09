from django.contrib import admin
from contact import models 
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone','email','created_date','description','show',) #campos da pagina models
    ordering = ('-id',) #colocando o - antes do id fica na ordem decrescente com os mais novos primeiro.
    list_filter = ('created_date',) #colocando filtro na pagina
    search_fields = ('id','first_name','email',)
    #list_max_show_all = 20 #mostrar a quantidade certa pois pesa muito no banco o quanto mostrar
    list_editable = ('first_name','last_name','show') 
    list_display_links = ('id','phone','email',) # o que esta no campo list_editable não pode estar no list_display_links


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) #campos da pagina models
    ordering = ('-id',) #colocando o - antes do id fica na ordem decrescente com os mais novos primeiro.
    