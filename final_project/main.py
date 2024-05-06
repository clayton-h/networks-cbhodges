#
# Python driver script
# that simulates WLAN
# controller functionality
#
# By: Clayton H.
#

from WLAN_controller import WLANController


def main() -> None:
    """Main driver function simulates
    a WLAN controller (device_name, floor_num).
    """
    controller = WLANController()

    print("***********************************************************\n")

    controller.add_access_point("AP1", 1)
    controller.add_access_point("AP2", 5)
    controller.add_access_point("AP3", 7)

    print("***********************************************************\n")

    controller.connect_device("Device1", 1)
    controller.connect_device("Device2", 3)
    controller.connect_device("Device3", 8)
    controller.connect_device("Device4", 1)

    print("***********************************************************\n")
    controller.print_network()
    print("***********************************************************\n")

    # controller.move_device("Device2", 1)

    controller.disconnect_device("Device1", 1)
    # controller.disconnect_device("Device2", 1)
    controller.disconnect_device("Device3", 8)
    controller.disconnect_device("Device4", 1)

    print("***********************************************************\n")
    controller.print_network()
    print("***********************************************************\n")


if __name__ == "__main__":
    main()
