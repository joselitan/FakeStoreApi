Valde att lägga till loggers så att testet kunde print ut:
- status code
- antal produkter
- att specifik produkt returnerar korrekt fält
- att specifikt product id returnerar rät data

för att köra test skall lokalt måste du installera python och sedan pytest och request. detta gör du genom:
https://www.python.org/downloads/
pip install pytest
pip install requests

det finns även en fil i root foldern som heter requirements.txt som innehåller ovan dependencys och då räcker det med:
pip install -r requirements.txt

När ovan är klar är det bara köra test genom att först vara i root folder för projektet och sedan i terminal fältet skriva:
pytest -v 