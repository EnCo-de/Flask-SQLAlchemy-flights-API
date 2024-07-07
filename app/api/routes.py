from app.api import bp
# from app.extensions import db
from app.models.flights import Flight
from flask import jsonify
from sqlalchemy import func # and_
from datetime import datetime


@bp.route('/')
def index():
    return {'api': '200 OK'}

@bp.route('permissions/<start>/<end>/', methods=['GET'])
def permissions(start=None, end=None):
    print("     from_date, to_date", start, end)
    from_date = datetime.strptime(start, "%Y-%m-%dT%H:%M")
    to_date = datetime.strptime(end, "%Y-%m-%dT%H:%M") # :%S.%f
    print(from_date, to_date)
    data = Flight.query.filter(Flight.sign_date>=from_date, Flight.sign_date<=to_date)
    print(data)
    # if from_date:
    #     data = Flight.query.filter_by(airoperator_name='airoperator_name')
    # else:
    #     data = Flight.query.all()
    
    # if isinstance(data, Flight):
    #     return data.jq()
    # return [ta.jq() for ta in data]
    return jsonify({"permissions": [each.to_json() for each in data]})


@bp.route('air-operators/<airoperator_name>/', methods=['GET'])
def airoperators(airoperator_name):
    # arrival_1_date_time
    # departure_1_date_time
    data = Flight.query.filter_by(airoperator_name=airoperator_name).filter(
            func.time(Flight.departure_1_date_time).between("01:00","07:00"), 
            func.time(Flight.arrival_1_date_time).between("01:00","07:00"))
    # print('\n\n', data)
    # if isinstance(data, Flight):
    #     return data.to_json()
    return [flight.to_json() for flight in data]

