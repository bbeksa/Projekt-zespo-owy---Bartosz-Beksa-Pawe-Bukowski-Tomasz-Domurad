# Bartosz Beksa, Paweł Bukowski, Tomasz Domurad
# Projekt zespołowy

Aplikacja do zarządzania fakturami

<br />

Instalacja:

Na komputerze należy zainstalować do Pythona następujące biblioteki: Pillow, Django, fpdf, num2words

pytesseract: https://github.com/UB-Mannheim/tesseract/wiki <br />
W pliku textRecognition.py należy podać ścieżkę do miejsca instalacji <br />

Polski pakiet językowy dla pytesseract: https://github.com/tesseract-ocr/tessdata <br />
Plik "pol" wrzucić do miejsca instalacji pytesseract

<br />

Uruchomienie:

Uruchomić konsole w katalogu projekt i wpisać komendę
```
python manage.py runserver
```

# 

<br />

Potencjalnymi użytkownikami są małe firmy lub posiadacze jednosobowych działalności gospodarczych lub małych firm którzy przez brak czasu lub umiejętności zlecają prowadenie dokumentacji biurom rachunkowym.

<br />

Funkcjonalności:

-skanowanie faktur, program pobiera zdjęcie lub skan faktury i sczytuje dane z dokumentu

-przechowywanie dokumentów

-tworzenie nowych od zera

-uzupełnianie i modyfikowanie już istniejących faktur 

<br />

Technologie:

-Python z użyciem biblotek Pillow, pytesseract, fpdf2

-framework Django 

<br />

Aspekt badawczy:

-zapoznanie się z możliwościami bibliotek do rozpoznawania tekstu ze zdjęcia


