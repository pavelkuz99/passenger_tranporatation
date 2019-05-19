import json
import requests


class ApiError(Exception):
    def __init__(self, message):
        super(ApiError, self).__init__(message)


class GeneralMethods:
    @staticmethod
    def create(model_type, info: json):
        response = requests.post(f'http://localhost:8000/{model_type}s/', json=info)
        if response.status_code != 201:
            raise ApiError(f'POST /{model_type}s/ {response.status_code}')

    @staticmethod
    def read_one(model_type, model_id: int):
        response = requests.get(f'http://localhost:8000/{model_type}s/{model_id}/')
        if response.status_code != 200:
            raise ApiError(f'GET /{model_type}s/{model_id}/ {response.status_code}')
        return response.json()

    @staticmethod
    def read_all(model_type):
        response = requests.get(f'http://localhost:8000/{model_type}s/')
        if response.status_code != 200:
            raise ApiError(f'GET /{model_type}s/ {response.status_code}')
        return response.json()

    @staticmethod
    def update(model_type, model_id: int, info: json):
        response = requests.put(f'http://localhost:8000/{model_type}s/{model_id}/', json=info)
        if response.status_code != 200:
            raise ApiError(f'GET /{model_type}s/{model_id}/ {response.status_code}')

    @staticmethod
    def delete(model_type, model_id: int):
        response = requests.delete(f'http://localhost:8000/{model_type}s/{model_id}/')
        if response.status_code != 204:
            raise ApiError(f'GET /{model_type}s/{model_id}/ {response.status_code}')


class ClientMethods:
    @staticmethod
    def create(name: str, phone: str):
        data = {"name": name, "phone": phone}
        GeneralMethods.create('client', data)

    @staticmethod
    def read_one(model_id):
        data = GeneralMethods.read_one('client', model_id)
        print(f'{data["name"]}: {data["phone"]}: {data["status"]}')

    @staticmethod
    def read_all():
        data = GeneralMethods.read_all('client')
        for item in data:
            print(f'{item["name"]}: {item["phone"]}: {item["status"]}')

    @staticmethod
    def update(model_id, field_to_update: str, new_info):
        data = {field_to_update: new_info}
        GeneralMethods.update('client', model_id, data)

    @staticmethod
    def delete(model_id):
        GeneralMethods.delete('client', model_id)



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