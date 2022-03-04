import enum

class devicestate(enum.Enum):
    new_device = 1
    serialID_recorded = 2
    imei_recorded = 3
    box_recorded = 4
    crate_recorded = 5
    damage_recorded = 6
    simcard_assigned = 7
    device_flashed = 8
    key_injected = 9
    repacking_sent = 10
    warehouse_stored = 11

    def damage_state(isDamaged):
        if isDamaged:
            return 0
        else:
            return 1
