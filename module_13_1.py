import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task_one = asyncio.create_task(start_strongman('Pasha', 3))
    task_two = asyncio.create_task(start_strongman('Denis', 4))
    task_three = asyncio.create_task(start_strongman('Apollon', 5))
    await task_one
    await task_two
    await task_three

asyncio.run(start_tournament())
