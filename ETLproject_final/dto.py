# dto.py

class DTO:
    def __init__(self, newcountry_region, newconfirmed, newdeaths, newrecovered):
        self.country_region = newcountry_region
        self.confirmed = newconfirmed
        self.deaths = newdeaths
        self.recovered = newrecovered
    def getCoutryRegion(self):
        return self.country_region
    def getConfirmed(self):
        return self.confirmed
    def getDeaths(self):
        return self.deaths
    def getRecovred(self):
        return self.recovred
    def setCoutryRegion(self, newcountry_region):
        self.country_region = newcountry_region
    def setConfirmed(self, newconfirmed):
        self.confirmed = newconfirmed
    def setDeaths(self, newdeaths):
        self.deaths = newdeaths
    def setRecovred(self, newrecoverd):
        self.recovred = newrecoverd
        
    def __str__(self):
        return '국가: ' + self.country_region + ', 확진자: ' + str(self.confirmed) + ', 사망자: ' + str(self.deaths) + ', 완치: ' + str(self.recovred)