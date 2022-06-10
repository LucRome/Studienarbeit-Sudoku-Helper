![](logo.png)

# Step-by-Step Sudoku
Repository für die Studienarbeit zum Thema Sudoku-Helper

## Setup
- Go to `src` folder and run:
```
python -m venv .venv
```
- After creating the virtual environment enter it:
    - Windows: `.venv\Scripts\activate.ps1` (Powershell), ``.venv\Scripts\activate.bat` (CMD)
      - *important: To use the Powershell, enable Execution of Powershell Scripts ([superuser.com](https://superuser.com/questions/106360/how-to-enable-execution-of-powershell-scripts))*
    - Unix: `source .venv/bin/activate`
- Install the dependencies:
    - `pip install -r requirements.txt`

### Using the Tasks for VisualStudio-Code:
- Can be used for easier handling
- Open `studienarbeit-sudoku-helper` folder with VS-Code
- Extension: Install `Python Extension Pack` to ensure correct function
- `F1`  -> `Python: Select Interpreter` -> Select the Interpreter from the venv
  - on Windows in `.venv/Scripts`
- To run a Task:
  - `F1` -> `Task: Run Task` -> Select Task

## Running the App
- Database migration:
```
py manage.py migrate
```
- Run:
  - Terminal:
    ```
    py manage.py runserver
    ```
  - VS Code:
    - Task: `Run Server`

## Running the Tests
### backend Tests
- execute tests
  - Terminal:
    - Go to folder `./src/backend`
    ```
    py -m unittest "validation.test_validation" "algorithms.test_algorithms" "sudoku.tests" "algorithms.test_utils" "algorithms.test_completion"
    ```
  - VS-Code:
    - Task: `Run Tests for Validation`

### Frontend Tests
### Requirements
- Selenium Package for Python
  - Installed with the other requirements
- Browser:
  - [Firefox](https://www.mozilla.org/de/firefox/new/)
### Executing
- Terminal:
  - go to folder `./src`
  - execute all test cases you want to execute
    - e.g.:
      ```
      py -m unittest frontend_tests.test_index [other test cases]
      ```
- VS-Code:
  - Task: `Run Frontend Tests`

# *Logo*
- *created using [canva.com](https://www.canva.com)*
- *favicons etc. generated using [realfavicongenerator.net](https://realfavicongenerator.net)*