# API Rest para cadastro de vagas de empregos, com autenticação de usuários.

## 📖  Descrição

Esse é o projeto de uma API Rest para cadastro de vagas de emprego. Ela armazena o cadastro de novos usuários e autentica para realizar as operações de CRUD (Create, Read, Update, Delete) com vagas e suas tecnologias.

<br/>

## 🛠️ Funcionalidades

- Cadastro de usuário
- Obtém um token de acesso apartir das credencias de usuário, necessário para utilizar os serviços.    
- Crud de vagas 
- Crud de tecnologias

<br/>

## 📡 Tecnologias utilizadas 
<div align="center"> 
<img align="center" alt="caio-py" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
  <img align="center" alt="caio-django" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg">
  <img align="center" alt="caio-pg" height="30" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original-wordmark.svg">
</div>
<br/><br/>

## ⏳ Inicialização

Esse projeto foi desenvolvido em ambiente Linux, utilizando o Ubuntu 22 e as tecnologias citadas anteriormente. 

1 - Primeiro clone o repositório e entre na pasta do projeto.

```bash
# Clone este repositório
$ git clone https://github.com/CaioSilva23/django-rest-framework.git

# Entre na pasta
$ cd django-rest-framework
```

2 - Segundo inicie um ambiente virtual

```bash
# Criar
  # Linux
    $ python3 -m venv venv
  # Windows
    $ python -m venv venv

#Ativar
  # Linux
    $ source venv/bin/activate
  # Windows
    $ venv/Scripts/Activate
```

3 - Instale as dependências

```bash
# Instale as dependências
# Linux
$ pip3 install -r requirements.txt
# Windows
$ pip install -r requirements.txt
```

4 - Faça as migrações e inicie a plicação.
```bash
# Linux e Windows
python3 manage.py migrate
python3 manage.py runserver
```

<br/>

## 🔎 Status do Projeto

![Badge em Desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento-green)

<br/>

## 📑 Referências

[Django REST framework](https://www.django-rest-framework.org/)
[Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)


Se inscreva no meu canal do [youTube](https://www.youtube.com/@caiosilva7722)

