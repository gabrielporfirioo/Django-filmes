
# API de Filmes com Django

Uma API simples para gerenciar uma coleção de filmes, construída com Django e Django Rest Framework (DRF). Este projeto demonstra como construir uma API RESTful usando o Django.

## Funcionalidades

- Listar todos os filmes
- Adicionar um novo filme
- Recuperar detalhes de um filme específico
- Atualizar informações de um filme
- Deletar um filme

## Tecnologias Utilizadas

- **Python 3.x**
- **Django 4.x**
- **Django Rest Framework (DRF)**
- **SQLite** (banco de dados padrão do Django, mas pode ser alterado para outro)

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado na sua máquina:

- **Python 3.x**: [Instalar Python](https://www.python.org/downloads/)
- **pip**: Deve estar instalado junto com o Python, mas se não estiver, confira o guia de instalação do [pip](https://pip.pypa.io/en/stable/installation/)
- **Virtualenv**: (opcional, mas recomendado) para isolar o ambiente do projeto

## Instruções de Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/api-de-filmes-django.git
cd api-de-filmes-django
```

### 2. Criar um Ambiente Virtual

Recomenda-se o uso de um ambiente virtual para evitar conflitos com outros projetos.

```bash
# No macOS/Linux
python3 -m venv venv
source venv/bin/activate

# No Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as Dependências

Use o `pip` para instalar as dependências listadas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

Se o `requirements.txt` ainda não foi gerado, você pode instalar as dependências manualmente:

```bash
pip install django djangorestframework
```

### 4. Aplicar as Migrações

Antes de rodar o projeto, certifique-se de configurar o banco de dados aplicando as migrações.

```bash
python manage.py migrate
```

### 5. Criar um Superusuário (Opcional)

Caso queira acessar a interface de administração do Django:

```bash
python manage.py createsuperuser
```

### 6. Executar o Servidor

Inicie o servidor de desenvolvimento com o seguinte comando:

```bash
python manage.py runserver
```

O servidor deve estar rodando em `http://127.0.0.1:8000/`.

## Endpoints da API

Aqui está uma lista dos principais endpoints da API fornecidos por este projeto:

| Método | Endpoint            | Descrição                     |
|--------|---------------------|-------------------------------|
| GET    | `/api/filmes/`       | Listar todos os filmes        |
| POST   | `/api/filmes/`       | Adicionar um novo filme       |
| GET    | `/api/filmes/{id}/`  | Recuperar um filme pelo ID    |
| PUT    | `/api/filmes/{id}/`  | Atualizar um filme pelo ID    |
| DELETE | `/api/filmes/{id}/`  | Deletar um filme pelo ID      |

### Exemplo de JSON para Requisições POST/PUT

```json
{
    "titulo": "A Origem",
    "diretor": "Christopher Nolan",
    "ano_lancamento": 2010,
    "genero": "Sci-Fi"
}
```

## Rodando Testes

Para garantir que tudo está funcionando corretamente, você pode rodar os testes utilizando o framework de testes do Django:

```bash
python manage.py test
```

## Recursos Adicionais

- [Documentação do Django](https://docs.djangoproject.com/)
- [Documentação do Django Rest Framework](https://www.django-rest-framework.org/)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
