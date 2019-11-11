from flask import Flask, render_template, session, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DateTimeField, BooleanField, TextAreaField, SelectField
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "mySecretKey"

# These are a few lines to set up the database for the app.
# we also have to import the os and the flask_sqlalchemy 
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ###############################################
# Next we create a model (table) for the customer
# ############################################### 

class CUSTOMER(db.Model):

    # The name of the table. If not populated it would inherit the name of CUSTOMER
    __tablename__ = "customer_info"

    customer_id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.Text)

    def __init__(self,first_name):
        self.first_name = first_name

    def __repr__(self):
        return f"The customer name is {self.first_name}."




class PersonalInfo(FlaskForm):
    submit = SubmitField("Υποβολή")
    first_name = StringField("Ονομα")
    surname = StringField('Επώνυμο')
    fathers_name = StringField('Όνομα Πατρός')
    date_of_birth = DateField('Ημερομηνία Γεννήσεως')
    marital_status = SelectField("Οικογενειακή Κατάσταση", choices=[('other', ' '), ('single', 'Άγαμος'), ('married', 'Έγγαμος')])
    nationality = StringField('Εθνικότητα')
    occupation = StringField('Επάγγελμα')
    address_line_1 = StringField("Οδός")
    address_line_2 = StringField("Αριθμός")
    city = StringField("Πόλη")
    postalCode = StringField("Ταχυδρομικός Κωδικός")
    county = StringField("Νομός")
    home_phone = StringField("Σταθερό")
    mobile_phone = StringField('Κινητό')
    alternative_phone = StringField('Εναλλακτικό Τηλ.')
    email = StringField('E-mail')
    insurance = SelectField('Ασφάλιση', choices=[('unknown',' '),('eopy','ΕΟΠΥΥ'),('private','Ιδιωτική Ασφάλεια')])
    insurance_comment = TextAreaField()
    amka = StringField('ΑΜΚΑ')
    spouseName = StringField('Ονοματεπώνυμο')
    spouse_dob = DateField('Ημερομηνία Γεννήσεως')
    spouse_occupation = StringField('Επάγγελμα')

@app.route("/", methods=["GET","POST"])
def index():
    form = PersonalInfo()

    if form.validate_on_submit():
        session['first_name'] = form.first_name.data
        session['surname'] = form.surname.data
        session['fathers_name'] = form.fathers_name.data
        session['marital_status'] = form.marital_status.data
        session['insurance'] = form.insurance.data
        flash('The record has been created')
        return redirect(url_for('personaldetails'))
    return render_template ("index.html", form = form)

@app.route('/personaldetails')
def personaldetails():
    return render_template("personaldetails.html")

if __name__ == "__main__":
    app.run(debug=True)
