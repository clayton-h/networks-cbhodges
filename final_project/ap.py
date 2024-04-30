#
# Python script that simulates
# an AP
#
# By: Clayton H.
#

import time


class AccessPoint:
    def __init__(self, name, floor_number) -> None:
        """Constructor initializes AP with corresponding information."""
        self.__name = name
        self.__floor_number = floor_number
        self.__connected_devices = []

    # Getter for name
    @property
    def name(self):
        return self.__name

    # Setter for name
    @name.setter
    def name(self, value):
        self.__name = value

    # Getter for floor number
    @property
    def floor_number(self):
        return self.__floor_number

    # Setter for floor number
    @floor_number.setter
    def floor_number(self, value):
        self.__floor_number = value

    # Getter for connected devices
    @property
    def connected_devices(self):
        return self.__connected_devices

    def connect_device(self, device, device_location) -> None:
        """Function to connect devices to APs."""
        self.__connected_devices.append(device)
        time.sleep(1)
        print(f"{device} (Floor {device_location}) connected to Access Point {self.__name} on Floor {self.__floor_number}.")

    def disconnect_device(self, device, device_location) -> None:
        """Function to disconnect devices from APs."""
        if device in self.__connected_devices:
            self.__connected_devices.remove(device)
            time.sleep(1)
            print(f"{device} (Floor {device_location}) disconnected from Access Point {self.__name} on Floor {self.__floor_number}.")
