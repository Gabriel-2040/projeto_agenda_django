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

    #User
    path('user/create/',views.register, name='register'),
    path('user/login/',views.login_view, name='login'),
    path('user/logout/',views.logout_view, name='logout'),
    path('user/update/',views.user_update, name='user_update'),

]
#tudo aqui nesse arquivo de urls vem da pasta views. são as funções
#isso é uma url '<int:contact_id>/', sempre deixar a barra / no final