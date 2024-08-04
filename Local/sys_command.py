import subprocess, os

def subprocess_open(command):
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='euc-kr')
    (stdoutdata, stderrdata) = popen.communicate()
    return stdoutdata, stderrdata

if __name__ == "__main__":
    if os.name == 'Windows':
        stdout, stderr = subprocess_open('dir')
    elif os.name == 'posix':
        stdout, stderr = subprocess_open('ls')
    else:
        print("OS is " + os.name)
        exit()
    print("[stdout]")
    print(stdout)
    print("[stderr]")
    print(stderr)
