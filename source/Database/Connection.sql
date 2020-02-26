CREATE TABLE [IF NOT EXISTS] connections (
    sensorid INTEGER PRIMARY KEY,
    connectiontype TEXT NOT NULL,
    connectionname TEXT NOT NULL,
    address TEXT NOT NULL,
)