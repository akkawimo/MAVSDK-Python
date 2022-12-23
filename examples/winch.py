#!/usr/bin/env python3

import asyncio
from mavsdk import System
from mavsdk.action import Winch


async def run():
    drone = System()
    await drone.connect(system_address="udp://localhost:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    await drone.action.do_winch(instance=0, action=Winch.LOAD_LINE, release_length=0.0, release_rate=0.0)

    while True:
        # print("Staying connected, press Ctrl-C to exit")
        await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
