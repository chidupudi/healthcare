from flask import Blueprint, request, jsonify
from app import db
from bson.objectid import ObjectId

prescription_bp = Blueprint('prescription', __name__)

@prescription_bp.route('/prescriptions', methods=['POST'])
def create_prescription():
    data = request.json
    # Insert prescription into MongoDB
    db.prescriptions.insert_one(data)
    return jsonify({"message": "Prescription created successfully!"}), 201

@prescription_bp.route('/prescriptions/<prescription_id>', methods=['GET'])
def get_prescription(prescription_id):
    prescription = db.prescriptions.find_one({"_id": ObjectId(prescription_id)})
    if prescription:
        return jsonify(prescription), 200
    return jsonify({"message": "Prescription not found!"}), 404
