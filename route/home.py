from app import app, requests, render_template
import sqlite3


@app.get('/')
@app.get('/home')
def home():
    connection = sqlite3.connect('su79_database.sqlite3')
    cursor = connection.cursor()
    result = cursor.execute('SELECT * FROM product').fetchall()
    products = []
    for row in result:
        product = {
            'id': row[0],
            'title': row[1],
            'category': row[2],
            'price': row[3],
            'image': app.config["IMAGE_DIR"]+row[4],
        }
        products.append(product)
    connection.close()

    return render_template('home.html', products=products, error='')


@app.get('/detail/<int:pro_id>')
def detail(pro_id):
    connection = sqlite3.connect('su79_database.sqlite3')
    cursor = connection.cursor()
    result = cursor.execute('SELECT * FROM product Where id = ?', [int(pro_id)]).fetchone()
    product = {
        'id': result[0],
        'title': result[1],
        'category': result[2],
        'price': result[3],
        'image': app.config["IMAGE_DIR"]+result[4],
    }
    connection.close()

    return render_template('detail.html', product=product, error='')
