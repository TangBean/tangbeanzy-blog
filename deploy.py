import subprocess
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')

commands = [
    'hugo -D',
    'git add ./',
    f'git commit -m {today}',
    'git push origin main'
]

for command in commands:
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    if output:
        print("Output: ", output.decode())
    if error:
        print("Error: ", error.decode())
