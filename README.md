# Input Validator

Prosty moduł w Pythonie do walidacji danych wejściowych wpisanych przez użytkownika.

## Funkcje
- Walidacja liczb całkowitych (`int`)
- Walidacja liczb zmiennoprzecinkowych (`float`)
- Walidacja stringów z opcjonalną listą dozwolonych wartości

## Przykład użycia

```python
from input_validate import inputValidate

age = inputValidate("Wprowadź wiek: ", "int", onlyPositive=True)
color = inputValidate("Wybierz kolor (red, green, blue): ", "string", wordList=["red", "green", "blue"])
