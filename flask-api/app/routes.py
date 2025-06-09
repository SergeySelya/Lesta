from flask import Blueprint, request, jsonify
from .models import Result
from .extensions import db

main = Blueprint('main', __name__)

@main.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    name = data.get('name')
    score = data.get('score')

    if not name or not isinstance(score, int):
        return jsonify({'error': 'Invalid data'}), 400

    result = Result(name=name, score=score)
    db.session.add(result)
    db.session.commit()

    return jsonify({'message': 'Data saved'}), 201

@main.route('/results', methods=['GET'])
def get_results():
    results = Result.query.all()
    return jsonify([
        {
            'id': r.id,
            'name': r.name,
            'score': r.score,
            'timestamp': r.timestamp.isoformat() if r.timestamp else None
        }
        for r in results
    ])

@main.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'ok'})
