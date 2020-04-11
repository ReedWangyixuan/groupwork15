from subprocess import Popen, PIPE
import re,time,unicodedata

commit = re.compile('^commit [0-9a-z]{40}$', re.IGNORECASE)
fixes  = re.compile('^\W+Fixes: [a-f0-9]{8,40} \(.*\)$', re.IGNORECASE)

def getFixDate(commit_id,repo):
    cmd = ["git","log","--pretty=format:\"%ad\"","-1", commit_id]
    p = Popen(cmd, cwd=repo, stdout=PIPE)
    date, res = p.communicate()
    date = unicodedata.normalize(u'NFKD', date.decode(encoding="utf-8", errors="ignore"))
    dateStamp = time.mktime(time.strptime(date[:-7].strip('"'),"%a %b %d %H:%M:%S %Y"))
    return dateStamp

def getFixCommits(kernelRange, repo):
    nr_fixes = 0
    fix_commit = []
    cmd = ["git", "log", "-p", "--no-merges", kernelRange]
    p = Popen(cmd, cwd=repo, stdout=PIPE)
    data, res = p.communicate()
    data = unicodedata.normalize(u'NFKD', data.decode(encoding="utf-8", errors="ignore"))
    for line in data.split("\n"):
        if(commit.match(line)):
            cur_commit = line
        if(fixes.match(line)):
            nr_fixes += 1
            fix_commit.append(cur_commit[7:19])
            #print(cur_commit[7:19],",",line.strip()[9:16],sep="")
    print("total found fixes:",nr_fixes)
    return fix_commit

if __name__ == "__main__":
    repo = "/home/huangyiqi/nicho/linux-stable"
    fix_commit = getFixCommits("v4.9..v4.9.2", repo)
    for commit_id in fix_commit:
        dateStamp = getFixDate(commit_id, repo)
        print(dateStamp)
