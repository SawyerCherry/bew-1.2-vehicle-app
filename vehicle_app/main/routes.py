"""Import packages and modules."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from ..models import Manufacturer, Vehicle
from vehicle_app.main.forms import NewVehicleForm


from vehicle_app import app, db

main = Blueprint("main", __name__)



##########################################
#           Routes                       #
##########################################


@main.route('/')
def homepage():
    all_vehicles = Vehicle.query.all()
    return render_template('homepage.html', vehicle=all_vehicles)


@main.route('/new_vehicle', methods=['GET', 'POST'])
@login_required
def new_vehicle():
    form = NewVehicleForm()

    if form.validate_on_submit():
        new_vehicle = Vehicle(
            model=form.body.data,
            vin=date.today(),
            user=current_user
        )

        db.session.add(new_vehicle)
        db.session.commit()

        flash('Your Vehicle was created!')
        return redirect(url_for('main.homepage'))
    return render_template('new_vehicle.html', form=form)


@main.route('/edit_vehicle', methods=['GET', 'POST'])
@login_required
def edit_vehicle():
    form = NewVehicleForm()

    if form.validate_on_submit():
        new_vehicle = Vehicle(
            model=form.body.data,
            vin=date.today(),
            user=current_user
        )

        db.session.add(new_vehicle)
        db.session.commit()

        flash('Your Vehicle was created!')
        return redirect(url_for('main.homepage'))
    return render_template('new_vehic;e.html', form=form)