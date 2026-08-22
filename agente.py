import chromadb
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.6-flash")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="faq_banco")

def buscar_contexto(pergunta_usuario, n_resultados=2):
    resultados = collection.query(
        query_texts=[pergunta_usuario],
        n_results=n_resultados
    )
    contextos = []
    for meta in resultados["metadatas"][0]:
        contextos.append(meta["resposta"])
    return contextos

def responder(pergunta_usuario):
    contextos = buscar_contexto(pergunta_usuario)
    contexto_texto = "\n".join(f"- {c}" for c in contextos)

    prompt = f"""Voce e um assistente de atendimento de um banco digital.
Responda a pergunta do cliente usando APENAS as informacoes do contexto abaixo.
Se a informacao nao estiver no contexto, diga educadamente que nao tem essa
informacao e sugira contato com a central de atendimento. Nunca invente dados.

Contexto:
{contexto_texto}

Pergunta do cliente: {pergunta_usuario}

Resposta:"""

    resposta = model.generate_content(prompt)
    return resposta.text

if __name__ == "__main__":
    print("Agente de FAQ do Banco (digite sair para encerrar)\n")
    while True:
        pergunta = input("Voce: ")
        if pergunta.lower() == "sair":
            break
        print("Agente:", responder(pergunta), "\n")