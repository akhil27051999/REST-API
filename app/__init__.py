from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .logger import setup_logger  # Custom logger setup function

# Step 1: Create SQLAlchemy & Migrate instances

  """
  1. These are not yet bound to any Flask app.
  2. They will be initialized later inside the factory using db.init_app(app)
  """

db = SQLAlchemy()
migrate = Migrate()

# Step 2: App factory

def create_app(config_class=None):

    """
    Flask App Factory:
    1. This function builds and returns a Flask app instance.
    2. We can pass different configuration classes (DevConfig, ProdConfig) to create the app with different environments dynamically.
    """
    
    # Step 2a: Create a new Flask app object

    app = Flask(__name__)
    
    # Step 2b: Load configuration

    """
    1. If a config_class is provided (DevConfig / ProdConfig), use it
    2. Otherwise, use the default Config class from config.py
    """

    if config_class:
        app.config.from_object(config_class)
    else:
        app.config.from_object('app.config.Config') # This will create app's based on all the configs provided inside the config.py file
    
    # Step 3: Set up logging

    # Use a custom logger for student management specific logging

    student_logger = setup_logger()
    
    # Attach the handlers from the custom logger to Flask's native logger

    app.logger.handlers = student_logger.handlers[:]
    app.logger.setLevel(student_logger.level)
    app.logger.propagate = False  # Prevent logs from being written twice
    
    # Log that the app has started

    app.logger.info("Student Management API started successfully.")

    # Step 4: Initialize database and migrations

    # This binds the SQLAlchemy and Migrate instances to the app

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so SQLAlchemy knows about them

    with app.app_context():
        from . import models
    
    # Step 5: Register Blueprints (modular routes)

    from .routes import student_bp
    app.register_blueprint(student_bp, url_prefix='/students')
    
    # Step 6: Basic routes

    @app.route('/')
    def home():
        app.logger.info("Home page accessed")
        return "Welcome to the Student Management API!"
    
    @app.route('/health')
    def health():
        app.logger.info("Health check accessed")
        return jsonify({"status": "ok"}), 200
    
    # Return the fully constructed app

    return app
