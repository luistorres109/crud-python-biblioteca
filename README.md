# 📚 CRUD Python - Sistema de Biblioteca

Um sistema CRUD de biblioteca desenvolvido em Python com MySQL, focado em praticar conceitos de orientação a objetos, arquitetura de projetos, persistência de dados, organização modular e boas práticas de desenvolvimento Back-End.

Este projeto foi desenvolvido com fins educacionais para praticar conceitos essenciais de desenvolvimento de software e banco de dados relacionais.

---

## 🚀 Funcionalidades

### 👤 Autor
- Criar autor
- Buscar autor por ID
- Atualizar dados do autor
- Remover autor

### 📖 Livro
- Criar livro
- Buscar livro por ID
- Atualizar dados do livro
- Remover livro

### 🧑 Usuário
- Criar usuário
- Buscar usuário por ID
- Atualizar dados do usuário
- Remover usuário

### 🔄 Empréstimo
- Criar empréstimo
- Buscar empréstimo por ID
- Atualizar empréstimo
- Remover empréstimo

---

## 🛡️ Regras de negócio implementadas

### Validação de datas de empréstimo
Foi implementada uma **Trigger no MySQL** para impedir inconsistência nos empréstimos:

> A data de empréstimo não pode ser posterior à data de devolução.

Exemplo inválido:

```text
Empréstimo: 20/06/2024
Devolução: 10/06/2024
```

O banco impede automaticamente esse registro.

---

## 🏗️ Arquitetura do Projeto

O projeto foi organizado utilizando separação de responsabilidades para facilitar manutenção e escalabilidade.

```text
crud-python/
│
├── config/
│   └── database.py
│
├── database/
│   └── database.sql
│
├── models/
│   ├── autor.py
│   ├── livro.py
│   ├── usuario.py
│   └── emprestimo.py
│
├── repositories/
│   ├── autor_repository.py
│   ├── livro_repository.py
│   ├── usuario_repository.py
│   └── emprestimo_repository.py
│
├── services/
│   ├── converter_data.py
│   ├── validar_data.py
│   ├── validar_email.py
│   ├── validar_nome.py
│   └── limpar_cmd.py
│
├── utils/
│   ├── menu.py
│   ├── autor.py
│   ├── livro.py
│   ├── usuario.py
│   └── emprestimo.py
│
├── requirements.txt
└── main.py
```

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- MySQL
- MySQL Connector Python

---

## ⚙️ Como Executar o Projeto

### 1. Clonar repositório

```bash
git clone https://github.com/luistorres109/crud-python.git
```

Entrar na pasta:

```bash
cd crud-python
```

---

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 3. Configurar Banco de Dados

Abra o MySQL Workbench (ou outro cliente MySQL) e execute:

```text
database/database.sql
```

Esse script irá:

- Criar banco `BibliotecaTreino`
- Criar tabelas
- Inserir dados iniciais
- Criar triggers de validação

---

### 4. Configurar conexão com banco

No arquivo:

```text
config/database.py
```

Configure suas credenciais do MySQL:

```python
host="localhost"
user="root"
password=""
database="BibliotecaTreino"
```

---

### 5. Executar aplicação

```bash
python main.py
```

---

## 🧠 Conceitos praticados

Este projeto foi utilizado para praticar:

- CRUD (Create, Read, Update, Delete)
- Programação Orientada a Objetos (POO)
- Modularização de projetos Python
- Arquitetura em camadas
- Relacionamentos em banco de dados
- Chaves estrangeiras
- Triggers MySQL
- Validações de dados
- Manipulação de datas
- Organização de código
- Repositórios e separação de responsabilidades

---

## 📈 Melhorias futuras

- [ ] Interface gráfica
- [ ] API REST com FastAPI
- [ ] Busca por nome
- [ ] Listagem paginada
- [ ] Testes automatizados
- [ ] Docker
- [ ] Logs
- [ ] Sistema de autenticação
- [ ] Relatórios de empréstimos

---

## 📌 Objetivo do Projeto

Este projeto foi desenvolvido principalmente para fins de estudo e prática de desenvolvimento Back-End, banco de dados e organização de software.

---

## 👨‍💻 Autor

- **Luís Miguel Torres Recalcatti**

**GitHub:** [luistorres109/crud-python](https://github.com/luistorres109/crud-python)
