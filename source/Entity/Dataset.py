import datetime
from typing import List

class Dataset:
    def __init__(self, sensorUuid: str, timestamp: datetime, values: [str]):
        self.sensorUuid = sensorUuid
        self.timestamp = datetime
        self.values = values

    def setSensorUuid(self, sensorUuid: str):
        self.sensorUuid = sensorUuid

    def getSensorUuid(self) -> str:
        return self.sensorUuid

    def setTimestmap(self, timestamp: datetime):
        self.timestamp = timestamp

    def getTimestmap(self) -> str:
        return self.timestamp

    def addValue(self, value: str):
        self.values.append(value)

    def getValues(self) -> str:
        return self.values