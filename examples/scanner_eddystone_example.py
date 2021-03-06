import time

from beacontools import BeaconScanner, EddystoneTLMFrame, EddystoneFilter, \
                        EddystoneUIDFrame, EddystoneURLFrame

def callback(bt_addr, rssi, packet, additional_info):
    print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))

# scan for all TLM frames of beacons in the namespace "12345678901234678901"
scanner = BeaconScanner(
    callback,
    device_filter=EddystoneFilter(namespace="12345678901234678901"),
    packet_filter=[EddystoneTLMFrame, EddystoneUIDFrame]
)
scanner.start()
time.sleep(10)
scanner.stop()

# scan for all URL frames without filtering for a specific beacon
scanner = BeaconScanner(
    callback,
    packet_filter=EddystoneURLFrame
)
scanner.start()
time.sleep(10)
scanner.stop()
