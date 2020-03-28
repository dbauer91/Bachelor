import datetime
from Dataset import Dataset
from typing import List

class Measurement:
    def __init__(self, measurementUuid: str, sensorId: str, timestamp: datetime):
        self.measurementUuid = measurementUuid
        self.sensorId = sensorId
        self.timestamp = datetime
        self.datasets = [Dataset]

    def setMeasurementUuid(self, measurementUuid: str):
        self.measurementUuid = measurementUuid
    
    def getMeasurementUuid(self) -> str:
        return self.measurementUuid

    def setSensorId(self, sensorId: str):
        self.sensorId = sensorId
    
    def getSensorId(self) -> str:
        return self.sensorId

    def setTimestamp(self, timestamp: str):
        self.timestamp = timestamp
    
    def getTimestamp(self) -> str:
        return self.timestamp

    def addDataset(self, dataset: Dataset):
        self.datasets.append(dataset)

    def removeDataset(self, dataset: Dataset):
        self.datasets.remove(dataset)
    
    def getDatasets(self) -> List[Dataset]:
        return self.datasets