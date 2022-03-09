from app.models import NewPitch
from flask import render_template, request, redirect, url_for
from . import main
from flask_login import login_required, current_user
from .forms import PitchForm
from .. import db
import markdown2

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = "Pitch"

    return render_template('index.html', title=title)



@main.route('/userpage', methods = ['GET', 'POST'])
@login_required
def userpage():
    '''
    View userpage page function that returns the userpage page and its data
    ''' 
    pitches_body=NewPitch.query.all()
    # form = PitchForm()
    # if form.validate_on_submit():


    #     uppitch = NewPitch( title = form.pitchtitle.data, pitch = form.pitchtitle.data, category = form.category.data, author = form.author.data)

    #     db.session.add(uppitch)
    #     db.session.commit()

    #     return redirect(url_for('main.index'))

    return render_template('userpage.html', pitches_body = pitches_body)


@main.route('/createpitch', methods = ['GET', 'POST'])
@login_required
def createpitch():
    '''
    View userpage page function that returns the userpage page and its data
    ''' 
    form = PitchForm()
    if form.validate_on_submit():


        uppitch = NewPitch( pitchtitle = form.title.data, mypitch = form.name.data, category = form.category.data, author = form.author.data)

        db.session.add(uppitch)
        db.session.commit()

        return redirect(url_for('main.userpage'))

    return render_template('createpitch.html', pitch_form = form)
