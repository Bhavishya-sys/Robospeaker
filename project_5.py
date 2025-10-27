import os
import pyttsx3

if __name__ == '__main__':
    print ("Welcome to Robospeakerm 1.1. Created by Bhavishya")
    while True:
        x = input("what do you want to speak:")
        if x == "q":
            break
        command = f" say {x}"
        os.system(command)