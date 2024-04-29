#
# Python script that simulates
# a WLAN controller
#
# By: Clayton H.
#

class AccessPoint:
    def __init__(self, name) -> None:
        self.__name = name
        self.__connected_devices = []

    def connect_device(self, device) -> None:
        self.__connected_devices.append(device)
        print(f"Device {device} connected to Access Point {self.__name}.")

    def disconnect_device(self, device) -> None:
        if device in self.__connected_devices:
            self.__connected_devices.remove(device)
            print(
                f"Device {device} disconnected from Access Point {self.__name}.")


class WLANController:
    def __init__(self) -> None:
        self.__access_points = {}

    def add_access_point(self, name) -> None:
        if name not in self.__access_points:
            self.__access_points[name] = AccessPoint(name)
            print(f"Access Point {name} added to WLAN Controller.")

    def connect_device(self, device, ap_name) -> None:
        if ap_name in self.__access_points:
            self.__access_points[ap_name].connect_device(device)
        else:
            print(f"Access Point {ap_name} not found.")

    def disconnect_device(self, device, ap_name) -> None:
        if ap_name in self.__access_points:
            self.__access_points[ap_name].disconnect_device(device)
        else:
            print(f"Access Point {ap_name} not found.")


def main() -> None:
    controller = WLANController()

    controller.add_access_point("AP1")
    controller.add_access_point("AP2")

    controller.connect_device("Device1", "AP1")
    controller.connect_device("Device2", "AP2")

    controller.disconnect_device("Device1", "AP1")


if __name__ == "__main__":
    main()
