import threading
import time

def print_numbers():
    print(f"Hello from {threading.current_thread().name}!")
    for i in range(1,6):
        print(f"Number: {i}")
        time.sleep(1) 
        #pause for 1 second

def print_letters():
    print(f"Hello from {threading.current_thread().name}!")
    for letter in ['A', 'B','C','D','E']:
        print(f"Letter: {letter}")
        time.sleep(1) 
        #pause for 1 second
#create threads
thread1 = threading.Thread(target=print_numbers, name="NumberThread")
thread2 = threading.Thread(target=print_letters, name="LetterThread")

#start executing
thread1.start()
thread2.start()
print(f"Is thread alive? {thread1.is_alive()}")#true
#start threads
thread1.join()
thread2.join()

print(f"Is thread alive? {thread1.is_alive()}")#false
#run functions one after another
#print_numbers()
#print_letters()

print("All tasks are complete")