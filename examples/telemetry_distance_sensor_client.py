#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():
    # Init the drone
    drone = System()
    await drone.connect(system_address="udp://:14540")

    # Start the tasks
    asyncio.ensure_future(print_distance_sensor(drone))


async def print_distance_sensor(drone):
    async for distance_sensor in drone.telemetry.distance_sensor():
        print(f"Current distance [m]: {distance_sensor.current_distance_m}")

if __name__ == "__main__":
    # Start the main function
    asyncio.ensure_future(run())

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()
