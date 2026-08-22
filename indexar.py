import chromadb
from faq import faq_data

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="faq_banco")

for i, item in enumerate(faq_data):
    collection.add(
        documents=[item["pergunta"]],
        metadatas=[{"resposta": item["resposta"]}],
        ids=[f"faq_{i}"]
    )

print(f"{len(faq_data)} perguntas indexadas com sucesso!")