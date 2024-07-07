from app.api import bp
# from app.extensions import db
from app.models.flights import Flight
from flask import request, jsonify
from sqlalchemy import func # and_
from datetime import datetime


@bp.route('/')
def index():
    return {'api': '200 OK'}

@bp.route('flight_no/<string:flight_id>/', methods=['GET'])
def flight_no(flight_id):
    print(flight_id)
    flights = Flight.query.filter_by(flight_no=flight_id)
    return {'flights': [flight.to_json() for flight in flights]}
        
@bp.route('flights/<uuid:flight_id>/', methods=['GET'])
def flights(flight_id):
    flight = Flight.query.get_or_404(flight_id)
    return {'flights': flight.to_json()}
        
@bp.route('permissions/<start>/<end>/', methods=['GET'])
def permissions(start=None, end=None):
    print("     from_date, to_date", start, end)
    from_date = datetime.strptime(start, "%Y-%m-%dT%H:%M")
    to_date = datetime.strptime(end, "%Y-%m-%dT%H:%M") # :%S.%f
    print(from_date, to_date)
    data = Flight.query.filter(Flight.sign_date>=from_date, Flight.sign_date<=to_date)
    print(data)
    fields = ['arrival_1', 'flight_no', 'sign_date', 'departure_1', 'traffic_type', 'permission_no', 'airoperator_name', 'place_of_business', 'arrival_1_date_time', 'departure_1_date_time']
    return jsonify({"permissions": [each.to_json(fields) for each in data]})

@bp.route('locations/', methods=['GET'])
def locations():
    airports = ('EVN', # Zvartnots International Airport
                'LWN', # Gyumri Shirak Airport
                'Syunik')
    location = request.args.get('q')
    arrival_1 = Flight.arrival_1.in_(airports)
    departure_1 = Flight.departure_1.in_(airports)
    match location:
        case 'in':
            criterion = (arrival_1 & departure_1)
        case 'from':
            criterion = (~arrival_1 & departure_1)
        case 'to':
            criterion = (arrival_1 & ~departure_1)
        case _:
            return {"locations/?q=": ['in','from','to']}
    data = Flight.query.filter(criterion)
    print(data)
    return jsonify({"flights": [each.to_json() for each in data]})

@bp.route('air-operators/<airoperator_name>/', methods=['GET'])
def airoperators(airoperator_name):
    # arrival_1_date_time
    # departure_1_date_time
    data = Flight.query.filter_by(airoperator_name=airoperator_name).filter(
            func.time(Flight.departure_1_date_time).between("01:00","07:00"), 
            func.time(Flight.arrival_1_date_time).between("01:00","07:00"))
    return [flight.to_json() for flight in data]