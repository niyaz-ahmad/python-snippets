#   ╻┏┓╻┏━┓╻ ╻╺┳╸   ╻ ╻╻╺┳╸╻ ╻   ╺┳╸╻┏┳┓┏━╸┏━┓╻ ╻╺┳╸   ┏━┓┏┓╻╺┳┓   
#   ┃┃┗┫┣━┛┃ ┃ ┃    ┃╻┃┃ ┃ ┣━┫    ┃ ┃┃┃┃┣╸ ┃ ┃┃ ┃ ┃    ┣━┫┃┗┫ ┃┃   
#   ╹╹ ╹╹  ┗━┛ ╹    ┗┻┛╹ ╹ ╹ ╹    ╹ ╹╹ ╹┗━╸┗━┛┗━┛ ╹    ╹ ╹╹ ╹╺┻┛   
#   ┏━╸╻ ╻╻╺┳╸   ┏━╸┏━┓┏┳┓┏┳┓┏━┓┏┓╻╺┳┓   ╻ ╻┏━┓┏┓╻╺┳┓╻  ┏━╸┏━┓
#   ┣╸ ┏╋┛┃ ┃    ┃  ┃ ┃┃┃┃┃┃┃┣━┫┃┗┫ ┃┃   ┣━┫┣━┫┃┗┫ ┃┃┃  ┣╸ ┣┳┛
#   ┗━╸╹ ╹╹ ╹    ┗━╸┗━┛╹ ╹╹ ╹╹ ╹╹ ╹╺┻┛   ╹ ╹╹ ╹╹ ╹╺┻┛┗━╸┗━╸╹┗╸

from threading import Timer
import random
import signal
import os
import atexit

exit_now: bool = False

def exit_handler():
    print(f"exit_handler(): exiting now.")

def snooze(sec_times: int)-> None:
    print(f'going to sleep for {sec_times} seconds..\n..')
    timer = Timer(sec_times, print, ['Woke up!'])
    
    signal.signal(signal.SIGINT, signal_handler)
    
    timer.start()
    
    received = input(f'press `C` key to exit and wait.. : ')
    print(f'received: {received}')
    if received == 'c' or received == 'C':
        print(f'recieved exit command. Will exit NOW!')
        os._exit(1)
    timer.cancel()

def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C!')
    print(f'I will exit now')
    os._exit(2)

        
if __name__ == "__main__":
    for i in range(4):
        print(f'\n\nPhase - {i}')
        timeout = random.randint(10, 17)
        snooze(timeout)
        
    atexit.register(exit_handler)
