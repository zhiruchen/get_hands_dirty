# encoding: utf-8

import asyncio
import time


async def outer():
    print("in outer")

    print("waiting for phase1")
    result1 = await phase1()

    print("waiting for phase2")
    result2 = await phase2(result1)

    return result1, result2


async def phase1():
    print("in phase1")
    time.sleep(1)
    return "PHASE1"


async def phase2(arg):
    print("in phase2")
    time.sleep(2)
    return "PHASE2: %s" % arg


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        val = event_loop.run_until_complete(outer())
        print("return value: ", val)
    finally:
        event_loop.close()
