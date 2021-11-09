from travel import myapp
from travel.forms import TopCities
from flask import render_template, flash, redirect
from travel.models import City 
from travel import db

@myapp.route("/", methods=['GET', 'POST'])
def home():
    name = 'An'
    title = 'Top Cities'
    form = TopCities()
    top_cities = ["Paris", "London", "Rome", "Tahiti"]
    if form.validate_on_submit():
        flash(f'Form Submitted for {form.city_name.data}!', category='success')
        return redirect('/home')

    return render_template("home.html", name = name, title = title, form = form, top_cities = top_cities)