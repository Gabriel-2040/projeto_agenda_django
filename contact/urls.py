from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    #pagina contact
    #fazer um CRUD - criar, ler, atualizar e deletar
    path('contact /<int:contact_id>/detail',views.contact, name='contact'),
    
    # pagina da home
    path('search/', views.search, name='search'),
    path('',views.index, name ='index'),
    
]
#isso é uma url '<int:contact_id>/', sempre deixar a barra / no final