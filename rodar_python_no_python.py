

import os
import subprocess

with open("test2", "w") as f:
    f.write("""import time
print('start')
time.sleep(2)
print('done')""")

(readend, writeend) = os.pipe()

p = subprocess.Popen(['python', '-u', 'test2'], stdout=writeend, bufsize=0)
still_open = True
output = ""
output_buf = os.read(readend, 1).decode()
while output_buf:
    print(output_buf, end="")
    output += output_buf
    if still_open and p.poll() is not None:
        os.close(writeend)
        still_open = False
    output_buf = os.read(readend, 1).decode()