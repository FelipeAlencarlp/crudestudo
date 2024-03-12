# CRUD feito com Python + Django

## Python version: 3.10.12
## Banco de dados: SQlite3

### Features

- [x] Cadastro de produtos
- [x] Listar produtos
- [x] Visualizar produtos
- [x] Editar produtos
- [x] Deletar produtos

Para utilização é preciso realizar o git clone do projeto. Abra o terminal e realize o seguinte comando:

```bash
git clone git@github.com:FelipeAlencarlp/crudestudo.git
```

Assim que realizado o git clone rodar o seguinte comando dentro da pasta do projeto no terminal:

```bash
python3 -m venv .venv
```

Em seguida:

```bash
python3 manage.py migrate
```

E por último basta iniciar o projeto:

```bash
python3 manage.py runserver
```