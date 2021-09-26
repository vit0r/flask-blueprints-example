from flask import Flask

from blueprints.modulo1 import modulo1_blueprint
from blueprints.modulo2 import modulo2_blueprint

app = Flask(__name__)

app.register_blueprint(modulo1_blueprint)
app.register_blueprint(modulo2_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
