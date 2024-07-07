from flask import render_template
from app.main import bp
from app.models.flights import Flight, description
from sqlalchemy import func, desc

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/chart/')
def chart():
    flights = Flight.query.group_by(
        Flight.departure_1, Flight.arrival_1, 
        func.time(Flight.departure_1_date_time),
        func.time(Flight.arrival_1_date_time)
        ).order_by(desc(func.count())).limit(5)
    flights_chart = flights.add_columns(func.count())
    for flight, num in flights_chart: # this is correct
        print(flight.uuid, num)
    print()
    return render_template('chart.html', 
                           ths=description.values(),
                           flights=flights)