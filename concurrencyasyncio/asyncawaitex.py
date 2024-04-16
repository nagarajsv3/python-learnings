import time
import asyncio

async def brew_coffee():
    print("Starting brew_coffee()")
    await asyncio.sleep(3)
    print("Ending brew_coffee()")
    return 30

async def toast_bagel():
    print("Starting toast_bagel()")
    await asyncio.sleep(2)
    print("Ending toast_bagel()")
    return 20

async def main():
    start_time = time.time()

    #bc, tb = await asyncio.gather(brew_coffee(), toast_bagel())
    batch =  asyncio.gather(brew_coffee(), toast_bagel())
    bc, tb = await batch
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"brew coffee result = {bc}")
    print(f"toast bagel result = {tb}")
    print(f"elapsed time result = {elapsed_time : .2f} seconds")

async def main_using_tasks():
    start_time = time.time()

    #bc, tb = await asyncio.gather(brew_coffee(), toast_bagel())
    task_bc = asyncio.create_task(brew_coffee())
    task_tb = asyncio.create_task(toast_bagel())
    
    bc = await task_bc
    tb = await task_tb

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"brew coffee result = {bc}")
    print(f"toast bagel result = {tb}")
    print(f"elapsed time result = {elapsed_time : .2f} seconds")
    

if __name__ == '__main__':
    #asyncio.run(main())
    asyncio.run(main_using_tasks())