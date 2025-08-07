from app import app, requests, render_template


@app.get('/support')
def support():
    return render_template('support.html')
