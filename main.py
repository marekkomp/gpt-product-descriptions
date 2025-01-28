import openai

# Ustaw swój klucz API tutaj
openai.api_key = "TWÓJ_KLUCZ_API"

# Proste zapytanie do GPT
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Możesz zmienić na "gpt-4" jeśli masz dostęp
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Napisz prosty opis produktu laptopa Fujitsu Lifebook U747 z procesorem i5, 8GB RAM i dyskiem SSD 256GB."}
        ],
        max_tokens=150,
        temperature=0.7
    )
    print("Odpowiedź GPT:")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Wystąpił błąd: {e}")
