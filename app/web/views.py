from flask import render_template, session, redirect, url_for, request
from . import main
from .forms import FlightsForm, CarForm, HotelForm
from mixpanel import Mixpanel

mp = Mixpanel('a841f59eae14574faf89743aa6da80d8')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/book/with/<partner>', methods=['GET', 'POST'])
def booking(partner):


    form = None
    partner_type = request.args.get('type')
    user_agent = request.user_agent


    mp.track('Browser Breakdown', 'Browser Breakdown',
             properties={'Partner': partner, 'Browser': user_agent.browser, 'Platform': user_agent.platform,
                         'Version': user_agent.version})


    # Initialise correct form
    if partner_type == 'flight':
        form = FlightsForm()
    elif partner_type == 'car':
        form = CarForm()
    elif partner_type == 'hotel':
        form = HotelForm()

    if form.validate_on_submit():
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('main.confirmation', partner=partner))

    mp.track('Page Load', 'Booking Form Loaded', properties={'Partner': partner, 'Vertical': partner_type})
    return render_template('booking.html', partner=partner, form=form)

@main.route('/success/<partner>')
def confirmation(partner):
    mp.track('Page Load', 'Confirmation Page', properties={'Partner': partner})
    return render_template('handover.html', name=session.get('name'))

