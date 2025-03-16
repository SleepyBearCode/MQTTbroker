from . import mqttWindmill
from . import mqttSolar
import subprocess
import platform
import time

def run_script_in_terminal(script_path, terminal_command):
    if platform.system() == "Windows":
        subprocess.Popen(["start", "cmd", "/k", f"{terminal_command} {script_path}"], shell=True)
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        
        subprocess.Popen(["xterm", "-e", f"{terminal_command} {script_path}"])
    else:
        print("Unsupported operating system")
        
python_interpreter = 'python'

script_paths = ['windmolen_mqtt\Windmill_send_and_receive.py', 'Zonnepaneel_mqtt\Zonnepaneel_send_and_receive.py', 'sensor\powermanager.py', 'sensor\Sensorwindmolen.py']

done = 0 

for script_path in script_paths:
    if done != 4:
        run_script_in_terminal(script_path, python_interpreter)
        time.sleep(2)  
        done += 1 
