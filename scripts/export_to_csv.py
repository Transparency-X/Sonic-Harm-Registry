import json
import csv
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
with open(os.path.join(DATA_DIR, 'registry.json'), 'r') as f:
    registry = json.load(f)

with open(os.path.join(DATA_DIR, 'registry.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['modality', 'harmType', 'definition', 'legalBasis', 'requirements', 'source'])
    writer.writeheader()
    writer.writerows(registry)
print("Exported to registry.csv")
