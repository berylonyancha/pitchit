from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm,UpdateProfile,ReviewForm
from ..import db,photos
from ..models import User,Pitch,Review
from flask_login import login_required,current_user

@main.route('/')
def index():
    return render_template('index.html')

@main.route("/post",methods=['GET','POST'])
@login_required
def post():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category= form.category.data
        like=0
        dislike=0

        # Updated pitch instance
        new_pitch = Pitch(pitch_title=title,pitch_body=pitch,category=category,like=like,dislike=dislike,user=current_user)

        # save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('main.post'))

    title="Post your pitch"
    return render_template('post.html',title=title,pitch_form=form)