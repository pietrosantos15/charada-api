### Curso Técnico de Desenvolvimento de Sistemas - Senai Itapeva
<h1 align="center"> Charada do Dia 🧠 </h1>
Este projeto é um sistema web construído utilizando Flask e Firestore (Firebase) como banco de dados. O objetivo é proporcionar uma experiência interativa onde o usuário recebe uma charada aleatória, insere sua resposta e descobre se acertou. O sistema também permite gerenciar (adicionar, editar e remover) charadas via API.

## Índice
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Como usar](#como-usar)
- [Autores](#autores)
- [Status](#status)

## Funcionalidades
 - Exibir uma charada aleatória do Firestore
 - Inserir resposta e validar com a correta
 - Mostrar feedback ao usuário (acertou ou errou)
 - Botão para gerar nova charada
 - API com rotas para adicionar, editar, excluir e buscar charadas
 - Integração com Firebase para armazenamento em nuvem

## Tecnologias

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![image](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![image](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![image](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)

## Como usar

### 🔧 Pré-requisitos
Antes de rodar o projeto, certifique-se de ter instalado:
- [Python 3.10+](https://www.python.org/)
- [Pip](https://pip.pypa.io/en/stable/)
- Um arquivo de credenciais Firebase: `ServiceAcccountKey.json`  
> Você deve obter esse arquivo ao criar um projeto no [Firebase Console](https://console.firebase.google.com/) e configurar o Firestore.

### 📥 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
