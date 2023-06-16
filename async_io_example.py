import asyncio
import inspect


async def test_async_function():
    await asyncio.sleep(2)
    print("AWAIT")
    return 2
async def test_async_function2():
    await asyncio.sleep(3)
    print("NO AWAIT")
    return 2

def test_not_async_function():
    pass

# asyncio.run(test_async_function())
# print(type(test_async_function))
# print(inspect.iscoroutinefunction(test_async_function))
# print(inspect.iscoroutinefunction(test_not_async_function))

async def main():
    task = asyncio.create_task(test_async_function())
    print(type(task))
    print(type(await task))

# asyncio.run(test_not_async_function())

async def new_main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(test_async_function()) # request to db
        # task2 = tg.create_task(test_async_function2())
        print("Start load page") # run selenuim, go to page
        await task1 #await request
        print("AFTER AWAIT") #refresh page + selenium check


asyncio.run(new_main())


# await test_async_function()
# task = asyncio.create_task(test_async_function())
# await asyncio.shield(task)
