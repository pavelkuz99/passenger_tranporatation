import json
import requests


class ApiError(Exception):
    def __init__(self, message):
        super(ApiError, self).__init__(message)


class ClientMethods:
    @staticmethod
    def create(name: str, phone: str):
        info = {"name": name, "phone": phone}
        response = requests.post('http://localhost:8000/clients/', json=info)
        if response.status_code != 201:
            raise ApiError(f'POST /clients/ {response.status_code}')

    @staticmethod
    def read_one(client_id: int):
        response = requests.get(f'http://localhost:8000/clients/{client_id}/')
        if response.status_code != 200:
            raise ApiError(f'GET /clients/{client_id}/ {response.status_code}')
        info = response.json()
        print(f'{info["name"]}: {info["phone"]}: {info["status"]}')

    @staticmethod
    def read_all():
        response = requests.get(f'http://localhost:8000/clients/')
        if response.status_code != 200:
            raise ApiError(f'GET /clients/ {response.status_code}')
        for info in response.json():
            print(f'{info["name"]}: {info["phone"]}: {info["status"]}')

    @staticmethod
    def update(client_id: int, field_to_update: str, new_info) -> (int, json):
        info = {field_to_update: new_info}
        response = requests.put(f'http://localhost:8000/clients/{client_id}/', json=info)
        if response.status_code != 200:
            raise ApiError(f'GET /clients/{client_id}/ {response.status_code}')



#
#
# class RouteActions:
#
#
# class RideActions:
#
#
# class DriverActions:
#
#
# class VehicleActions
#
#
#
#     class Person:
#
#
#     class Manager(Person):
#         def __init__(self, id_number: int, name: str, phone: str, level: int):
#             super().__init__(id_number, name, phone)
#             self.level = level
#
#     class Driver(Person):
#         def __init__(self, id_number: int, name: str, phone: str):
#             super().__init__(id_number, name, phone)
#             self.rating = 0.0
#             self.workload = []
#             self.status = ''
#
#     class Passenger(Person):
#         def __init__(self, id_number: int, name: str, phone: str):
#             super().__init__(id_number, name, phone)
#             self.rating = ''
#             self.rides_list = []
#             self.status = ''
#
#     class Transport:
#         def __init__(self, model: str, color: str, capacity: int, license_number: str):
#             self.model = model
#             self.color = color
#             self.capacity = capacity
#             self.license_number = license_number
#
#     class Route:
#         def __init__(self, start_point: str, end_point: str, duration: int, distance: int):
#             self.start_point = start_point
#             self.end_point = end_point
#             self.stops_list = []
#             self.duration = duration
#             self.distance = distance
#
#     class Ride(Route):
#         def __init__(self, start_point: str, end_point: str, ride_date: date, ride_time: time, duration: int,
#                      distance: int, car: Transport, driver: Driver):
#             super().__init__(start_point, end_point, duration, distance)
#             self.ride_date = ride_date
#             self.ride_time = ride_time
#             self.car = car
#
#     self.driver = driver