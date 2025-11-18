"""
### PL

inputValidator.py
Funkcja inputValidate służy do walidacji danych wejściowych od użytkownika.

Parametry:
- requestStr: string, zapytanie wyświetlane użytkownikowi
- dataTypeStr: string, oczekiwany typ danych: "int", "float" lub "string"
- onlyPositive: bool (opcjonalnie), tylko wartości dodatnie dla int i float
- wordList: list (opcjonalnie), lista dozwolonych stringów dla typu string

### ENG

inputValidator.py
The inputValidate function is used to validate input data from the user.

Parameters:

- requestStr: string, the prompt displayed to the user
- dataTypeStr: string, the expected data type: "int", "float", or "string"
- onlyPositive: bool (optional), only positive values for int and float
- wordList: list (optional), list of allowed strings for type string

"""

def inputValidate(requestStr, dataTypeStr, onlyPositive = False, wordList = []):
    while True:
        try:
            if dataTypeStr == "int":
                res = int(input(requestStr)) 
                if onlyPositive:
                    if res > 0:
                        return res
                    else:
                        print(f"Wrong value have been written, write {dataTypeStr} with positive sign")
                        continue
                else:
                    return res   

            if dataTypeStr == "float":
                res = float(input(requestStr)) 
                if onlyPositive:
                    if res > 0:
                        return res
                    else:
                        print(f"Wrong value have been written, write {dataTypeStr} with positive sign")
                        continue
                else:
                    return res

            if dataTypeStr == "string":
                res = str(input(requestStr).lower()) 
                if not wordList:
                    return res
                else:
                    if res in wordList:
                        return res
                    else:
                        print(f"Wrong value have been written, write {dataTypeStr} from list {wordList}")
                        continue

        except ValueError:
            if (dataTypeStr == "int" or dataTypeStr == "float") and onlyPositive == True:
                print(f"Wrong value have been written, write {dataTypeStr} with positive sign")
            else:
                print(f"Wrong value have been written, write {dataTypeStr} value")
            continue

###################################################################################################