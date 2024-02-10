from flask import Flask
from flask_smorest import Api

from items import items_blp

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Store Management API"
app.config["API_VERSION"] = "v1"

app.config.update(
    OPENAPI_VERSION="3.0.3",
    OPENAPI_JSON_PATH="api-spec.json",
    OPENAPI_URL_PREFIX="/",
    OPENAPI_SWAGGER_UI_PATH="/swagger-ui",
    OPENAPI_SWAGGER_UI_URL="https://cdn.jsdelivr.net/npm/swagger-ui-dist/",
)

api = Api(app)

api.register_blueprint(items_blp)
