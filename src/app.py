from flask import Flask, render_template, jsonify, request
import json
import yaml
import os

app = Flask(__name__)

# Load data
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
with open(os.path.join(DATA_DIR, 'registry.json'), 'r') as f:
    registry = json.load(f)
with open(os.path.join(DATA_DIR, 'thresholds.yaml'), 'r') as f:
    thresholds = yaml.safe_load(f)

# Index registry by (modality, harmType) for fast lookup
term_index = {}
for term in registry:
    key = (term['modality'], term['harmType'])
    term_index[key] = term

@app.route('/')
def index():
    return render_template('index.html', modalities=['acoustic','voice','audio','sound'],
                           harm_types=['harassment','violence','surveillance','monitoring','abuse'])

@app.route('/api/terms', methods=['GET'])
def get_terms():
    modality = request.args.get('modality')
    harm_type = request.args.get('harmType')
    if modality and harm_type:
        key = (modality, harm_type)
        return jsonify(term_index.get(key, {}))
    elif modality:
        filtered = [t for t in registry if t['modality'] == modality]
        return jsonify(filtered)
    elif harm_type:
        filtered = [t for t in registry if t['harmType'] == harm_type]
        return jsonify(filtered)
    else:
        return jsonify(registry)

@app.route('/api/compare', methods=['POST'])
def compare_terms():
    data = request.get_json()
    term_ids = data.get('terms', [])
    results = []
    for term_id in term_ids:
        if '_' in term_id:
            mod, harm = term_id.split('_')
            key = (mod, harm)
            results.append(term_index.get(key, {}))
    return jsonify(results)

@app.route('/api/thresholds')
def get_thresholds():
    return jsonify(thresholds)

@app.route('/term/<modality>/<harmType>')
def term_detail(modality, harmType):
    key = (modality, harmType)
    term = term_index.get(key, {})
    return render_template('term_detail.html', term=term)

if __name__ == '__main__':
    app.run(debug=True)
