# ZipAirlines

# Project Requirements
python3 and virtualenv

# Running the Project
virtualenv venv
source venv/bin/activate
cd ZipAirlines
python manage.py migrate
python manage.py runserver

# REST API urls
http://127.0.0.1:8000/api/v1/airplanes/

# POST Data
{
"airplanes": [
  { 
   "id": 1,
   "passengers": 12
  },
  {
   "id": 2,
   "passengers": 20
  }
 ]
}

# Response Data

{
    "airplanes": [
        {
            "id": 1,
            "passengers": 12,
            "tank_capacity": 200,
            "per_passenger_consumption": 0.024,
            "per_minute_fuel_consumption": 0.824,
            "max_fly_minutes": 242.7184,
            "fuel_required": 1.088
        },
        {
            "id": 2,
            "passengers": 20,
            "tank_capacity": 400,
            "per_passenger_consumption": 0.04,
            "per_minute_fuel_consumption": 1.64,
            "max_fly_minutes": 243.9024,
            "fuel_required": 2.4
        }
    ]
}

# Running the Tests
python manage.py test
