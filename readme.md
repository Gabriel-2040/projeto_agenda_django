Iniciar o projeto Agendda Django

```
python -m venv venv
pip install django 
django-admin startproject projeto .
python manage.py startapp contact .
```

Configurar o Git

```
git config --global user.name "seu nome"
git config --global user.email "seu email"
git config --global init.defaultBranch main
git init
git add .
git commit -m "Primeiro commit"
git remote add origin <url do repositório> - só se faz uma vez
git push -u origin main - só se faz uma vez
```

Migrando a base ded dados do Django

### Quando eu fizer alterações nos models preciso rodar esses dois comandos

```
python manage.py makemigrations
python manage.py migrate
```
## Criando e modificando a senha de um super usuario

```
python manage.py createsuperuser
python manage.py changepassword USERNAME
```

python - Usando o shell do Django. 


## Importe o modulo
```
from contact.models import Contact
```
## Cria um contato (Lazy) - Lazy significa que o contato ainda não foi salvo no banco de dados. Precisa chamar o contact.save() para salvar
### Retorna o contato
```
contact =  Contact(**fields)
```
 ** fields é um dicionario com os campos do model
contact.save() : Salva o contato no banco de dados
## Seleciona um contato com id = 10
### Retorna o contato
```
contact = Contact.objects.get(pk=10)
```
## Edita um contato
### Retorna o contato
```
contact.field_name1= 'novo valor 1'
contact.field_name2= 'novo valor 2'
contact.save()
```
## Deleta um contato
### Depende da base de dados, geralmente retorna o numero de valores manipulados na base de dados
```
contact.delete()
```
## Seleciona todos os contatos ordenando por id DESC
### Retorna QuerySet[]
```
contacts = Contact.objects.filter(**filters).order_by('-id') 
```
**filters é um dicionario com os campos do model

### ordem das coisas no django

o arquivo ou o que tiver na past views chama/renderiza o template que está na pasta templates
e a URL chama a view que está na pasta views
