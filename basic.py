from flask import Flask, render_template, session, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DateTimeField, BooleanField, TextAreaField, SelectField

app = Flask(__name__)

app.config["SECRET_KEY"] = "mySecretKey"

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
