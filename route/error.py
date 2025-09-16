from app import app, requests, render_template


@app.errorhandler(404)
def error_404(e):
    return {
        "status": "Page Not Found",
    }, 404


@app.errorhandler(500)
def error_500(e):
    return {
        "status": "Oop Internal server Error",
    }, 500
