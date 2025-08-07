from app import app, requests, render_template


@app.get('/checkout')
def checkout():
    return render_template('checkout.html')
