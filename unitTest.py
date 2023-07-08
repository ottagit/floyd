# import module into test file
from vehicleList import scan_vehicles

honda = ["premacy", "fit", "civic"]


def test_parking_list():
    assert scan_vehicles(honda) == ["fit", "civic"]

