import logging
import logging.config
import os
import traceback

import connexion
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import configs
from fruitst.usecases.exceptions import FruitStError

db = SQLAlchemy()


def create_app(config=None):
    if config is None:
        configs_map = {
            'development': configs.DevelopmentConfig,
            'testing': configs.TestingConfig,
            'production': configs.ProductionConfig
        }
        env = os.environ.get("ENV", "development").lower()
        config = configs_map[env]

    app = connexion.FlaskApp(__name__, specification_dir='swagger/')
    app.add_api('fruitst_api.yaml')

    flask_app = app.app
    flask_app.config.from_object(config)

    CORS(flask_app, supports_credentials=True)
    configure_log_handlers(flask_app)
    configure_exception_handlers(flask_app)

    db.init_app(flask_app)
    return flask_app


def configure_log_handlers(app):
    """Config log handlers for application.

    Args:
        app (flask.Flask): flask application instance
    """
    logging.config.fileConfig(app.config["LOGGER_CONFIG_PATH"])

    logger = logging.getLogger("root")

    # unify log format for all handers
    for handler in logger.root.handlers:
        app.logger.addHandler(handler)
    app.logger.setLevel(logger.root.level)

    app.logger.info("Start api services info log")
    app.logger.error("Start api services error log")


def configure_exception_handlers(app):
    def handle_api_exception(exception):
        traceback.print_exc()
        app.logger.error(str(exception))
        if isinstance(exception, FruitStError):
            return {"error": {"code": exception.code, "message": exception.message}}, 400
        return {"error": {"code": "000", "message": "Unknown error"}}, 500

    app.register_error_handler(Exception, handle_api_exception)
