import os
import subprocess

def displayOut(result):
    '''
    Display the output of a subprocess' result
    '''
    if result.stdout:
        print(result.stdout.decode())


def displayErr(result):
    '''
    Display the error of a subprocess' result
    '''
    if result.stderr:
        print(result.stderr.decode())


def execCommand(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        displayOut(result)
        displayErr(result)
    except FileNotFoundError:
        print("Command not found")


def processToFile(command, output_file):
    with open(output_file, "w") as f_out:
        result = subprocess.run(command, stdout=f_out, stderr=subprocess.PIPE)
        displayErr(result)
    

def processFromFile(command, input_file):
    with open(input_file, "r") as f_in:
        result = subprocess.run(command, stdin=f_in, stderr=subprocess.PIPE)
        displayErr(result)


def processPipes(commands):
    '''
    Handle piping between commands 
    (i.e. output of a process is input of another)
    '''
    processes = []
    for idx, cmd in enumerate(commands):
        cmd_components = cmd.split()
        # First command: output to pipe
        if idx == 0:
            processes.append(subprocess.Popen(cmd_components, stdout=subprocess.PIPE))
        # Following commands: takes input from the previous pipe and output to the next
        else:
            processes.append(subprocess.Popen(cmd_components, stdin=processes[-1].stdout, stdout=subprocess.PIPE))

    # Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached
    output, error = processes[-1].communicate()
    if output:
        print(output.decode())
    if error:
        print(error.decode())


def handleCommands(command):
    components = command.split()

    # Redirect to output file
    if '>' in components:
        redirect_idx = components.index('>')
        cmd = components[:redirect_idx]
        output_file = components[redirect_idx + 1]
        processToFile(cmd, output_file)
        return

    # Redirect to input file
    if '<' in components:
        redirect_idx = components.index('<')
        cmd = components[:redirect_idx]
        input_file = components[redirect_idx + 1]
        processFromFile(cmd, input_file)
        return

    # Handle piping
    if '|' in command:
        commands = [cmd.strip() for cmd in command.split('|')]
        processPipes(commands)
        return

    execCommand(components)


def main():
    while True:
        try: 
            command = input("Enter a command: ")
            if command.lower() == 'q':
                break
            handleCommands(command)
        except KeyboardInterrupt:
            print("\nType 'q' to quit.")
    

if __name__ == "__main__":
    main()