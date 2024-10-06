from flask import Blueprint, request, jsonify
from app import db
from bson.objectid import ObjectId

billing_bp = Blueprint('billing', __name__)


@billing_bp.route('/bills', methods=['POST'])
def create_bill():
    data = request.json
    # Insert billing record into MongoDB
    db.bills.insert_one(data)
    return jsonify({"message": "Bill created successfully!"}), 201

@billing_bp.route('/bills/<bill_id>', methods=['GET'])
def get_bill(bill_id):
    bill = db.bills.find_one({"_id": ObjectId(bill_id)})
    if bill:
        return jsonify(bill), 200
    return jsonify({"message": "Bill not found!"}), 404
