#!/usr/bin/python3
import os
import shlex

def execute_command(command):
    # Split the command into arguments
    args = shlex.split(command)
    
    # Execute the command
    try:
        result = os.system(command)
        return result
    except Exception as e:
        return str(e)

def main():
    while True:
        # Display a prompt
        command = input(">> ")
        
        # Exit the interpreter
        if command.lower() in ['exit', 'quit']:
            print("Exiting the command interpreter.")
            break
        
        # Execute the command
        output = execute_command(command)
        
        # Print the output
        if output != 0:
            print(f"Error: {output}")

if __name__ == "__main__":
    main()