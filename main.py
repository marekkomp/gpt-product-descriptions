import openai
import os

# Ustaw swój klucz API
openai.api_key = "TWÓJ_KLUCZ_API"  # Wklej swój klucz API tutaj

# Prosty prompt do API OpenAI
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Możesz zmienić na "gpt-4", jeśli masz dostęp
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Napisz prosty opis laptopa Fujitsu Lifebook U747."}
        ],
        max_tokens=100,
        temperature=0.7
    )
    print(response.choices[0].message.content)
except openai.AuthenticationError:
    print("Błąd autoryzacji: Sprawdź swój klucz API.")
except openai.OpenAIError as e:
    print(f"Wystąpił błąd w API OpenAI: {e}")
except Exception as e:
    print(f"Nieoczekiwany błąd: {e}")
