# CRUD com Flask e SQLite

Este é um projeto CRUD (Create, Read, Update, Delete) desenvolvido em **Flask**, com persistência de dados utilizando **SQLite**. O frontend utiliza **HTML**, **CSS**, **JavaScript**, e **Bootstrap** para uma interface amigável e responsiva.

---

## 🚀 Funcionalidades

- **Criar Usuário**: Adicionar novos usuários com nome e email.
- **Listar Usuários**: Exibir uma lista de todos os usuários cadastrados, incluindo as datas de criação e atualização.
- **Editar Usuário**: Atualizar nome e email de um usuário específico.
- **Excluir Usuário**: Remover um usuário da base de dados.

---

## 📂 Estrutura do Projeto

```plaintext
project_crud_flask_sqlite/
├── app.py              # Arquivo principal do Flask
├── models.py           # Definição do modelo User e configurações do banco
├── routes.py           # Rotas CRUD do Flask
├── index.html          # Página principal do frontend
├── script.js           # JavaScript para interações no frontend
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
```

# Como Configurar o Projeto

Siga os passos abaixo para configurar e executar o projeto em sua máquina local.

---

## 🛠️ Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:

- **Python 3.9+**: [Download Python](https://www.python.org/downloads/)
- **Git**: [Download Git](https://git-scm.com/)

---

## ⚙️ Passos de Configuração

### 1. Clone o Repositório

Faça o clone do repositório em sua máquina:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtua

- **No Windows**
```bash
venv\Scripts\activate
```

- **No macOS/Linux**
```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute o servidor Flask

```bash
python app.py
```
### 6. Abra o navegador e acesse

```bash
http://127.0.0.1:5000/
```
---

# 🧪 Executando os Testes

Siga os passos abaixo para executar os testes do projeto e gerar um relatório em HTML.

## 🛠️ Pré-requisitos

Certifique-se de que o **pytest** e o **pytest-html** estão instalados no ambiente virtual.

### 1. Instale as Dependências de Testes

Caso ainda não tenha instalado, execute o execute o comando:

```bash
pip install pytest pytest-html
```

### 2. Execute o seguinte comando no terminal

```bash
pytest tests/ --capture=tee-sys --log-cli-level=INFO --html=report.html
```
