from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


class Product:
    def __init__(self, id, name, description, price, image_url):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.image_url = image_url

    def get_product(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "image_url": self.image_url
        }


@app.route("/products", methods=["GET"])
def get_products():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 24))
    offset = (page - 1) * limit

    conn = sqlite3.connect("./back/bdd.sqlite")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products LIMIT ? OFFSET ?", (limit, offset))
    rows = cursor.fetchall()
    conn.close()

    products = [
        Product(id=row[0], name=row[1], description=row[2], price=row[3], image_url=row[4]).get_product()
        for row in rows
    ]

    return jsonify({"products": products, "page": page, "limit": limit})


if __name__ == "__main__":
    app.run(debug=True, port=8080)
