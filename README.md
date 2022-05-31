![](logo.png)

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

# Running the Tests
## backend Tests
**Tests for Sudoku Base Classes:**
- go to folder containing sudoku classes
```
cd ./src/backend
```
- execute tests
```
py -m unittest sudoku.Tests
py -m unittest validation.test_validation
```

## Frontend Tests
### Requirements
- Selenium Package for Python
  - Installed with the other requirements
- Browser:
  - [Firefox](https://www.mozilla.org/de/firefox/new/)
### Executing
- go to folder `src`
  - `cd ..../Studienarbeit-Sudoku-Helper/src`
- execute all test cases you want to execute
  - e.g.:
    ```
    py -m unittest frontend_tests.test_index [other test cases]
    ```