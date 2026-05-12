# PEREGRIN Technical Assessment

## Overview

This repository contains a test automation suite for both web UI and API validation. It includes:

- `saucedemo/`: end-to-end web tests for the Sauce Demo application
- `api/`: API test cases and edge case coverage
- `pages/`: Page object models for the web tests
- `utils/`: shared utilities such as screenshot capture

## Requirements

- Python 3.11+ (project uses a Python virtual environment)
- `pytest` for test execution
- `playwright` for browser automation

## Setup

From the repository root:

Create a virtual environment:
```powershell
python -m venv <assign a (directory name)>
```
Activate and enter the virtual environment
```powershell
.\<directory name>\Scripts\activate
pip install -r requirements.txt
```

Note: (Use this line if it persist to not activate the virtual environment)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

If Playwright browsers are not installed, run:

```powershell
python -m playwright install
```

## Running Tests

### Run all pytest tests

```powershell
pytest
```

### Run a specific Sauce Demo test

```powershell
pytest saucedemo\saucedemo_checkout_test.py
```

### Run API tests

```powershell
pytest api
```

## Project Structure
```
technical-assessment-test/
├── api/
│   ├── get_user_1_test.py
│   ├── get_users_test.py
│   ├── post_user_title_and_body_test.py
│   ├── put_user_title_and_body_test.py
│   └── edge_cases/
│       └── api_edge_cases_test.py
├── saucedemo/
│   └── checkout_flow_test.py
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── checkout_page.py
│   └── checkout_information.py
├── utils/
│   └── screenshot.py
├── conftest.py
├── pytest.ini
└── requirements.txt
```
## Notes

- Ensure the virtual environment is activated before running tests.
- Use `pytest` options like `-q` for quieter output or `--html=report.html` to generate an HTML report.

## Report

A sample test report is available in `report.html`.
