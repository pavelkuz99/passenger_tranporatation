import json
import requests
from datetime import datetime


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
        print(f'{data["name"]} : {data["phone"]} : {data["status"]}')

    @staticmethod
    def read_all():
        data = GeneralMethods.read_all('client')
        for item in data:
            print(f'{item["name"]} : {item["phone"]} : {item["status"]}')

    @staticmethod
    def update(model_id, field_to_update: str, new_info):
        data = {field_to_update: new_info}
        GeneralMethods.update('client', model_id, data)

    @staticmethod
    def delete(model_id):
        GeneralMethods.delete('client', model_id)


class RouteMethods:
    @staticmethod
    def create(route: str, distance: int):
        data = {"start_end": route, "distance": distance}
        GeneralMethods.create('route', data)

    @staticmethod
    def read_one(model_id):
        data = GeneralMethods.read_one('route', model_id)
        print(f'{data["start_end"]} : {data["distance"]}')

    @staticmethod
    def read_all():
        data = GeneralMethods.read_all('route')
        for item in data:
            print(f'{item["start_end"]} : {item["distance"]}')

    @staticmethod
    def update(model_id, field_to_update: str, new_info):
        data = {field_to_update: new_info}
        GeneralMethods.update('route', model_id, data)

    @staticmethod
    def delete(model_id):
        GeneralMethods.delete('route', model_id)


class VehicleMethods:
    @staticmethod
    def create(car_model: str, color: str, car_license: str):
        data = {"car_model": car_model, "color": color, "car_license": car_license}
        GeneralMethods.create('vehicle', data)

    @staticmethod
    def read_one(model_id):
        data = GeneralMethods.read_one('vehicle', model_id)
        print(f'{data["car_model"]} : {data["color"]} : {data["car_license"]}')

    @staticmethod
    def read_all():
        data = GeneralMethods.read_all('vehicle')
        for item in data:
            print(f'{item["car_model"]} : {item["color"]} : {item["car_license"]}')

    @staticmethod
    def update(model_id, field_to_update: str, new_info):
        data = {field_to_update: new_info}
        GeneralMethods.update('vehicle', model_id, data)

    @staticmethod
    def delete(model_id):
        GeneralMethods.delete('vehicle', model_id)


class DriverMethods:
    @staticmethod
    def create(name: str, phone: str):
        data = {"name": name, "phone": phone}
        GeneralMethods.create('driver', data)

    @staticmethod
    def read_one(model_id):
        data = GeneralMethods.read_one('driver', model_id)
        print(f'{data["name"]} : {data["phone"]} : {data["rating"]}')

    @staticmethod
    def read_all():
        data = GeneralMethods.read_all('driver')
        for item in data:
            print(f'{item["name"]} : {item["phone"]} : {item["rating"]}')

    @staticmethod
    def update(model_id, field_to_update: str, new_info):
        data = {field_to_update: new_info}
        GeneralMethods.update('driver', model_id, data)

    @staticmethod
    def delete(model_id):
        GeneralMethods.delete('driver', model_id)


class RideMethods:
    @staticmethod
    def create(route: str, date_and_time, driver: str, vehicle: str):
        data = {"route": route, "date_and_time": date_and_time, "driver": driver, "vehicle": vehicle}
        GeneralMethods.create('ride', data)

    @staticmethod
    def read_one(model_id):
        data = GeneralMethods.read_one('ride', model_id)
        print(f'{data["route"]} : {data["date_and_time"]} : {data["driver"]} : {data["vehicle"]}')

    @staticmethod
    def read_all():
        data = GeneralMethods.read_all('ride')
        for item in data:
            print(f'{item["route"]} : {item["date_and_time"]} : {item["driver"]} : {item["vehicle"]}')

    @staticmethod
    def update(model_id, field_to_update: str, new_info):
        data = {field_to_update: new_info}
        GeneralMethods.update('ride', model_id, data)

    @staticmethod
    def delete(model_id):
        GeneralMethods.delete('ride', model_id)
