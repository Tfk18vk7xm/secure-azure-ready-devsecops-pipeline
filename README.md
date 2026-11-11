
# Secure Azure-Ready DevSecOps Release Pipeline

An end-to-end DevSecOps project demonstrating automated application testing, security scanning, container supply chain security, and controlled software releases.

## Project Objective

Build a secure and automated release pipeline using GitHub Actions, Docker, and open-source security tools, with Azure infrastructure templates validated locally.

## Technology Stack

- Python
- FastAPI
- Pytest
- Git and GitHub
- GitHub Actions
- Docker
- Bandit
- Trivy
- Syft
- Cosign
- Azure Bicep

## Application Features

- REST API built using FastAPI
- Home endpoint (`/`)
- Health-check endpoint (`/health`)
- Interactive API documentation (`/docs`)
- Automated endpoint tests using Pytest

## Project Structure

```text
secure-azure-ready-devsecops-pipeline/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Run Locally

Create and activate a virtual environment, then install dependencies:

```bash
python -m venv venv
pip install -r requirements.txt
```

Start the application:

```bash
python -m uvicorn app.main:app --reload
```

Run automated tests:

```bash
python -m pytest -v
```

## Development Progress

### Day 1 — Application Foundation

- Created FastAPI application.
- Implemented home and health-check endpoints.
- Created automated tests.
- Verified both tests successfully.
- Configured Python virtual environment.
- Added Git ignore rules.

### Upcoming Implementation

- GitHub repository setup.
- GitHub Actions CI pipeline.
- Automated security scanning.
- Docker image build and scanning.
- Software Bill of Materials (SBOM).
- Container image signing and verification.
- Azure Bicep template validation.
- Controlled release workflow.

## Cost Considerations

Designed as a local-first project using free and open-source tools. No paid Azure infrastructure is required for the planned implementation.
