# Separate module for API routes (used by app.py)
from flask import Blueprint, jsonify, request
import json
import os

terms_bp = Blueprint('terms', __name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'registry.json')

@terms_bp.route('/terms', methods=['GET'])
def list_terms():
    with open(DATA_PATH, 'r') as f:
        registry = json.load(f)
    modality = request.args.get('modality')
    harm = request.args.get('harmType')
    if modality and harm:
        result = [t for t in registry if t['modality'] == modality and t['harmType'] == harm]
    elif modality:
        result = [t for t in registry if t['modality'] == modality]
    elif harm:
        result = [t for t in registry if t['harmType'] == harm]
    else:
        result = registry
    return jsonify(result)
