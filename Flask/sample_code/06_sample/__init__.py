from flask import Flask
import hello_blueprint

def create_app():
    app = Flask(__name__, static_url_path="/static")
    app.register_blueprint(hello_blueprint.bp)
    app.run(host="127.0.0.1", port="8006")


if __name__ == "__main__":
    create_app()