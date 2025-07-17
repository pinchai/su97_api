from flask import Flask, render_template
import requests

app = Flask(__name__)


# @app.get('/')
# @app.get('/home')
# def home():
#     return render_template('master.html')
#
#

@app.get('/')
@app.get('/home')
def home():
    products = []
    error = ''
    try:
        r = requests.get('https://fakestoreapi.com/products')
        if r.status_code == 200:
            products = r.json()
    except Exception as e:
        error = e
    return render_template('home.html', products=products, error=error)


@app.get('/detail/<int:pro_id>')
def detail(pro_id):
    product = None
    error = ''
    try:
        r = requests.get(f"https://fakestoreapi.com/products/{pro_id}")
        if r.status_code == 200:
            product = r.json()
    except Exception as e:
        error = e
    return render_template('detail.html', product=product, error=error)


@app.get('/cart')
def cart():
    return render_template('cart.html')


@app.get('/support')
def about():
    return render_template('support.html')


if __name__ == '__main__':
    app.run()
