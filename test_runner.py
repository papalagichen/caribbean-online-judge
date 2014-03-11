import subprocess

ID = 1013
SOURCE = './{0}/source.py'.format(ID)
TEST = __import__('{0}.test'.format(ID))
INPUT = TEST.test.INPUT.strip()
OUTPUT = TEST.test.OUTPUT.strip()

child = subprocess.Popen(['python', SOURCE], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

for i in INPUT.split('\n'):
    child.stdin.write(i + '\n')
child.stdin.flush()

answer = ''
for o in OUTPUT.split('\n'):
    line = child.stdout.readline()
    answer += line
answer = answer.strip()

if cmp(OUTPUT, answer):
    print('=== EXPECT ===\n{0}\n=============='.format(OUTPUT))
    print('==== GOT =====\n{0}\n=============='.format(answer))
else:
    print('ACCEPT')