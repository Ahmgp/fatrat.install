import subprocess
subprocess.call("git clone https://github.com/Screetsec/TheFatRat.git",shell=True)
subprocess.call("cd TheFatRat",shell=True)
subprocess.call("chmod +x setup.sh",shell=True)
subprocess.call("./setup.sh",shell=True)
subprocess.call("cd TheFatRat",shell=True)
subprocess.call("./update && chmod +x setup.sh && ./setup.sh",shell=True)

