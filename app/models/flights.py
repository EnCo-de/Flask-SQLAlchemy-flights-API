from app.extensions import db


class Flight(db.Model):
    __tablename__ = 'flights'
    fields = ['uuid', 'created', 'task_id', 'arrival_1', 'flight_no', 'sign_date', 'departure_1', 'traffic_type', 'permission_no', 'airoperator_name', 'place_of_business', 'arrival_1_date_time', 'departure_1_date_time']
    
    # _id = db.Column(db.Integer)
    # title = db.Column(db.String(150))
    # content = db.Column(db.Text)
    uuid = db.Column(db.Uuid, primary_key=True) #                 ed137e40-fdd1-4c22-8844-69dfc6307299  ac3caede-1f31-44d6-aa44-921cb32f4211
    created = db.Column(db.String(20)) #                         2024-04-02 19:02:52.481000            2024-04-02 19:03:26.020000
    task_id = db.Column(db.Integer) #                    484                                   427
    arrival_1 = db.Column(db.String(3), nullable=False) #      EVN                                   SSH
    flight_no  = db.Column(db.String(20), nullable=False) #   FOE1207                               FIA7461
    sign_date = db.Column(db.String(20)) #                              2024-02-04 18:54:23                   2024-02-04 18:52:52
    departure_1 = db.Column(db.String(3), nullable=False) #    LCA                                   EVN
    traffic_type  = db.Column(db.String(20))             #  empty                              combined
    permission_no  = db.Column(db.String(20), nullable=False) #     ARM-20021                             ARM-20020
    airoperator_name = db.Column(db.String(20), nullable=False) #    Airoperator 1                         Airoperator 2
    place_of_business = db.Column(db.String(3), nullable=False) #    ROU                                   MDA
    arrival_1_date_time  = db.Column(db.String(20)) #                      2024-04-03 06:00:00                   2024-04-03 07:00:00
    departure_1_date_time  = db.Column(db.String(20)) #                    2024-04-03 04:00:00
    # arrival_1_date_time  = db.Column(db.DateTime(timezone=True)) #                      2024-04-03 06:00:00                   2024-04-03 07:00:00
    # departure_1_date_time  = db.Column(db.DateTime(timezone=True)) #                    2024-04-03 04:00:00


    def __repr__(self):
        return self.flight_no

    def to_json(self):
        return {field: str(getattr(self, field)) for field in self.fields}



'''>>> df.dtypes
    ['uuid', 'created', 'task_id', 'arrival_1', 'flight_no', 'sign_date', 'departure_1', 'traffic_type', 'permission_no', 'airoperator_name', 'place_of_business', 'arrival_1_date_time', 'departure_1_date_time']
uuid                             object
created                  datetime64[ns]
task_id                           int64
arrival_1                        object
flight_no                        object
sign_date                        object
departure_1                      object
traffic_type                     object
permission_no                    object
airoperator_name                 object
place_of_business                object
arrival_1_date_time      datetime64[ns]
departure_1_date_time    datetime64[ns]
dtype: object



uuid                   ed137e40-fdd1-4c22-8844-69dfc6307299  ac3caede-1f31-44d6-aa44-921cb32f4211
created                          2024-04-02 19:02:52.481000            2024-04-02 19:03:26.020000
task_id                                                 484                                   427
arrival_1                                               EVN                                   SSH
flight_no                                           FOE1207                               FIA7461
sign_date                               2024-02-04 18:54:23                   2024-02-04 18:52:52
departure_1                                             LCA                                   EVN
traffic_type                                          empty                              combined
permission_no                                     ARM-20021                             ARM-20020
airoperator_name                              Airoperator 1                         Airoperator 2
place_of_business                                       ROU                                   MDA
arrival_1_date_time                     2024-04-03 06:00:00                   2024-04-03 07:00:00
departure_1_date_time                   2024-04-03 04:00:00                   2024-04-03 04:00:00'''