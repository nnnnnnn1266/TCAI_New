# TCAI Project (Turtle Care AI)

A simple FastAPI + frontend demo for turtle-care question answering.

## Features

- `POST /ask` endpoint for QA
- `GET /health` endpoint for health checks
- Static frontend served by FastAPI
- Mock inference layer designed to be replaced by a fine-tuned LLM later

## Project Structure

```
TCAI-project/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   └── inference.py
│   └── models/
│       └── schemas.py
├── frontend/
│   └── index.html
├── data/
├── docs/
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000> and ask a question.

## API Example

`POST /ask`

Request:

```json
{
  "question": "Why do turtles bask?"
}
```

Response:

```json
{
  "answer": "Turtles bask to regulate body temperature and absorb UVB light for shell and bone health."
}
```
