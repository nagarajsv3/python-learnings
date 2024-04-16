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

    print('*'*108)
    check = brew_coffee()
    print('*'*108)

    #bc, tb = await asyncio.gather(brew_coffee(), toast_bagel())  ##Runs Coroutine
    batch =  asyncio.gather(brew_coffee(), toast_bagel())
    bc, tb = await batch  ##Runs Coroutine
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"brew coffee result = {bc}")
    print(f"toast bagel result = {tb}")
    print(f"elapsed time result = {elapsed_time : .2f} seconds")

async def main_rnd():
    start_time = time.time()

    print('*'*108)
    check = brew_coffee()


    check_toast = toast_bagel()
    check2 = await check
    check_toast2 = await check_toast
    
    print(check)
    print(check2)

    print(check_toast)
    print(check_toast2)
    
    print('*'*108)



    
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    #print(f"brew coffee result = {bc}")
    #print(f"toast bagel result = {tb}")
    print(f"elapsed time result = {elapsed_time : .2f} seconds")

async def main_using_tasks():
    start_time = time.time()

    #bc, tb = await asyncio.gather(brew_coffee(), toast_bagel())
    task_bc = asyncio.create_task(brew_coffee())
    task_tb = asyncio.create_task(toast_bagel())
    
    bc = await task_bc  ##Runs Coroutine
    tb = await task_tb  ##Runs Coroutine

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"brew coffee result = {bc}")
    print(f"toast bagel result = {tb}")
    print(f"elapsed time result = {elapsed_time : .2f} seconds")
    

if __name__ == '__main__':
    #asyncio.run(main())
    #asyncio.run(main_using_tasks())  ##Runs Coroutine
    asyncio.run(main_rnd())  ##a. Creates Event Loop  b.Runs Coroutine


    #await coroutine - runs the coroutine 
    #create task - creates task
    #await task - waites till the task is run

    #b, c = await asyncio.gather(brew_coffee(), toast_bagel()) - run multiple coroutines together
    #res = await brew_coffee() - run 1 coroutine 

    #asyncin.run(our_coroutine()) ##a. Creates Event Loop  b.Runs Coroutine