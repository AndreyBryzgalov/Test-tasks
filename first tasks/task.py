import requests
import time

base_url = "https://restful-booker.herokuapp.com"

auth_data = {
    "username": "admin",
    "password": "password123"
}
auth_response = requests.post(f"{base_url}/auth", json=auth_data)
token = auth_response.json()["token"]

# создания бронирования
def create_booking(token):
    booking_data = {
        "firstname": "Андрей",
        "lastname": "Брызгалов",
        "totalprice": 1000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-11-01",
            "checkout": "2023-11-10"
        },
        "additionalneeds": "Питание"
    }
    response = requests.post(f"{base_url}/booking", json=booking_data, headers={"Authorization": f"Bearer {token}"})
    booking_id = response.json()["bookingid"]
    print(f"Идентификатор бронирования: {booking_id}")
    return booking_id

# обновления бронирования
def update_booking(token, booking_id):
    update_data = {
        "bookingdates": {
            "checkin": "2023-11-11",
            "checkout": "2023-11-25"
        }
    }
    update_response = requests.patch(f"{base_url}/booking/{booking_id}", json=update_data, headers={"Authorization": f"Bearer {token}"})

# получение информации о бронировании
def get_booking_info(token, booking_id):
    get_response = requests.get(f"{base_url}/booking/{booking_id}", headers={"Authorization": f"Bearer {token}"})
    booking_info = get_response.json()
    print("Информация о бронировании:")
    print(booking_info)
    return booking_info

# удаления бронирования
def delete_booking(token, booking_id):
    delete_response = requests.delete(f"{base_url}/booking/{booking_id}", headers={"Authorization": f"Bearer {token}"})
    if delete_response.status_code == 204:
        print(f"Бронь {booking_id} успешно удалена.")
    elif delete_response.status_code == 404:
        print(f"Бронь {booking_id} не найдена .")
    else:
        print(f"Ошибка удаление {booking_id}. Status code: {delete_response.status_code}")

booking_id = create_booking(token)
update_booking(token, booking_id)
booking_info = get_booking_info(token, booking_id)
time.sleep(5)  # Подождать перед удалением
delete_booking(token, booking_id)
