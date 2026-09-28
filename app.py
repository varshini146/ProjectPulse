from flask import Flask, request, jsonify, render_template
from services.hindsight_service import retain_memory, recall_memory

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/api/memory", methods=["POST"])
def add_memory():
    data = request.get_json()

    if not data or "content" not in data:
        return jsonify({"error": "content is required"}), 400

    retain_memory(data["content"])

    return jsonify({
        "success": True,
        "message": "Project memory stored successfully."
    })


@app.route("/api/memory", methods=["GET"])
def get_memory():
    query = request.args.get("q")

    if not query:
        return jsonify({"error": "query is required"}), 400

    result = recall_memory(query)

    memories = []

    if hasattr(result, "results"):
        for item in result.results:
            memories.append({
                "text": item.text,
                "type": item.type
            })

    return jsonify({
        "success": True,
        "results": memories
    })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)