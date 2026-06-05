# API Usage

Base URL: `https://api.sonicharmregistry.org/v1`

## Endpoints

### `GET /terms`
Returns all 20 terms.

**Query params:**
- `modality` (acoustic, voice, audio, sound)
- `harmType` (harassment, violence, surveillance, monitoring, abuse)

Example: `/terms?modality=acoustic&harmType=violence`

### `POST /compare`
Compare two or more terms.

Request body:
```json
{
  "terms": ["acoustic_harassment", "sound_harassment"]
}
