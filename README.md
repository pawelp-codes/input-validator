# Input Validator

Prosty moduł w Pythonie do walidacji danych wejściowych wpisanych przez użytkownika.
    /   Simple Python module for validating user input data.

## Funkcje  /   Features
- Walidacja liczb całkowitych (`int`)   /   Validation of integers (`int`)  
- Walidacja liczb zmiennoprzecinkowych (`float`)    /   Validation of floating-point numbers (`float`) 
- Walidacja stringów z opcjonalną listą dozwolonych wartości    /   Validation of strings with an optional list of allowed values
## Przykład użycia

```python
from input_validate import inputValidate

age = inputValidate("Wprowadź wiek: ", "int", onlyPositive=True)
color = inputValidate("Wybierz kolor (red, green, blue): ", "string", wordList=["red", "green", "blue"])
