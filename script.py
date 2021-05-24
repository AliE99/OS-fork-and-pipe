import subprocess
for i in range(20):
    status = subprocess.call(["gcc","main.c"])
    if status == 0:
        print(subprocess.check_output("./a.out").decode('utf-8'))
    else:
        print("Failed to compile")