from flask import Flask, Blueprint
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS
import os
from models import db
from main import main_bp
from tags import tags_bp
from event import event_bp
from review import review_bp
from userroute import user_bp
from booking import booking_bp
from interests import interest_bp
from photo_controller import photo_bp
from Auth import jwt, bcrypt, auth_bp
from billing_info import billing_info_bp
from pricing_controller import pricing_bp
from routes.advert import advert_fees_bp
from routes.profiles import profiles_bp



def create_app():
    app = Flask(__name__)    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    migrate = Migrate(app, db)
    ma = Marshmallow(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(event_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(interest_bp)
    app.register_blueprint(billing_info_bp)
    app.register_blueprint(profiles_bp)
    app.register_blueprint(advert_fees_bp)
    app.register_blueprint(tags_bp)
    app.register_blueprint(pricing_bp)
    app.register_blueprint(photo_bp)
    CORS(app, resources={r"*": {"origins": "*"}})
 
    
    return app

app = create_app()
