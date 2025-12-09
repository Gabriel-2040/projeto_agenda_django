from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# id(primary key) - django gera automatico
# , first_name(string), last_name(string), phone(string), email(email), created_date(date), description(text),

# sera dfeito depois
# category(foreingkey), show(boolean), picture(imagem)
# Depois
# owner(ForeignKey),

# estamos criando campos de um formulário que vai preencher uma tabela no banco de dados
# blank = True é que não precisa preencher o campo
# TextField é para textos grandes. diferente de CharField que é até 254 caracteres.


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categorias'
        verbose_name = 'Categoria'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name} '


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='picture/%Y/%m/%d')
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    owner = models.ForeignKey(User,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
