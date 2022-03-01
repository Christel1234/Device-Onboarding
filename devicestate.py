import enum

class devicestate(enum.Enum):
    device_received = 1
    serialID_recorded = 2
    package_recorded = 3
    damage_recorded = 4
    simcard_assigned = 5
    imei_recorded = 6
    device_flashed = 7
    keys_injected = 8
    sent_for_repacking = 9
    stored_in_warehouse = 10
