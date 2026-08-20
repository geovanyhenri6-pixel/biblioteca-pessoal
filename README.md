# Biblioteca Pessoal

Um site simples pra organizar a leitura: cadastro dos livros que eu quero ler, que estou lendo ou já li, com nota pros que terminei e um resumo com estatísticas de leitura (quantos livros, nota média, distribuição por status).

Esse é um projeto de estudo — o objetivo principal foi aprender Flask e banco de dados relacional (SQLite) na prática, além de front-end básico (HTML/CSS/um pouco de JavaScript) construindo o visual do zero.

## Tecnologias

- Python
- Flask
- SQLite

## Como rodar localmente

```bash
git clone https://github.com/geovanyhenri6-pixel/biblioteca-pessoal
cd biblioteca

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Cria um arquivo `.env` na raiz do projeto com:

```
SECRET_KEY=<gere um valor com o comando abaixo>
DATABASE=instance/biblioteca.db
```

```bash
python -c "import secrets; print(secrets.token_hex(16))"
```

Inicializa o banco:

```bash
flask --app app init-db
```

Roda o servidor:

```bash
flask --app app run --debug
```

## Estrutura do banco

### `usuarios`

| Campo | Descrição |
|---|---|
| `id` | chave primária |
| `nome` | |
| `email` | único |
| `senha_hash` | senha armazenada com hash (nunca em texto puro) |
| `data_criacao` | preenchido automaticamente |

### `livros`

| Campo | Descrição |
|---|---|
| `id` | chave primária |
| `usuario_id` | chave estrangeira → `usuarios.id` |
| `titulo` | |
| `autor` | |
| `status` | `quero_ler`, `lendo` ou `lido` |
| `nota` | de 1 a 10 (com casas decimais), só relevante quando `status = lido` |
| `data_criacao` | preenchido automaticamente |

Cada usuário só enxerga e mexe nos próprios livros — todas as consultas e alterações são sempre filtradas pelo `usuario_id` da sessão.

## Funcionalidades

- Cadastro e login com sessão, senha armazenada com hash (nunca em texto puro)
- Adicionar, editar e remover livros
- Filtro da listagem por status (quero ler / lendo / lido)
- Nota de 1 a 10 pra livros já lidos, com um slider customizado
- Página de estatísticas: total de livros, quantos já foram lidos, nota média e um gráfico de barras por status
- Layout próprio, com identidade visual construída do zero (paleta de cores, tipografia, sistema de componentes)