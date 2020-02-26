import datetime
from typing import List

class Dataset:
    def __init__(self, measurementId: str, timestamp: datetime, values: [str]):
        self.measurementId = measurementId
        self.timestamp = datetime
        self.values = values

    def setMeasurementId(self, measurementId: str):
        self.measurementId = measurementId

    def getMeasurementId(self) -> str:
        return self.measurementId

    def setTimestmap(self, timestamp: datetime):
        self.timestamp = timestamp

    def getTimestmap(self) -> str:
        return self.timestamp

    def addValue(self, value: str):
        self.values.append(value)

    def getValues(self) -> str:
        return self.values