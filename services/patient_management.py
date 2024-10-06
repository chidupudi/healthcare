from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from db import db  # Import db from db.py

patient_bp = Blueprint('patient_management', __name__)

@patient_bp.route('/patients', methods=['POST'])
def register_patient():
    data = request.json
    # Insert patient data into MongoDB
    db.patients.insert_one(data)
    return jsonify({"message": "Patient registered successfully!"}), 201

@patient_bp.route('/patients/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = db.patients.find_one({"_id": ObjectId(patient_id)})
    if patient:
        return jsonify(patient), 200
    return jsonify({"message": "Patient not found!"}), 404
