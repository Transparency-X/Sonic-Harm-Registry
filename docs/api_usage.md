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
```

Response: side-by-side comparison object.

```

---

## 3. Data Files

### `data/registry.json`
```json
[
  {
    "modality": "acoustic",
    "harmType": "harassment",
    "definition": "Use of sound to create a hostile or intimidating environment (workplace or home).",
    "legalBasis": "UK Equality Act 2010, s.26; US Title VII",
    "requirements": "Unwanted conduct related to protected characteristic; violates dignity.",
    "source": "Carozzi v University of Hertfordshire [2024] EAT"
  },
  {
    "modality": "acoustic",
    "harmType": "violence",
    "definition": "Violence exercised by means of sound; causes unease, helplessness, or physical harm.",
    "legalBasis": "WHO noise guidelines (non-binding), ASOLOFAL definition",
    "requirements": "Persistent unwanted sound exceeding WHO night limits (55 dBA).",
    "source": "Miyara (2000)"
  },
  {
    "modality": "acoustic",
    "harmType": "surveillance",
    "definition": "Criminal‑legal interception of speech within private spaces.",
    "legalBasis": "German StPO §100c, ECHR Art.8",
    "requirements": "Judicial warrant, strict necessity.",
    "source": "German Code of Criminal Procedure"
  },
  {
    "modality": "acoustic",
    "harmType": "monitoring",
    "definition": "Continuous measurement of ambient noise for regulatory compliance.",
    "legalBasis": "EU Directive 2002/49/EC",
    "requirements": "Noise mapping, action plans if >55 dBA night.",
    "source": "END 2002/49/EC"
  },
  {
    "modality": "acoustic",
    "harmType": "abuse",
    "definition": "Harmful misuse of sound technology (e.g., acoustic harassment devices).",
    "legalBasis": "Marine Mammal Protection Act (US), Animal Welfare Act",
    "requirements": "Prohibition of auditory injury to non‑target species.",
    "source": "MMPA 16 U.S.C. § 1361"
  },
  {
    "modality": "voice",
    "harmType": "harassment",
    "definition": "Verbal abuse related to protected characteristics (race, accent, gender).",
    "legalBasis": "UK Equality Act 2010, s.26",
    "requirements": "Unwanted conduct violating dignity, irrespective of intent.",
    "source": "Carozzi v University of Hertfordshire [2024] EAT"
  },
  {
    "modality": "voice",
    "harmType": "violence",
    "definition": "Not commonly used; subsumed under acoustic violence.",
    "legalBasis": "N/A",
    "requirements": "N/A",
    "source": "See acoustic violence"
  },
  {
    "modality": "voice",
    "harmType": "surveillance",
    "definition": "Corporate/governmental monitoring of voice interactions for compliance.",
    "legalBasis": "MiFID II, HIPAA, GDPR",
    "requirements": "Transparency, data minimisation, legitimate purpose.",
    "source": "MiFID II Delegated Regulation (EU) 2017/565"
  },
  {
    "modality": "voice",
    "harmType": "monitoring",
    "definition": "Covered by voice surveillance; occupational voice monitoring not standard.",
    "legalBasis": "N/A",
    "requirements": "N/A",
    "source": ""
  },
  {
    "modality": "voice",
    "harmType": "abuse",
    "definition": "Medical misuse of one's voice causing physical injury (nodules, polyps).",
    "legalBasis": "WHO ICD-11 (clinical definition)",
    "requirements": "Repeated overuse, screaming, strained vocalisations.",
    "source": "ICD-11, chapter 12 (Voice disorders)"
  },
  {
    "modality": "audio",
    "harmType": "harassment",
    "definition": "Use of recorded or transmitted sound (explicit music, voicemails) to distress.",
    "legalBasis": "US Title VII (9th Circuit 2023)",
    "requirements": "Sexually graphic, violently misogynistic content pollutes workplace.",
    "source": "Doe v. Acme Corp (9th Cir. 2023)"
  },
  {
    "modality": "audio",
    "harmType": "violence",
    "definition": "Subsumed under acoustic violence.",
    "legalBasis": "N/A",
    "requirements": "N/A",
    "source": ""
  },
  {
    "modality": "audio",
    "harmType": "surveillance",
    "definition": "Surreptitious collection of sounds via hidden microphones.",
    "legalBasis": "GDPR Art.5, 9, 13; UK DPA 2018",
    "requirements": "DPIA, signage, no recording in private areas.",
    "source": "ICO Employment Practices Code"
  },
  {
    "modality": "audio",
    "harmType": "monitoring",
    "definition": "Employer use of recording devices at work; must be proportionate.",
    "legalBasis": "ICO Code, GDPR",
    "requirements": "Only rare circumstances; covert never in restrooms.",
    "source": "ICO Employment Practices Code (2011)"
  },
  {
    "modality": "audio",
    "harmType": "abuse",
    "definition": "Non‑consensual distribution of intimate audio recordings.",
    "legalBasis": "UK Amendment 72 (pending 2025)",
    "requirements": "Criminalises intimate audio without consent.",
    "source": "UK House of Lords Library, 2025"
  },
  {
    "modality": "sound",
    "harmType": "harassment",
    "definition": "Deliberate use of amplified sound as psychological weapon or torture.",
    "legalBasis": "UN CAT, IHL",
    "requirements": "Intentional infliction of severe mental suffering.",
    "source": "HRW report 2025 (Thai‑Cambodian border)"
  },
  {
    "modality": "sound",
    "harmType": "violence",
    "definition": "Covert use of sound as instrument of war, dominance, and control.",
    "legalBasis": "None (theoretical, but may breach Geneva Conventions)",
    "requirements": "Vibrational warfare, atmospheric occupation.",
    "source": "Ouzounian, The Trembling City (2026)"
  },
  {
    "modality": "sound",
    "harmType": "surveillance",
    "definition": "Passive monitoring of sound for security or intelligence.",
    "legalBasis": "National security classifications (e.g., SOSUS)",
    "requirements": "Typically exempt from civilian oversight.",
    "source": "US Navy SOSUS declassified documents"
  },
  {
    "modality": "sound",
    "harmType": "monitoring",
    "definition": "Neutral tracking of sound levels (dB) in workplace or residential areas.",
    "legalBasis": "OSHA 29 CFR 1910.95, EU Directive 2003/10/EC",
    "requirements": "Action value: 85 dBA 8‑hour TWA; upper limit 87 dBA.",
    "source": "OSHA noise standard"
  },
  {
    "modality": "sound",
    "harmType": "abuse",
    "definition": "See acoustic abuse.",
    "legalBasis": "N/A",
    "requirements": "N/A",
    "source": ""
  }
]
