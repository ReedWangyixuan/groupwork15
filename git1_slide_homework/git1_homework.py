from subprocess import Popen, PIPE
import unicodedata

def execute_gitcmd(kernelRange, path, filename):
    cmd = ["git", "log", "--stat", "--oneline", "--follow",kernelRange,filename]
    p = Popen(cmd, cwd=path, stdout=PIPE)
    data, res = p.communicate()
    data = unicodedata.normalize(u'NFKD', data.decode(encoding="utf-8", errors="ignore"))
    return data

def write_txtfile(data):
    res_file = open('git1_result.txt',mode='w')
    res_file.write(data)

if __name__ == "__main__":
    kernelRange = "v4.4..v4.5"
    path = "/home/huangyiqi/nicho/linux-stable"
    filename = "kernel/sched/core.c"
    data = execute_gitcmd(kernelRange, path, filename)
    # print(data) #If you want to print the result of the git command.
    write_txtfile(data)

