import enum

class devicestate(enum.Enum):
    new_device = 1
    serialID_recorded = 2
    imei_recorded = 3
    packageID_recorded = 4
    damage_recorded = 5
    simcard_assigned = 6
    device_flashed = 7
    keys_injected = 8
    repacking_sent = 9
    warehouse_stored = 10
