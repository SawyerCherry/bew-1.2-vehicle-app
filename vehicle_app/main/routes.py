"""Import packages and modules."""
from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date, datetime
from ..models import Manufacturer, Vehicle
from vehicle_app.main.forms import VehicleForm, ManufacturerForm


from vehicle_app import app, db

main = Blueprint("main", __name__)



##########################################
#           Routes                       #
##########################################


@main.route('/')
def homepage():
    all_vehicles = Vehicle.query.all()
    return render_template('homepage.html', vehicle=all_vehicles)


@main.route('/create_vehicle', methods=['GET', 'POST'])
@login_required
def new_vehicle():
    form = VehicleForm()

    if form.validate_on_submit():
        new_vehicle = Vehicle(
            manufacturer=form.manufacturer.data,
            model=form.model.data,
            vin=form.vin.data
        )

        db.session.add(new_vehicle)
        db.session.commit()

        flash('Your Vehicle was created!')
        return redirect(url_for('main.homepage'))
    return render_template('new_vehicle.html', form=form)

@main.route('/create_manufacturer', methods=['GET', 'POST'])
@login_required
def create_manufacturer():
    form = ManufacturerForm()
    if form.validate_on_submit():
        new_manufacturer = Manufacturer(
            name=form.name.data,
        )
        db.session.add(new_manufacturer)
        db.session.commit()

        flash('New Manufacturer added successfully.')
        return redirect(url_for('.homepage'))
    
    # if form was not valid, or was not submitted yet
    return render_template('new_manufacturer.html', form=form)


@main.route('/vehicle/<vehicle_id>', methods=['GET', 'POST'])
def vehicle_detail(book_id):
    vehicle = Vehicle.query.get(vehicle_id)
    form = BookForm(obj=book)
    
    # if form was submitted and contained no errors
    if form.validate_on_submit():
        vehicle.title = form.title.data
        vehicle.publish_date = form.publish_date.data
        vehicle.author = form.author.data
        

        db.session.commit()

        flash('Vehicle was updated successfully.')
        return redirect(url_for('main.vehicle_detail', book_id=book_id))

    return render_template('vehicle_detail.html', book=book, form=form)