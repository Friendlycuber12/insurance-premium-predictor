# Insurance Premium Predictor API

A Machine Learning-powered Insurance Premium Prediction API built with FastAPI. This project predicts insurance premiums based on user demographics and lifestyle factors.

## Live Demo

🌐 **Project URL:** http://13.60.45.63:8000/

📖 **Swagger Documentation:** http://13.60.45.63:8000/docs

## Features

- Predict insurance premiums using a trained Machine Learning model
- FastAPI backend with automatic API documentation
- Dockerized application
- Deployed on AWS EC2
- Input validation using Pydantic

## Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas
- Pydantic
- Docker
- AWS EC2

## Run Locally

```bash
git clone https://github.com/your-username/Insurance-Premium-Predictor.git
cd Insurance-Premium-Predictor

python -m venv myenv
source myenv/bin/activate

pip install -r requirements.txt

uvicorn app:app --reload
```

## API Documentation

Local:

```text
http://127.0.0.1:8000/docs
```

Production:

```text
http://13.60.45.63:8000/docs
```

## Deployment

The API is containerized using Docker and deployed on AWS EC2.

## Author

**Keshav Soni**

Computer Science Engineering Student | Backend Development Enthusiast
