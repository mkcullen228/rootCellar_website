from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from wtforms import Form, FloatField, StringField #, validators,

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

def __repr__(self):
        return '<User {}>'.format(self.username)

# Model
# TODO: Valdate ranges in filed (optional)
class InputMacroNutrientsForm(Form):
    calories = FloatField()
    protein = FloatField()
    fat = FloatField()
    carbohydrate = FloatField()
    fiber = FloatField()
    cholesterol = FloatField()
    saturated_fat = FloatField()
    unsaturated_fat = FloatField()
    sugar = FloatField()

class InputMicroNutrientsForm(Form):
    Betaine = FloatField()
    Calcium = FloatField()
    Choline = FloatField()
    Copper = FloatField()
    Fluoride = FloatField()
    Folate = FloatField()
    Folate_DFE = FloatField()
    Folate_food = FloatField()
    Folic_acid = FloatField()
    Iron = FloatField()
    Magnesium = FloatField()
    Manganese = FloatField()
    Niacin = FloatField()
    Fluoride = FloatField()
    Pantothenic_acid = FloatField()
    Phosphorus = FloatField()
    Potassium = FloatField()
    Retinol = FloatField()
    Riboflavin = FloatField()
    Selenium = FloatField()
    Sodium = FloatField()
    Fluoride = FloatField()
    Thiamin = FloatField()
    Vitamin_A = FloatField()
    Vitamin_B12 = FloatField()
    Vitamin_B12_added = FloatField()
    Vitamin_B6 = FloatField()
    Vitamin_C = FloatField()
    Vitamin_D = FloatField()
    Vitamin_D2 = FloatField()
    Vitamin_D3 = FloatField()
    Vitamin_E = FloatField()
    Vitamin_E_added = FloatField()
    Vitamin_K = FloatField()
    Zinc = FloatField()

class IgnoreRecipeForm(Form):
    ignore_list = StringField()

class UserPreference(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    firstname = db.Column(db.String(64), index=True, unique=True)
    lastname = db.Column(db.String(64), index=True, unique=True)
    gender = db.Column(db.String(64), index=True, unique=True)
    age = db.Column(db.Integer, index=True)
    weight_lb = db.Column(db.Integer, index=True)
    height_in = db.Column(db.Integer, index=True)
    foods_allergic = db.Column(db.String(1200), index=True)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
