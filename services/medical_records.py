from flask import Blueprint, request, jsonify
from app import db
from bson.objectid import ObjectId

medical_bp = Blueprint('medical_record', __name__)

@medical_bp.route('/medical_records', methods=['POST'])
def add_medical_record():
    data = request.json
    # Insert medical record into MongoDB
    db.medical_records.insert_one(data)
    return jsonify({"message": "Medical record added successfully!"}), 201

@medical_bp.route('/medical_records/<record_id>', methods=['GET'])
def get_medical_record(record_id):
    record = db.medical_records.find_one({"_id": ObjectId(record_id)})
    if record:
        return jsonify(record), 200
    return jsonify({"message": "Medical record not found!"}), 404
