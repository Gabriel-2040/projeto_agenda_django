from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
     # pagina da home
    path('',views.index, name ='index'),
    path('search/', views.search, name='search'),

    #pagina contact
    #fazer um CRUD - criar, ler, atualizar e deletar
    path('contact/<int:contact_id>/',views.contact, name='contact'),
    path('contact/<int:contact_id>/update',views.update, name='update'),
    path('contact/create/',views.create, name='create'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),

   
    
    
]
#isso é uma url '<int:contact_id>/', sempre deixar a barra / no final