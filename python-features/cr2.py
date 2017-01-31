# encoding: utf-8

import asyncio


async def coroutine():
    print("in coroutine")
    return "result"


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()

    try:
        val = event_loop.run_until_complete(coroutine())
        print("coroutine returned %s" % val)
    finally:
        event_loop.close()
