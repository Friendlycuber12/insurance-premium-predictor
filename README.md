# Insurance Premium Predictor API

A Machine Learning-powered Insurance Premium Prediction API built with FastAPI and a Streamlit frontend. This project predicts insurance premium categories based on user demographics and lifestyle factors.

## Live Demo

Backend API:

```text
http://13.60.45.63:8000/
```

Swagger documentation:

```text
http://13.60.45.63:8000/docs
```

Streamlit frontend:

```text
http://13.60.45.63:8501/
```

## Features

- Predict insurance premium categories using a trained Machine Learning model
- FastAPI backend with automatic API documentation
- Streamlit frontend connected to the prediction API
- Dockerized backend and frontend services
- Deployed on AWS EC2
- Input validation using Pydantic

## Tech Stack

- Python
- FastAPI
- Streamlit
- Scikit-learn
- Pandas
- Pydantic
- Docker
- Docker Compose
- AWS EC2

## Run Locally Without Docker

```bash
git clone https://github.com/Friendlycuber12/insurance-premium-predictor.git
cd insurance-premium-predictor

python -m venv myenv
source myenv/bin/activate

pip install -r requirements.txt

uvicorn app:app --reload
```

In another terminal, run the frontend:

```bash
API_URL=http://127.0.0.1:8000/predict streamlit run frontend.py
```

Backend docs:

```text
http://127.0.0.1:8000/docs
```

Frontend:

```text
http://127.0.0.1:8501/
```

## Run With Docker Compose

```bash
docker compose up --build -d
```

Backend API:

```text
http://127.0.0.1:8000/
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Streamlit frontend:

```text
http://127.0.0.1:8501/
```

## EC2 Deployment

SSH into the EC2 instance, pull the latest code, and restart both services:

```bash
cd insurance-premium-predictor
git pull origin main
docker compose down
docker compose up --build -d
```

Make sure the EC2 security group allows inbound TCP traffic on:

- `8000` for the FastAPI backend and `/docs`
- `8501` for the Streamlit frontend

## Author

**Keshav Soni**

Computer Science Engineering Student | Backend Development Enthusiast
