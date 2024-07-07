from app.api import bp
# from app.extensions import db
from app.models.flights import Flight
from flask import jsonify
# from sqlalchemy import and_
from datetime import datetime


@bp.route('/')
def index():
    return {'api': '200 OK'}

@bp.route('air-operators/<airoperator_name>/', methods=['GET'])
def airoperators(airoperator_name=None):
    if airoperator_name:
        data = Flight.query.filter_by(airoperator_name=airoperator_name)
    else:
        data = Flight.query.all()
    print('\n\n', data)
    if isinstance(data, Flight):
        return data.to_json()
    return [flight.to_json() for flight in data]

@bp.route('permissions/<start>/<end>/', methods=['GET'])
def permissions(start=None, end=None):
    from_date = datetime.strptime(start, "%Y-%m-%d")
    to_date = datetime.strptime(end, "%Y-%m-%d")
    print(from_date, to_date)
    data = Flight.query.filter(Flight.sign_date>from_date, Flight.sign_date<to_date)
    print(data)
    # if from_date:
    #     data = Flight.query.filter_by(airoperator_name='airoperator_name')
    # else:
    #     data = Flight.query.all()
    
    # if isinstance(data, Flight):
    #     return data.jq()
    # return [ta.jq() for ta in data]
    return jsonify([each.to_json() for each in data])