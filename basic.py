from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, DateTimeField, BooleanField, TextAreaField, SelectField

app = Flask(__name__)

app.config["SECRET_KEY"] = "mySecretKey"

class CustomerInfoForm(FlaskForm):
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
    insurance = SelectField('Ασφάλιση', choices=[('unknown',''),('eopy','ΕΟΠΥΥ'),('private','Ιδιωτική Ασφάλεια')])
    insurance_comment = TextAreaField()
    amka = StringField('ΑΜΚΑ')
    spouseName = StringField('Ονοματεπώνυμο')
    spouse_dob = DateField('Ημερομηνία Γεννήσεως')
    spouse_occupation = StringField('Επάγγελμα')

@app.route("/", methods=["GET","POST"])
def index():
    first_name = True
    surname = 'False'
    fathers_name = 'False'
    marital_status = 'False'

    form = CustomerInfoForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        # surname = form.surname.data
        # fathers_name = form.fathers_name.data
        # marital_status = form.marital_status.data
    return render_template ("index.html", form = form, first_name = first_name, surname = surname, fathers_name = fathers_name, marital_status = marital_status)

if __name__ == "__main__":
    app.run(debug=True)
