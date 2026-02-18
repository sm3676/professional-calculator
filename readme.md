# Professional Calculator

A modular, object-oriented Python calculator built using clean architecture principles and the Factory Design Pattern.  
This project includes full unit testing and GitHub Actions CI integration.

---

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Division by zero handling
- Factory Pattern implementation
- Object-Oriented Design
- 100% Unit Test Coverage
- GitHub Actions Continuous Integration

---

##  Project Structure

```
professional-calculator/
│
├── app/
│   ├── calculator/
│   ├── calculation/
│   └── operation/
│
├── tests/
├── .github/workflows/
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Architecture Overview

This project follows:

- Object-Oriented Programming (OOP)
- Factory Design Pattern
- Modular and Clean Architecture
- Separation of Concerns

Flow of execution:

Calculator → CalculationFactory → Calculation → Operation

## Running the Project Locally

### 1️⃣ Create and Activate Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### 3️⃣ Run Tests
python -m pytest -v

### 4️⃣ Run Coverage Report

python -m pytest --cov=app

Expected coverage:

TOTAL 100%

## GitHub Actions (CI)

This project includes an automated GitHub Actions workflow.

On every push:

- Dependencies are installed
- Tests are executed
- Coverage is verified
- Build status is validated

You can view the CI results in the **Actions** tab of this repository.


## Example Usage

python
from app.calculator.calculator import Calculator

result = Calculator.calculate(10, 5, "add")
print(result)  # Output: 15


## Technologies Used

- Python 3
- Pytest
- Pytest-Cov
- Git
- GitHub Actions



## Author

Sharvani  
GitHub: https://github.com/sm3676
