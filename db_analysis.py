import chromadb
import pprint

print = pprint.pprint

chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(name="my_collection")

def load_data():
    with open("elevators.txt","r") as f:
        content=f.read()
    content=content.split("\n")
    return content

def add_data_to_database(content):
    collection.upsert(
        documents=content,
        ids=[f"id{n}" for n in range(len(content))]
    )

def run_query():
    queries = [
        "What is the busiest time for the elevator",
        "how many trips does the elevator take at 10",
        "how long do the trip take at 13"
    ]

    for query in queries:
        results = collection.query(
            query_texts=[query],
            n_results=2
        )
        print(f"Results for '{query}':")
        print(results)

def app():
    x =load_data()
    print(x)
    add_data_to_database(x)
    run_query()

if __name__ =="__main__":
    app()