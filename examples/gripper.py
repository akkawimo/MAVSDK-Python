#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():
    drone = System()
    await drone.connect(system_address="udp://localhost:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print(f"-- Gripper Grab")
    await drone.action.gripper_grab(instance=1)
    await asyncio.sleep(1)
    print(f"-- Gripper Release")
    await drone.action.gripper_release(instance=1)

    while True:
        print("Staying connected, press Ctrl-C to exit")
        await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
