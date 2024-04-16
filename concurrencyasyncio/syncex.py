import time

def brew_coffee():
    print("Starting brew_coffee()")
    time.sleep(3)
    print("Ending brew_coffee()")
    return 30

def toast_bagel():
    print("Starting toast_bagel()")
    time.sleep(2)
    print("Ending toast_bagel()")
    return 20

def main():
    start_time = time.time()
    bc = brew_coffee()
    tb = toast_bagel()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"brew coffee result = {bc}")
    print(f"brew coffee result = {tb}")
    print(f"elapsed time result = {elapsed_time : .2f} seconds")
    

if __name__ == '__main__':
    main()