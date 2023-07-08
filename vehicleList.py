# create a list of vehicles
toyota = ["premio", "corolla", "markX"]
mazda = ["demio", "cx5", "cx6"]
# use a for loop to iterate the vehicle collection

parkingList = []


def scan_vehicles(vehicle_list):
    for vehicle in vehicle_list:
        if len(vehicle) < 7:
            parkingList.append(vehicle)
    return parkingList

