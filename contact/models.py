from django.db import models
from django.utils import timezone
# Create your models here.

#id(primary key) - django gera automatico
# , first_name(string), last_name(string), phone(string), email(email), created_date(date), description(text),

#sera dfeito depois
# category(foreingkey), show(boolean), owner(ForeignKey), picture(imagem)

# estamos criando campos de um formulário que vai preencher uma tabela no banco de dados
# blank = True é que não precisa preencher o campo
# TextField é para textos grandes. diferente de CharField que é até 254 caracteres.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    phone =  models.CharField(max_length=50)
    email =  models.EmailField(max_length=254, blank = True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    