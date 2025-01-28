import openai
import os
import streamlit as st

# Pobieranie klucza API z Secrets Streamlit
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Generator opisów produktowych z GPT")
st.write("Wprowadź dane produktu, aby wygenerować opis SEO.")

# Dane wejściowe od użytkownika
product_details = st.text_area("Dane produktu (wklej poniżej)", """
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
""")

if st.button("Generuj opis"):
    prompt = f"""
    Stwórz rozbudowany, atrakcyjny opis produktowy z uwzględnieniem zasad SEO na podstawie poniższych danych:
    {product_details}
    """

    try:
        # Zmiana struktury zgodnie z nowym API OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Możesz zmienić na "gpt-3.5-turbo" dla tańszej opcji
            messages=[
                {"role": "system", "content": "You are a professional e-commerce content writer specializing in SEO."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        # Wyświetlenie odpowiedzi modelu
        st.subheader("Wygenerowany opis produktu:")
        st.write(response.choices[0].message.content)  # Użycie obiektu `message.content` zamiast indeksowania

    except openai.error.AuthenticationError:
        st.error("Błąd: Nieprawidłowy klucz API.")
    except openai.error.OpenAIError as e:
        st.error(f"Błąd API OpenAI: {e}")
    except Exception as e:
        st.error(f"Nieoczekiwany błąd: {e}")
