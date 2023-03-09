
# Culinary Recipes API

Uma API simples utilizando Django Rest Framework para chef's manterem receitas que podem ser consultadas publicamente por usuários não necessariamente autenticados.

## Importante

Para rodar localmente é necessário rodar um "createsuperuser" para criar um Chef(admin), pois além de algumas funções necessitarem de autenticação, o Chef é um atributo required da receita. Caso rode utilizando o Dockerfile não será um problema pois jé é iniciado um usuário (de login: "admin" e password: "admin") automaticamente.

## Libs externas

Foram utilizadas as seguintes libs externas e suas dependências (vide requirements.txt):
 - https://pypi.org/project/drf-yasg/ (para documentação no Swagger)
 - https://pypi.org/project/django-filter/ (para filtros de busca)
