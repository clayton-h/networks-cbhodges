#
# Python script that simulates
# WLAN controller functionality
#
# By: Clayton H.
#

import time
from ap import AccessPoint


class WLANController:
    """Class that simulates a WLAN controller.
    """

    def __init__(self) -> None:
        """Constructor initializes WLAN controller dictionary of APs.
        """
        self.__access_points: dict[str, AccessPoint] = {}

    def print_network(self) -> None:
        """Function to print all network information.
        """
        time.sleep(1)
        for ap_name, ap in self.__access_points.items():
            print(f"Access point {ap_name} (Floor {ap.floor_number}) online.")
            print(f"Connected Devices: {len(ap.connected_devices)}\n")

    def add_access_point(self, name: str, location: int) -> None:
        """Function to add access points to the WLAN controller.

        Args:
            name (str): AP name
            location (int): AP floor number (location)
        """
        if name not in self.__access_points:
            self.__access_points[name] = AccessPoint(name, location)
            time.sleep(1)
            print(f"Access Point {name} (Floor {location}) ")
            print("added to WLAN Controller.\n")

    def connect_device(self, device: str, device_location: int) -> None:
        """Function to connect devices to the network.

        Args:
            device (str): Device name
            device_location (int): Device floor number (location)
        """
        closest_ap = None
        min_distance = 1

        for ap_name, ap in self.__access_points.items():
            ap_location = ap.floor_number

            distance = self.calculate_distance(ap_location, device_location)

            # Only consider APs within 1 floor distance
            if distance <= min_distance:
                min_distance = distance
                closest_ap = ap_name

        if closest_ap is not None:
            self.__access_points[closest_ap].connect_device(
                device, device_location)
        else:
            time.sleep(1)
            print(f"Connection failed! No APs found within ({min_distance}) ")
            print(f"floor of {device} (Floor {device_location}).\n")

    def disconnect_device(self, device: str, device_location: int) -> None:
        """Function to disconnect devices from the network.

        Args:
            device (str): Device name
            device_location (int): Device floor number (location)
        """
        closest_ap = None
        min_distance = float('inf')  # infinity

        # First find the closest access point based on location
        for ap_name, ap in self.__access_points.items():
            ap_location = ap.floor_number
            distance = self.calculate_distance(ap_location, device_location)

            # Check for the access point that
            # the device is most likely connected to
            # (always true for the first real distance)
            if distance < min_distance:
                min_distance = distance
                closest_ap = ap_name

        # Disconnect the device if an appropriate access point is found
        if closest_ap is not None:
            self.__access_points[closest_ap].disconnect_device(
                device, device_location)
        else:
            print("No access point found that matches ")
            print(f"{device} (Floor {device_location}).\n")

    def calculate_distance(
            self, ap_location: int, device_location: int) -> int:
        """Function to calculate the distance between a given AP
        and device given floor their corresponding floor numbers.

        Args:
            ap_location (int): AP floor number (location)
            device_location (int): Device floor number (location)

        Returns:
            int: Distance between an AP and a device
        """
        return abs(ap_location - device_location)

    # def move_device(self, device: str, device_location_new: int) -> None:
    #     """Function to move a device and reconnect
    #     to an AP once moved.

    #     Args:
    #         device (str): Device name
    #         device_location_new (int): New device floor number (location)
    #     """
    #     device_location_old = 9001
    #     self.disconnect_device(device)
    #     self.connect_device(device)
    #     print(f"{device} moved from {device_location_old} ")
    #     print(f"to {device_location_new}.")
