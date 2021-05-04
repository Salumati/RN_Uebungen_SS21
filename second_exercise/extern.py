from station import Station
from station_visit import StationVisit
from config import customerK1SpawnTime, customerK2SpawnTime

entrance = Station("Eingang")
baker = Station("Bäcker", 10)
sausage = Station("Wurst", 30)
cheese = Station("Käse", 60)
checkout = Station("Kasse", 5)
outrance = Station("Ausgang")
stationVisitsK1 = [StationVisit(entrance, customerK1SpawnTime), StationVisit(baker, 10, 10, 10), StationVisit(
            sausage, 30, 5, 10), StationVisit(cheese, 45, 3, 5), StationVisit(checkout, 60, 30, 30), StationVisit(outrance, 0)]
stationVisitsK2 = [StationVisit(entrance, customerK2SpawnTime), StationVisit(
    sausage, 30, 2, 5), StationVisit(checkout, 60, 3, 20), StationVisit(baker, 3, 20), StationVisit(outrance, 0)]

def stationVisitsCopy(stationVisits):
    res = []
    for stationVisit in stationVisits:
        res.append(stationVisit.copyShallow())
    print(res)
    return res