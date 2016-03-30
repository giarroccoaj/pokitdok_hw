__author__ = 'g-rock'

from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators
# import pokitdok

class ContactForm(Form):
    first_name = TextField("First Name:", [validators.DataRequired("Please enter a First Name.")])
    last_name = TextField("Last Name:", [validators.DataRequired("Please enter a Last Name.")])
    birth_date = TextField("Birth Date:", [validators.DataRequired("Please enter a Birth Date.")])
    id = TextField("ID:", [validators.DataRequired("Please enter a ID. ")])
    trading_partner_id = TextField("Trading Partner ID:",
                                   [validators.DataRequired("Please enter a Trading Partner Id.")])
    submit = SubmitField("Submit")
