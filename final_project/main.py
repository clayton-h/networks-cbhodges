#
# Python driver script
# that simulates WLAN
# controller functionality
#
# By: Clayton H.
#

import time
from WLAN_controller import WLANController


def main() -> None:
    # (device_name, floor_number)
    controller = WLANController()

    controller.add_access_point("AP1", 1)
    controller.add_access_point("AP2", 5)
    controller.add_access_point("AP3", 7)

    print('\t')

    controller.connect_device("Device1", 1)
    controller.connect_device("Device2", 3)
    controller.connect_device("Device3", 8)
    controller.connect_device("Device4", 1)

    print('\t')
    controller.print_network()
    print('\t')

    controller.disconnect_device("Device1", 1)
    controller.disconnect_device("Device3", 8)
    controller.disconnect_device("Device4", 1)

    print('\t')
    controller.print_network()
    print('\t')


if __name__ == "__main__":
    main()
