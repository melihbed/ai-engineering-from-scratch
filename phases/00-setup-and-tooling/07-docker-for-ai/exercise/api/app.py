from flask import Flask
from qdrant_client import QdrantClient

app = Flask(__name__)
client = QdrantClient(host="qdrant", port=6333)


@app.route('/')
def hello_geek():
    return '<p>Hi from Flask!</p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

