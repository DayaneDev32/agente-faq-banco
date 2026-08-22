# Agente de IA para FAQ Bancario

Agente conversacional com arquitetura RAG (Retrieval-Augmented Generation) para responder perguntas frequentes de um banco digital ficticio, usando busca semantica e geracao de linguagem natural.

## Objetivo

Demonstrar a construcao de um agente de IA aplicado ao setor bancario, com foco em reduzir alucinacao (respostas inventadas) atraves de recuperacao de contexto real antes da geracao da resposta.

## Tecnologias

- Python - linguagem principal
- ChromaDB - banco de dados vetorial para busca semantica (embeddings)
- Google Gemini API - modelo de linguagem para geracao das respostas
- python-dotenv - gerenciamento seguro de variaveis de ambiente

## Como funciona (arquitetura RAG)

1. A FAQ do banco e indexada no ChromaDB como vetores semanticos (embeddings)
2. Quando o cliente faz uma pergunta, o sistema busca as perguntas mais parecidas semanticamente na base (nao apenas por palavras-chave)
3. O contexto recuperado e enviado junto com a pergunta para o modelo Gemini
4. O modelo gera uma resposta baseada apenas no contexto fornecido, reduzindo o risco de informacoes inventadas - ponto critico em aplicacoes do setor financeiro

## Estrutura do projeto

faq.py - base de dados da FAQ (perguntas e respostas)
indexar.py - indexa a FAQ no banco vetorial ChromaDB
agente.py - agente conversacional (busca contexto e gera resposta)

## Como rodar localmente

1. Clone o repositorio:
git clone https://github.com/DayaneDev32/agente-faq-banco.git
cd agente-faq-banco

2. Crie e ative o ambiente virtual:
python -m venv venv
venv\Scripts\activate

3. Instale as dependencias:
pip install chromadb google-generativeai python-dotenv

4. Crie um arquivo .env na raiz do projeto com sua chave da API do Gemini:
GEMINI_API_KEY=sua_chave_aqui

Obtenha gratuitamente em https://aistudio.google.com/apikey

5. Indexe a FAQ:
python indexar.py

6. Rode o agente:
python agente.py

## Proximos passos (producao)

Este projeto e um prototipo funcional. Para uma aplicacao bancaria real, seriam necessarias camadas adicionais de infraestrutura em nuvem, autenticacao, compliance regulatorio (LGPD/Bacen), testes de carga e monitoramento continuo.

## Autora

Daiany - em transicao de carreira para tecnologia, com foco em IA aplicada.
