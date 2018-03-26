from flask import Blueprint, render_template, request
from primeapp import primechecker
bp = Blueprint( __name__, __name__,template_folder='templates')

@bp.route('/', methods =['POST', 'GET'])


def show():
    if request.method == 'POST':
        if request.form.get('createnote'):
            text = request.form.get('notetext')
            primetext = primechecker.isPrime(text)
            return render_template('index.html', text = primetext)
    return render_template('index.html')