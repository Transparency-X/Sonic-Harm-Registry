import json
import os
import pytest

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'registry.json')

def test_registry_complete():
    with open(DATA_PATH, 'r') as f:
        registry = json.load(f)
    expected_modalities = ['acoustic', 'voice', 'audio', 'sound']
    expected_harms = ['harassment', 'violence', 'surveillance', 'monitoring', 'abuse']
    keys = {(item['modality'], item['harmType']) for item in registry}
    for mod in expected_modalities:
        for harm in expected_harms:
            assert (mod, harm) in keys, f"Missing {mod}_{harm}"
