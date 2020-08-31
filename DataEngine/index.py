from flask import Flask
from .views import init_view
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    init_view(app)
    return app
if __name__ == "main":
    ap = create_app()
    ap.run(debug=True)

