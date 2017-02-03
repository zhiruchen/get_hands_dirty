import asyncio


@asyncio.coroutine
def count_down(number, n):
    while n > 0:
        print("T-minus", n, "({})".format(number))
        yield from asyncio.sleep(1)
        n -= 1


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(count_down("A", 2)),
             asyncio.ensure_future(count_down("B", 3))]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
