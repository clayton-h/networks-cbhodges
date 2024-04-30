#
# Python script that simulates
# a WLAN controller
#
# By: Clayton H.
#

import time
from ap import AccessPoint


class WLANController:
    def __init__(self) -> None:
        """Constructor initializes WLAN controller APs."""
        self.__access_points = {}

    def print_network(self) -> None:
        """Function to print all network information."""
        time.sleep(1)
        for ap_name, ap in self.__access_points.items():
            print(
                f"Access point {ap.name} (Floor {ap.floor_number}) online. Connected Devices: {ap.connected_devices}")

    def add_access_point(self, name, location) -> None:
        """Function to add access points to the WLAN controller."""
        if name not in self.__access_points:
            self.__access_points[name] = AccessPoint(name, location)
            time.sleep(1)
            print(
                f"Access Point {name} (Floor {location}) added to WLAN Controller.")

    def connect_device(self, device, device_location) -> None:
        """Function to connect devices to the network."""
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
            print(
                f"Connection failed! No APs found within ({min_distance}) floor of {device} (Floor {device_location}).")

    def disconnect_device(self, device, device_location) -> None:
        """Function to disconnect devices from the network."""
        closest_ap = None
        min_distance = float('inf')

        # First find the closest access point based on location
        for ap_name, ap in self.__access_points.items():
            ap_location = ap.floor_number
            distance = self.calculate_distance(ap_location, device_location)

            # Check for the access point that the device is most likely connected to
            if distance < min_distance:
                min_distance = distance
                closest_ap = ap_name

        # Disconnect the device if an appropriate access point is found
        if closest_ap is not None:
            self.__access_points[closest_ap].disconnect_device(
                device, device_location)
        else:
            print(
                f"No access point found that matches the device location for {device}.")

    def calculate_distance(self, ap_location, device_location) -> int:
        """Function to calculate the distance between a given AP
        and device given floor their corresponding floor numbers."""
        return abs(ap_location - device_location)
