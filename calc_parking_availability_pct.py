def queryDb(arrivalDeparture,currentTime,structureLat,structureLon):
    rv = None
    if arrivalDeparture == "Arrival":
        rv = -2
    if arrivalDeparture == "Departure":
        rv = 3
    return rv

def get_pct_avail(currentTime,structureLat,structureLon):
    sumArrivalHr = queryDb(arrivalDeparture="Arrival",
                           currentTime=currentTime,
                           structureLat=structureLat,
                           structureLon=structureLon)
    sumDepartureHr = queryDb(arrivalDeparture="Departure",
                           currentTime=currentTime,
                           structureLat=structureLat,
                           structureLon=structureLon)
    diffVehCountHour = sumArrivalHr - sumDepartureHr
    pct_avail = 0
    if diffVehCountHour >= 5:
        pct_avail = 10
    if diffVehCountHour <= -5:
        pct_avail = 90
    if -5 < diffVehCountHour and diffVehCountHour < 5:
        pct_avail = 90 - (diffVehCountHour + 5)*8
    return pct_avail

print get_pct_avail("20160409T1730",37,-122)