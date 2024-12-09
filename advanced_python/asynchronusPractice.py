import asyncio
import time


async def helper(id, sec):
    print(f"In helper function {id}")
    await asyncio.sleep(sec)
    print(f"Waiting completed for {id}")
    return id



async def main():
    start = time.time()
    print("Entered coroutine")
    # tasks = []
    # async with asyncio.TaskGroup()as tg:
    #     for i,j in enumerate([4,4,4,4], start=1):
    #         temp = tg.create_task(helper(i,j))
    #         tasks.append(temp)
    res = await asyncio.gather(helper(1,4), helper(2,2), helper(3,3), helper(4,1))
    print("End of the coroutine")
    # print(type(res)) --> list
    print(res)
    end = time.time()
    print(end-start)


asyncio.run(main())