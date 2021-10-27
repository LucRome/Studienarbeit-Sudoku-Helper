# Studienarbeit-Sudoku-Helper
Repository für die Studienarbeit zum Thema Sudoku-Helper

# Setup
- Go to `src` folder and run:
```
python -m venv .venv
```
- After creating the virtual environment enter it:
    - Windows: `.venv\Scripts\activate.bat`
    - Unix: `source .venv/bin/activate`
- Install the dependencies:
    - `pip install -r requirements.txt`

# Running the App
- Database migration:
```
py manage.py migrate
```
- Run:
```
py manage.py runserver
```