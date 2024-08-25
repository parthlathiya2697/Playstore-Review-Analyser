Run Instructions

Python version : 3.10.5

python3 -m pip install --upgrade pip

0. Create and activate virtual env
python -m venv .venv
source .venv/bin/activate

1. Install requirements.txt
pip install -r requirements.txt

# Command
python3 main.py

or 

uvicorn main:app --reload

# Dev Env
- Use ' '(one space) as the x-token in the Header of the API Request to gain access