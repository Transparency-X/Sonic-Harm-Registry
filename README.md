# Sonic Harm Registry (SHR)

[![License: CC BY‑NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Status: Alpha](https://img.shields.io/badge/status-alpha-orange)](https://github.com/yourusername/sonic-harm-registry)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

**Centralising definitions, legal standards, and international case law for acoustic harassment, sonic violence, voice surveillance, audio abuse, and all sound‑based harms.**

---

## 📖 Overview

The **Sonic Harm Registry (SHR)** is the first open‑source knowledge base dedicated to classifying, comparing, and legally contextualising terms where **sound / acoustic / voice / audio** intersect with **harassment, violence, surveillance, monitoring, and abuse**.

Based on a systematic review of international treaties (UN Convention against Torture, GDPR, ECHR), national laws (US Civil Rights Act, UK Equality Act, German criminal procedure codes), and cutting‑edge scholarship (Ouzounian 2026, Miyara 1997/2000), SHR provides:

- A **dynamic grid** of 4 modalities × 5 harm types (20 core terms)
- **Legal citations, jurisdiction maps, and burden‑of‑proof notes** for each term
- A **machine‑readable JSON/CSV export** for researchers, activists, and legal tech
- **Cross‑references** to related concepts (noise pollution, acoustic ecology, whistleblower protection)

SHR is not a static report – it is a living registry, updated as new laws, court rulings, and scholarly definitions emerge.

### Why this matters

- **Sound is a weapon:** from acoustic harassment devices (AHDs) to vibrational warfare, sonic tools are increasingly used to intimidate, torture, and surveil.
- **Law lags behind technology:** while image‑based abuse is criminalising, audio‑based abuse (e.g. non‑consensual intimate recordings) remains a legal grey zone in most jurisdictions.
- **Terminology is fragmented:** “acoustic violence”, “sound harassment”, “voice surveillance” – the same phenomenon may be called different things across disciplines, hindering advocacy and enforcement.

SHR bridges these gaps.

---

## 📁 Project Directory Structure

The repository is organised for clarity between documentation, data, code, and outputs from prior research.

```

sonic-harm-registry/
├── README.md                         # This file
├── CONTRIBUTING.md                   # Guidelines for contributors
├── LICENSE                           # CC BY-NC 4.0 full text
├── requirements.txt                  # Python dependencies (Flask, pandas, etc.)
├── setup.py                          # Package installation script
│
├── docs/                             # All human‑readable documentation
│   ├── research_report.md            # Full comparative report (grid + citations + source references)
│   ├── legal_sources.bib             # BibTeX file with all 50+ citations
│   ├── jurisdiction_notes/           # Country‑specific legal analyses
│   │   ├── eu.md
│   │   ├── uk.md
│   │   ├── us.md
│   │   └── germany.md
│   └── api_usage.md                  # How to query the REST API
│
├── data/                             # Structured term definitions
│   ├── registry.json                 # Master JSON array of all 20 terms (modality × harm type)
│   ├── registry.csv                  # Same data as CSV for spreadsheet users
│   ├── thresholds.yaml               # Decibel limits, time‑weighted averages, legal thresholds
│   └── sources.json                  # Mapping from citation keys to full metadata
│
├── src/                              # Source code
│   ├── app.py                        # Flask web application (grid viewer + API)
│   ├── api/                          # REST API endpoints
│   │   ├── terms.py                  # GET /terms, GET /terms/{modality}/{harm}
│   │   └── compare.py                # POST /compare
│   ├── static/                       # CSS, JS, images
│   │   ├── grid.css
│   │   ├── grid.js
│   │   └── assets/                   # Banner, icons
│   └── templates/                    # Jinja2 HTML templates
│       ├── index.html                # Homepage with interactive grid
│       ├── term_detail.html          # Individual term page
│       └── compare.html              # Side‑by‑side comparison tool
│
├── notebooks/                        # Jupyter notebooks for data analysis
│   ├── generate_grid_from_report.ipynb   # Parsed the research report to create registry.json
│   └── jurisdiction_coverage.ipynb       # Maps which terms are recognised per country
│
├── tests/                            # Unit tests for API and data integrity
│   ├── test_registry.py
│   └── test_api.py
│
└── scripts/                          # Utility scripts
├── export_to_csv.py              # Converts registry.json → registry.csv
├── validate_citations.py         # Checks that every source in registry.json exists in sources.json
└── update_from_courtlistener.py  # Scrapes new rulings (future feature)

```

**Integration of previous outputs:**

- `docs/research_report.md` – Contains the full comparative grid (acoustic/voice/audio/sound × harassment/violence/surveillance/monitoring/abuse) with extensive citations and international legal requirements. This is the foundational document for the entire registry.
- `data/registry.json` – Programmatically generated from the research report using `notebooks/generate_grid_from_report.ipynb`. Each cell of the grid becomes a JSON object with `modality`, `harmType`, `definition`, `legalBasis`, `requirements`, `source`.
- `data/registry.csv` – Same data in tabular format, mirroring the grid rows and columns for easy import into Excel or legal databases.

---

## ✨ Features

| Feature | Description |
| :------ | :---------- |
| **📊 Interactive Grid** | Browse the 4×5 matrix (Acoustic / Voice / Audio / Sound × Harassment / Violence / Surveillance / Monitoring / Abuse). Each cell contains a definition, legal basis, key requirements, and at least one primary source citation. |
| **🌍 Jurisdiction Mapping** | Select any country or region (EU, US, UK, ASEAN, etc.) to see which terms are legally recognised, with pending legislation highlighted. |
| **📚 Citation Database** | Full bibliographic records for over 50 sources – court cases (EAT, 9th Circuit), directives (EU 2002/49/EC), regulations (GDPR, MiFID II), and academic papers. Click through to the original text. |
| **📎 API Access** | RESTful API (JSON) to retrieve term definitions, legal thresholds, and cross‑references. Perfect for legal tech apps or compliance checklists. |
| **🧾 Evidence Templates** | Download printable templates for documenting acoustic harassment (decibel logs, witness statements) or audio surveillance (device fingerprints). |
| **🔍 Term Comparison Tool** | Select two or more terms (e.g. “sound harassment” vs. “acoustic violence”) to generate a side‑by‑side comparison of legal status, required evidence, and typical remedies. |
| **📢 Community Reports** | Anonymised, moderated submissions of real‑world incidents (no identifying data) to help identify emerging patterns – e.g. use of loudspeakers as torture in border disputes. |

---

## 🗺️ Roadmap of Future Features

### Q3–Q4 2026 (Alpha → Beta)

- **Mobile‑friendly grid** – fully responsive design for field researchers.
- **Offline mode** – download the entire registry as a static HTML/JSON bundle.
- **Multilingual interface** – pilot languages: Spanish, French, German, Arabic (reflecting regions with documented acoustic violence cases).
- **Integration with noise monitoring hardware** – allow users to upload anonymised dB(A) data that automatically triggers a term suggestion (e.g. if levels exceed WHO night limits, flag “acoustic harassment” potential).

### 2027

- **Machine learning classifier** – train a model on legal texts and incident reports to suggest the most appropriate SHR term given a free‑text description (e.g. “my neighbour plays ultra‑low frequency tones at 3am” → sound harassment / acoustic violence).
- **Legal alerts bot** – subscribe to RSS feeds of new court rulings (via CourtListener, EUR‑Lex) that mention SHR terms; push notifications to registered users.
- **Visual evidence toolkit** – spectrogram and waveform generator to help users visualise acoustic abuse (e.g. rhythmic bursts typical of AHDs).
- **Jurisdiction coverage expansion** – add India, Brazil, South Africa, Japan, and Mexico with local legal analyses.

### 2028 and beyond

- **Decentralised credential registry** – use verifiable credentials (W3C standard) to let victims securely share evidence with lawyers without exposing raw audio.
- **UN treaty body integration** – automatically map incident reports to reporting guidelines for CAT, ICERD, or CEDAW, enabling civil society shadow reports.
- **Acoustic ecology module** – expand beyond harm to include rights to quiet, soundscape preservation, and indigenous sonic sovereignty.

---

## 🚀 Getting Started

### For users (browsing the registry)
Visit **[https://sonicharmregistry.org](https://sonicharmregistry.org)** (placeholder – when live) or clone and run locally:

```bash
git clone https://github.com/yourusername/sonic-harm-registry.git
cd sonic-harm-registry
pip install -r requirements.txt
python src/app.py
```

Then open http://localhost:5000 in your browser.

For contributors

Read CONTRIBUTING.md (coming soon). We welcome:

· Legal researchers (update citations, flag new cases)
· UX designers (improve grid accessibility)
· Developers (API endpoints, offline sync)
· Translators (localise term definitions)

Data format example

All term definitions are stored in data/registry.json. Example entry:

```json
{
  "modality": "acoustic",
  "harmType": "harassment",
  "definition": "Use of sound to create a hostile or intimidating environment...",
  "legalBasis": "UK Equality Act 2010, s.26",
  "requirements": "Unwanted conduct related to protected characteristic",
  "source": "Carozzi v University of Hertfordshire [2024] EAT"
}
```

---

📄 License

This work is licensed under a Creative Commons Attribution‑NonCommercial 4.0 International License – free to share and adapt for non‑commercial purposes, with attribution. Commercial use (e.g. proprietary legal tech products) requires explicit permission.

---

🙏 Acknowledgements

· Dr. Federico Miyara (Acoustic Violence definition, 1997/2000)
· Prof. Gascia Ouzounian, The Trembling City (MIT Press, 2026)
· Human Rights Watch (2025 border loudspeaker report)
· UK House of Lords Library (Amendment 72 on audio abuse)
· All contributors to the open‑source acoustic justice movement

---

📬 Contact

For questions, collaboration, or to report a missing legal source:
registry@sonicharm.org | Open an issue

“Silence is not the absence of sound, but the presence of justice.”
