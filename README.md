# Golf Caddie Agent

A personal golf strategy assistant built with FastAPI, SQLite, and Python.

The aim of this project is to build towards an agentic AI caddie that can give personalised golf recommendations using player memory, course context, weather data, and eventually LLM-based reasoning.

At this stage, the project includes a working backend API, persistent player profile memory, and a recommendation endpoint that uses stored player data to generate basic golf strategy advice.

## Project Goals

This project is designed to demonstrate core agentic AI concepts in a practical and personal domain:

* Persistent memory
* Tool-based context gathering
* Structured API design
* Personalised recommendations
* Future LLM reasoning
* Future external API integration

The long-term goal is for the caddie to answer questions such as:

> “I’m playing a narrow 390-yard par 4 with trees left. What should I hit?”

And respond using information such as:

* Player handicap
* Club distances
* Common miss
* Current improvement focus
* Hole yardage
* Hazards
* Weather conditions
* Previous shot history

## Current Features

### FastAPI Backend

The app exposes a local API using FastAPI.

Current endpoints include:

| Method   | Endpoint          | Purpose                                 |
| -------- | ----------------- | --------------------------------------- |
| `GET`    | `/`               | Root API check                          |
| `GET`    | `/health`         | Health check                            |
| `POST`   | `/recommendation` | Generate a golf strategy recommendation |
| `POST`   | `/player-profile` | Create a player profile                 |
| `GET`    | `/player-profile` | Read the current player profile         |
| `PUT`    | `/player-profile` | Update the current player profile       |
| `DELETE` | `/player-profile` | Delete the current player profile       |

### Player Profile Memory

The app uses SQLite and SQLAlchemy to persist a player profile.

The player profile currently stores:

* Name
* Handicap
* Driver distance
* 7 iron distance
* Common miss
* Current improvement focus

This gives the recommendation endpoint a basic memory layer.

### Recommendation Engine

The recommendation endpoint currently uses:

* Hole input from the user
* Stored player profile data
* Basic weather context from a placeholder weather tool
* Rule-based strategy logic

The recommendation logic is intentionally simple for now. The purpose is to establish the backend structure before adding LLM reasoning.

## Tech Stack

* Python
* FastAPI
* Uvicorn
* SQLite
* SQLAlchemy
* Pydantic

## Project Structure

```text
Golf-Caddy/
│
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── tools.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the repository

```powershell
git clone <your-repo-url>
cd Golf-Caddy
```

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

You should see `(.venv)` at the start of your terminal prompt.

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Run the app

```powershell
uvicorn app.main:app --reload
```

The API should now be running at:

```text
http://127.0.0.1:8000
```

FastAPI docs are available at:

```text
http://127.0.0.1:8000/docs
```

## Example Usage

### Create a Player Profile

`POST /player-profile`

```json
{
  "name": "Oliver",
  "handicap": 28,
  "driver_distance": 210,
  "seven_iron_distance": 135,
  "common_miss": "left",
  "current_focus": "smooth tempo and avoiding pulls"
}
```

### Get the Current Player Profile

`GET /player-profile`

Example response:

```json
{
  "id": 1,
  "name": "Oliver",
  "handicap": 28,
  "driver_distance": 210,
  "seven_iron_distance": 135,
  "common_miss": "left",
  "current_focus": "smooth tempo and avoiding pulls"
}
```

### Update the Player Profile

`PUT /player-profile`

```json
{
  "name": "Oliver",
  "handicap": 26,
  "driver_distance": 215,
  "seven_iron_distance": 140,
  "common_miss": "left",
  "current_focus": "controlled tempo and keeping the ball in play"
}
```

### Delete the Player Profile

`DELETE /player-profile`

Example response:

```json
{
  "message": "Player profile deleted successfully."
}
```

### Generate a Recommendation

`POST /recommendation`

```json
{
  "course_name": "Richmond Park",
  "hole_number": 4,
  "tee_name": "Yellow",
  "yardage": 390,
  "par": 4,
  "stroke_index": 5,
  "fairway_width": "narrow",
  "hazards": "trees left, bunker right",
  "notes": "The green is slightly raised."
}
```

Example response:

```json
{
  "recommendation": "Take less than driver and aim for the safest part of the fairway.",
  "reasoning": "This par 4 is not especially long, so position may be more valuable than maximum distance. The fairway is narrow, so accuracy is more valuable than distance. Your current common miss is left, so avoid aiming too close to trouble on the left side. The wind is significant at around 15 mph, so club selection and shot shape need extra caution. The wind is moving left to right, which may exaggerate shots that start or curve that way. Dry conditions may allow more rollout, so a shorter club from the tee may still leave a manageable approach. Important hazards to consider: trees left, bunker right. This is one of the harder holes on the course, so a bogey-friendly strategy is sensible. Additional notes: The green is slightly raised. Your current improvement focus is: controlled tempo and keeping the ball in play.",
  "confidence": "medium"
}
```

## Current Behaviour Notes

A player profile must exist before a recommendation can be generated.

If no player profile exists, the recommendation endpoint returns a low-confidence response asking the user to create a profile first.

This is intentional. The recommendation tool reads memory, but it does not create memory automatically.

## Roadmap

### Near-Term

* Refactor routes out of `main.py`
* Add dedicated routers for recommendations and player profiles
* Add a service layer for player profile database logic
* Add shot history and round history tables
* Make recommendations use recent shot tendencies

### Agentic AI Improvements

* Add OpenAI API integration
* Add LLM-based recommendation reasoning
* Add structured model outputs
* Allow the model to use tools such as:

  * player profile lookup
  * shot history lookup
  * weather lookup
  * course data lookup
* Add confidence scoring and explanation quality checks

### External API Integrations

* Add real weather API data
* Investigate golf course APIs for:

  * course lookup
  * scorecards
  * tee sets
  * hole yardages
  * par
  * stroke index
* Keep external API responses behind adapter functions so the app is not tightly coupled to one provider

### Future Product Ideas

* Personal shot history dashboard
* Club recommendation engine
* Course strategy planner
* Round review assistant
* Frontend interface
* Visual hole strategy map

## Why This Project Exists

This project is intended to build and demonstrate an understanding of agentic AI through a practical golf use case.

Rather than starting with a generic chatbot, this app builds the foundations of an agentic system step by step:

```text
User request
    ↓
API endpoint
    ↓
Agent/recommendation layer
    ↓
Tools
    ↓
Persistent memory
    ↓
Structured recommendation
```

The current version is not fully AI-powered yet, but it establishes the backend, memory, and tool structure needed for an agentic AI caddie.
