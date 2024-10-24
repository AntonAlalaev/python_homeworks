import asyncio


async def start_strongman(name, power):
    print(f"Силач {name} начал соревноваться")
    for i in range(1, 6):
        await asyncio.sleep(5 / power)
        print(f" Силач {name} поднял шар # {i}")
    print(f"Силач {name} закончил соревнования")


async def start_tournament():
    print("Турнир начался...")
    task1 = asyncio.create_task(start_strongman("Pasha", 3))
    task2 = asyncio.create_task(start_strongman("Denis", 4))
    task3 = asyncio.create_task(start_strongman("Appolon", 5))
    await task1
    await task2
    await task3
    print("Турнир закончился...")


asyncio.run(start_tournament())
