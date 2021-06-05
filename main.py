from flask import Flask, render_template

def create_app():
    app = Flask(__name__)    
    
    @app.route("/api")
    def api():
        return render_template("index.html")
    return app
    
app = create_app()