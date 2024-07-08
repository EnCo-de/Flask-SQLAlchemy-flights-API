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
    flights_table = flights.add_columns(func.count(), 
        func.time(Flight.departure_1_date_time),
        func.time(Flight.arrival_1_date_time))
    chart_data = []
    for flight, num, departure_1_time, arrival_1_time  in flights_table:
        chart_data.append((' '.join(map(str, [
            flight.departure_1, '-',
            flight.arrival_1,
            departure_1_time[:5], '-',
            arrival_1_time[:5]])), num))
    return render_template('chart.html', 
                           ths=description.values(),
                           flights=flights,
                           flights_table=flights_table,
                           chart_data=chart_data)