__author__ = 'g-rock'

from flask import Flask, render_template, request, flash, session
from form import ContactForm
from json2html import *


import pokitdok

app = Flask(__name__)

app.secret_key = '1i\xb3\xcd\x01R\x81\x89&1S,\t\xa3\xf7\xbej\xe1\xf8\xda\xdb\x87\xc8\xe4'


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
            html = json2html.convert(json=json_file)
            session['var'] = html
            return render_template('eligibility_results.html', json=json_file)

    elif request.method == 'GET':
        return render_template('form.html', form=form)

@app.route('/eligibility/summary')
def summary():
    html_summary = session.get('var', None)
    return render_template('full_summary.html', html=html_summary)


if __name__ == '__main__':
    app.run(debug=True)
