from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database Configuration
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:657300@localhost/GARYH0702'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Health Record Model
class HealthRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    record_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create DB and tables before the first request
@app.before_first_request
def create_tables():
    db.create_all()

# Add a health record
@app.route('/record', methods=['POST'])
def add_record():
    data = request.get_json()

    new_record = HealthRecord(
        user_id=data['user_id'],
        record_type=data['record_type'],
        description=data['description']
    )

    db.session.add(new_record)
    db.session.commit()

    return jsonify({'message': 'Health record created successfully'}), 201

# Get all health records for a user
@app.route('/records/<int:user_id>', methods=['GET'])
def get_records(user_id):
    records = HealthRecord.query.filter_by(user_id=user_id).all()
    output = []

    for record in records:
        record_data = {'id': record.id, 'user_id': record.user_id, 'record_type': record.record_type, 'description': record.description, 'created_at': record.created_at}
        output.append(record_data)

    return jsonify({'records': output})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
