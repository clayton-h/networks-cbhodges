#
# Python script that simulates
# access point functionality
#
# By: Clayton H.
#

import time


class AccessPoint:
    """Class that simulates an Access Point.
    """

    def __init__(self, name: str, floor_number: int) -> None:
        """Constructor initializes AP with corresponding information.

        Args:
            name (str): AP name
            floor_number (int): AP floor number (location)
        """
        self.__name: str = name
        self.__floor_number: int = floor_number
        # a set is used for better performance
        # (as the data's order is unimportant, unlike an array)
        self.__connected_devices: set[str] = set()

    @property
    def name(self) -> str:
        """Getter for AP name

        Returns:
            str: AP name
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """Setter for AP name

        Args:
            value (str): AP name
        """
        self.__name = value

    # Getter for floor number
    @property
    def floor_number(self) -> int:
        """Getter for AP floor number (location)

        Returns:
            int: AP floor number (location)
        """
        return self.__floor_number

    @floor_number.setter
    def floor_number(self, value: int) -> None:
        """Setter for AP floor number (location)

        Args:
            value (int): AP floor number (location)
        """
        self.__floor_number = value

    # Getter for connected devices
    @property
    def connected_devices(self) -> set[str]:
        """Getter for devices connected to an AP

        Returns:
            set: Set of devices connected to an AP
        """
        return self.__connected_devices

    def connect_device(self, device: str, device_location: int) -> None:
        """Function to connect devices to APs.

        Args:
            device (str): AP name
            device_location (int): AP floor number (int)
        """
        self.__connected_devices.add(device)
        time.sleep(1)
        print(f"{device} (Floor {device_location}) connected to ")
        print(f"Access Point {self.__name} (Floor {self.__floor_number}).\n")

    def disconnect_device(self, device: str, device_location: int) -> None:
        """Function to disconnect devices from APs.

        Args:
            device (str): AP name
            device_location (int): AP floor number (location)
        """
        if device in self.__connected_devices:
            self.__connected_devices.remove(device)
            time.sleep(1)
            print(f"{device} (Floor {device_location}) disconnected from ")
            print(f"Access Point {self.__name} (Floor {self.__floor_number}).\n")
