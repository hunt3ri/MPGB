from flask import render_template
from . import main
from mixpanel import Mixpanel

mp = Mixpanel('a841f59eae14574faf89743aa6da80d8')


@main.app_errorhandler(404)
def page_not_found(e):
    #mp.track('Errors', 'Errors', properties={'ErrorType': '404'})
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    #mp.track('Errors', 'Errors', properties={'ErrorType': '500'})
    return render_template('500.html'), 500

