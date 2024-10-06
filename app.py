from flask import Flask
from db import db  # Import db from db.py
from services.patient_management import patient_bp
from services.appointment_scheduling import appointment_bp
from services.medical_records import medical_bp
from services.billing import billing_bp
from services.prescription import prescription_bp

app = Flask(__name__)

# Register Blueprints for all services
app.register_blueprint(patient_bp, url_prefix='/api')
app.register_blueprint(appointment_bp, url_prefix='/api')
app.register_blueprint(medical_bp, url_prefix='/api')
app.register_blueprint(billing_bp, url_prefix='/api')
app.register_blueprint(prescription_bp, url_prefix='/api')

@app.route('/')
def home():
    return "Welcome to the Healthcare Management System!"

if __name__ == "__main__":
    app.run(debug=True)
