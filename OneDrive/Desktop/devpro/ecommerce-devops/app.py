from flask import Flask, render_template

app = Flask(__name__)

products = [
    {"name": "Gaming Laptop", "price": "₹75000"},
    {"name": "iPhone 15", "price": "₹85000"},
    {"name": "Wireless Headphones", "price": "₹5000"},
    {"name": "Smart Watch", "price": "₹7000"},
    {"name": "Bluetooth Speaker", "price": "₹3000"},
    {"name": "DSLR Camera", "price": "₹65000"}
]


@app.route('/')
def home():
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)