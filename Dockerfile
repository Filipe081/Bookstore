# `python-base` sets up all our shared environment variables
FROM python:3.12-slim as python-base

# python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.5.1 \ 
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Atualiza o PATH para incluir o Poetry e o ambiente virtual
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instalar dependências do sistema
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl build-essential libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Instalar Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Configurar o diretório de instalação das dependências
WORKDIR $PYSETUP_PATH

# Copiar arquivos de dependências do projeto
COPY poetry.lock pyproject.toml ./

# Instalar dependências do Poetry, sem incluir as de desenvolvimento
RUN poetry install --without dev

# Instalar o psycopg2 para trabalhar com PostgreSQL
RUN pip install psycopg2

# Configurar o diretório de trabalho da aplicação
WORKDIR /app

# Copiar o código do projeto
COPY . /app/

# Expor a porta usada pelo Django
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
