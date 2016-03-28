__author__ = 'g-rock'

from flask import Flask, render_template, request, flash
from form import ContactForm
from json2html import *

import pokitdok

app = Flask(__name__)

app.secret_key = 'cant wait for dinner'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/eligibility', methods=['GET', 'POST'])
def eligibility():
    form = ContactForm()

    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required.')
            return render_template('form.html', form=form)
        else:
            pd = pokitdok.api.connect('uXEDs08GoIPr8uSju26s', 'BJFFLO708p09VmkfjxgM0cdLDKhma3t4cUAgEnkq')
            json_file = pd.eligibility({
                "member": {
                    "birth_date": form.birth_date.data,
                    "first_name": form.first_name.data,
                    "last_name": form.last_name.data,
                    "id": form.id.data
                },
                "trading_partner_id": form.trading_partner_id.data
            })

            return render_template('eligibility_results.html', json=json_file)

    elif request.method == 'GET':
        return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
