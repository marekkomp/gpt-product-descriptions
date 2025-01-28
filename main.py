import openai
import os

# Pobieranie klucza API z zmiennej środowiskowej
openai.api_key = os.getenv("OPENAI_API_KEY")

# Funkcja do generowania opisu produktu
def generate_product_description(product_details):
    prompt = f"""
    Stwórz rozbudowany, atrakcyjny opis produktowy z uwzględnieniem zasad SEO na podstawie poniższych danych:
    
    Szczegóły produktu:
    {product_details}
    
    Uwzględnij:
    - Zalety produktu i specyfikacje techniczne.
    - Grupę docelową (np. dla biznesu, pracy biurowej, nauki).
    - Optymalizację pod kątem SEO, używając słów kluczowych jak: "laptop poleasingowy", "Fujitsu Lifebook U747", "laptop biznesowy".
    - Zwięzłe akapity i czytelność.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional e-commerce content writer specializing in SEO."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    return response["choices"][0]["message"]["content"]

# Dane produktu
product_details = """
Kondycja: "A" poleasingowy, przetestowany
Producent: Fujitsu
Model: Lifebook U747
Seria procesora: Intel Core i5
Stan ekranu: Bez wad
Stan obudowy: Normalne, delikatne ślady użytkowania
Gwarancja: 12 miesięcy
Procesor: i5 - 6200U, 3MB Cache, 6 gen.
Taktowanie: 2.30 - 2.80 GHz
Ilość rdzeni: 2
Ilość pamięci RAM: 8GB
Typ pamięci RAM: DDR4
Dysk: 256GB
Typ dysku: SSD
Licencja: Windows 10 Professional
Typ licencji: OEM
Zainstalowany system: Windows 10 Professional
Ekran dotykowy: Nie
Rozdzielczość ekranu: 1920 x 1080
Przekątna ekranu: 14"
Powłoka matrycy: Matowa
Typ matrycy: IPS / PLS
Rodzaj karty graficznej: Zintegrowana
Model karty graficznej: Intel HD 520
Złącza zewnętrzne: 1x USB 3.0 typ C, 2x USB 3.0, VGA, DisplayPort, Audio, LAN
Napęd: Beznapędowy
Kamera: Tak, wbudowana
Komunikacja: WiFi
Bateria: Oryginalna, czas pracy od 1h do 2,5h (używana)
Klawiatura: QWERTY PL
W zestawie: Zasilacz z przewodem
"""

# Generowanie opisu
description = generate_product_description(product_details)
print("Wygenerowany opis produktu:")
print(description)
