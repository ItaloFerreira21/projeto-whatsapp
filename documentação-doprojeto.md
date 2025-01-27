# Projeto de Automação de Grupos no WhatsApp

## Objetivo do Projeto

Automatizar o processo de criação de grupos no WhatsApp para empresas que contratam freelancers, facilitando a gestão dos mesmos e evitando a repetição de etapas, como o preenchimento de formulários.

---

## Funcionalidades

### 1. Cadastro de Freelancers

- **Dados necessários:**
  - Nome completo
  - Número de celular
  - Sexo
  - E-mail (quando necessário)
  - Número de RG (para garantir a identidade)
  - Chave PIX (para pagamentos)

- **Como será feito:**
  - O contratante insere os dados no sistema.
  - Esses dados são salvos no banco de dados do sistema, sendo reutilizados para criar grupos sem a necessidade de preenchimento repetido.

### 2. Criação de Vagas e Grupos

- **Como funciona:**
  - O contratante cria uma vaga no aplicativo com especificações do evento/trabalho.
  - O aplicativo gera um link único para ser enviado aos freelancers.
  - Quando um freelancer clica no link, ele é adicionado automaticamente a um novo grupo no WhatsApp relacionado ao trabalho, sem ser removido do grupo original.

### 3. Envio de Formulários

- **Formulário:**
  - Após a seleção de um freelancer, o sistema automaticamente envia um formulário com informações pré-preenchidas, baseadas no banco de dados do freelancer.
  - O freelancer só precisa confirmar ou atualizar as informações antes de finalizar.

---

## Fluxo do Sistema

1. **Contratante realiza o login.**
2. **Contratante cadastra novos freelancers no banco de dados.**
3. **Contratante cria uma vaga com as especificações necessárias (ex: descrição do trabalho, horário, requisitos).**
4. **Sistema gera um link exclusivo para a vaga e o contratante envia para o grupo de freelancers no WhatsApp.**
5. **Freelancers que clicarem no link são pré-selecionados para o trabalho, permanecendo no grupo original.**
6. **Formulário com dados do freelancer é enviado automaticamente para o freelancer preencher, caso ainda não tenha completado.**

---

## Tecnologias Utilizadas

- **Backend:** Python (Flask)
- **Frontend:** React, TailwindCSS
- **Banco de Dados:** PostgreSQL
- **Autenticação:** JWT
- **Integração com WhatsApp:** API para automatização de grupos

---

## Estrutura do Banco de Dados

### 1. Tabela `Freelancers`

| Coluna        | Tipo de Dados     | Descrição                               |
|---------------|-------------------|-----------------------------------------|
| id            | INTEGER           | Identificador único do freelancer       |
| nome          | VARCHAR(255)      | Nome completo                          |
| celular       | VARCHAR(15)       | Número de celular                       |
| sexo          | VARCHAR(10)       | Sexo (masculino/feminino)               |
| email         | VARCHAR(255)      | E-mail (opcional)                       |
| rg            | VARCHAR(20)       | Número de RG (opcional)                |
| chave_pix     | VARCHAR(50)       | Chave PIX (opcional)                   |

### 2. Tabela `Vagas`

| Coluna        | Tipo de Dados     | Descrição                               |
|---------------|-------------------|-----------------------------------------|
| id            | INTEGER           | Identificador único da vaga             |
| titulo        | VARCHAR(255)      | Título da vaga                         |
| descricao     | TEXT              | Descrição do trabalho                   |
| data_inicio   | TIMESTAMP         | Data de início da vaga                  |
| data_fim      | TIMESTAMP         | Data de término da vaga                 |

---

## Passos Futuros

1. **Melhorar a integração com o WhatsApp** – Estudar formas de automatizar a criação de grupos diretamente no WhatsApp usando APIs externas ou ferramentas de automação.
2. **Adicionar funcionalidades de filtro e busca** – Permitir que o contratante filtre freelancers por habilidades ou experiência.
3. **Implementar painel administrativo** – Para gerenciar usuários e visualizar o andamento de vagas e formulários.

---

## Como Rodar o Projeto

### Backend (Flask)

1. **Instalar dependências**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Rodar o servidor**:
    ```bash
    python app.py
    ```

### Frontend (React)

1. **Instalar dependências**:
    ```bash
    npm install
    ```

2. **Rodar o servidor**:
    ```bash
    npm start
    ```

---


 Banco de Dados e Estrutura de Dados
Prioridade: Alta
O que já temos: Freelancer com campos como nome, celular e sexo.
O que falta fazer:
Criar tabelas para armazenar dados do freelancer.
Definir a estrutura do banco de dados com os campos necessários (email, nome completo, celular, RG, chave PIX, sexo).
Relacionar dados entre freelancers e contratantes (cada contratante terá acesso aos seus freelancers cadastrados).
Adicionar campos para os grupos de trabalho e vagas (data, descrição, status do grupo, etc).


2. Autenticação e Acesso dos Contratantes
Prioridade: Alta
O que já temos: O registro e login de contratantes com JWT funcionando.
O que falta fazer:
Definir níveis de acesso: Um contratante só deve ter acesso aos freelancers que ele cadastrou.
Permitir que contratantes possam visualizar, adicionar, editar e excluir freelancers.
Garantir que apenas contratantes autenticados possam realizar operações no sistema (uso do JWT).


3. Criação de Mensagens e Links de Seleção
Prioridade: Alta
O que já temos: O sistema de envio de links para grupos.
O que falta fazer:
Implementar a criação de mensagens com os detalhes da vaga.
Gerar links únicos para cada vaga, de forma que quando os freelancers clicarem, sejam pré-selecionados para o evento, mas ainda permaneçam no grupo original.
Gerar um novo grupo para o evento específico e adicionar os freelancers selecionados.


4. Formulário para Freelancers
Prioridade: Média
O que já temos: A ideia de que freelancers devem preencher um formulário com dados como email, nome completo, número de celular, etc.
O que falta fazer:
Criar a interface de formulário onde os freelancers preencherão os dados.
Automatizar o preenchimento do formulário com dados que já possuímos no banco (nome, celular, sexo).
Validar o formulário de forma que o freelancer só possa enviar quando os campos obrigatórios estiverem completos.


5. Integração com WhatsApp
Prioridade: Baixa
O que já temos: A intenção de integrar com o WhatsApp, mas ainda não começamos a implementação direta.
O que falta fazer:
Integrar o sistema para criar grupos automaticamente no WhatsApp com os freelancers selecionados.
Automatizar o processo de envio de links para o grupo do WhatsApp.


6. Interface de Administração (Para Contratantes)
Prioridade: Média
O que já temos: Uma ideia básica de que o contratante precisará de uma interface para gerenciar seus freelancers e eventos.
O que falta fazer:
Criar uma interface no frontend onde o contratante pode ver a lista de freelancers, criar novas vagas e ver o status das vagas.
Adicionar filtros para gerenciar os freelancers com base em critérios como "disponibilidade" ou "habilidades" (se necessário).


7. Testes e Validação
Prioridade: Média
O que já temos: Algumas funcionalidades já estão implementadas, mas precisamos garantir que tudo está funcionando como esperado.


O que falta fazer:
Criar testes de integração e unitários para garantir que a criação de grupos, links e mensagens está funcionando corretamente.
Testar o fluxo de autenticação para garantir que o sistema de login e autorização esteja seguro e funcional.
Ordem de Prioridade:
Banco de Dados e Estrutura de Dados.
Autenticação e Acesso dos Contratantes.
Criação de Mensagens e Links de Seleção.
Formulário para Freelancers.
Integração com WhatsApp.
Interface de Administração.
Testes e Validação.