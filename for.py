# create a list of vehicles
toyota = ["premio", "corolla", "markX"]
mazda = ["demio", "cx5", "cx6"]
honda = ["premacy", "fit", "civic"]
# use a for loop to iterate the vehicle collection


def scan_vehicles(vehicle_list):
    for vehicle in vehicle_list:
        if len(vehicle) < 7:
            print(vehicle)


scan_vehicles(toyota)

