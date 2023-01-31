#!/usr/bin/env python3

import asyncio
from mavsdk import System
from mavsdk.telemetry_server import DistanceSensor


async def run():
    # Init the drone
    drone = System()
    await drone.connect(system_address="udp://:14540")

    while True:
        distance_sensor = DistanceSensor(0.1, 25.0, 16.0)
        print("Sending message: " + str(distance_sensor))
        await drone.telemetry_server.publish_distance_sensor(distance_sensor)
        await asyncio.sleep(1)


if __name__ == "__main__":
    # Start the main function
    asyncio.ensure_future(run())

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()
