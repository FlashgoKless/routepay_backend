import requests
import json

# URL вашего Flask-сервера
API_URL = "http://localhost:8002/route?json={'locations':[{'lat': 55.751244,'lon': 37.618423},{'lat': 59.934280,'lon': 30.335098}]}"

# Отправляем запрос
try:
    response = requests.post(
        API_URL,
        headers={"Content-Type": "application/json"})
    
    # Проверяем статус ответа
    if response.status_code == 200:
        result = response.json()
        print("Успешный ответ:")
        print(f"Количество маневров: {len(result['maneuvers_geometries'])}")
        
        # Пример вывода первой геометрии
        if result['maneuvers_geometries']:
            first_maneuver = result['maneuvers_geometries'][0]
            print(f"\nПервый маневр (тип: {first_maneuver.get('type', 'unknown')}):")
            print(f"Координаты: {first_maneuver['coordinates'][:2]}...")  # Выводим первые 2 точки
    
    else:
        print(f"Ошибка: {response.status_code}")
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Ошибка при выполнении запроса: {e}")