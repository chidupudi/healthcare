from flask import Blueprint, request, jsonify
from app import db
from bson.objectid import ObjectId

appointment_bp = Blueprint('appointment_scheduling', __name__)

@appointment_bp.route('/appointments', methods=['POST'])
def schedule_appointment():
    data = request.json
    # Insert appointment into MongoDB
    db.appointments.insert_one(data)
    return jsonify({"message": "Appointment scheduled successfully!"}), 201

@appointment_bp.route('/appointments/<appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = db.appointments.find_one({"_id": ObjectId(appointment_id)})
    if appointment:
        return jsonify(appointment), 200
    return jsonify({"message": "Appointment not found!"}), 404
