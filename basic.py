from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField

app = Flask(__name__)

app.config["SECRET_KEY"] = "mySecretKey"

class CustomerInfoForm(FlaskForm):
    name = StringField("Ονοματεπώνυμο:")
    submit = SubmitField("Υποβολή")

@app.route("/", methods=["GET","POST"])
def index():
    name = False

    form = CustomerInfoForm()

    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template ("index.html", form = form, name = name)

if __name__ == "__main__":
    app.run(debug=True)
