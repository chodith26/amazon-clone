from flask import Flask, render_template, jsonify

app = Flask(__name__)

products = [
    {"name": "Harry Potter Book Set", "price": "₹3,599", "category": "Books"},
    {"name": "Stanley Cup 40oz", "price": "₹2,899", "category": "Kitchen"},
    {"name": "Wireless Headphones", "price": "₹6,499", "category": "Electronics"},
    {"name": "Yoga Mat Premium", "price": "₹1,299", "category": "Sports"},
    {"name": "Ceramic Coffee Mug", "price": "₹549", "category": "Kitchen"},
    {"name": "Mechanical Keyboard", "price": "₹4,999", "category": "Computers"},
    ]

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/api/products")
def api_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)