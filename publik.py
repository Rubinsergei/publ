import re
from transformers import pipeline
from datetime import datetime, timedelta

# Создаем pipeline с моделью для генерации текста
generator = pipeline("text-generation", model="sberbank-ai/rugpt3large_based_on_gpt2", device=0)

# Определение функций для выполнения простых действий
def get_time():
    current_time = datetime.now().strftime("%H:%M")
    return f"Сейчас {current_time}."

def set_timer(minutes):
    end_time = datetime.now() + timedelta(minutes=int(minutes))
    end_time_str = end_time.strftime("%H:%M")
    return f"Таймер установлен на {minutes} минут. Таймер сработает в {end_time_str}."

# Функция для обработки вопросов и выполнения действий
def process_query(query):
    if "сколько времени" in query:
        return get_time()
    elif "таймер" in query:
        minutes = re.findall(r"\d+", query)
        if minutes:
            return set_timer(minutes[0])
        else:
            return "Пожалуйста, укажите время для таймера."
    else:
        response = generator(query, max_length=50, num_return_sequences=1)[0]["generated_text"]
        return response

# Функция ассистента с использованием ИИ
def personal_assistant():
    print("Здравствуйте! Я ваш личный ассистент на основе ИИ. Чем могу помочь?")
    
    while True:
        query = input("> ")
        if "пока" in query or "до свидания" in query:
            print("До свидания! Если понадобится помощь, обращайтесь!")
            break

        response = process_query(query)
        print(response)

# Запуск ассистента
if __name__ == "__main__":
    personal_assistant()