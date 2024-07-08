import subprocess

def stop_abnormal_code(process_name):
    # Stop the process by name using system commands
    try:
        subprocess.run(['killall', '-9', process_name], check=True)
        print(f"Stopped process: {process_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping process: {e}")

# Example usage (replace with actual detection and process name)
detected_abnormal_code = "suspect_process"
stop_abnormal_code(detected_abnormal_code)

# Scramble script example (to prevent future execution)
def create_scramble_script(process_name):
    with open(f"scramble_{process_name}.sh", 'w') as f:
        f.write(f"#!/bin/bash\n")
        f.write(f"echo 'Script to disable {process_name} on next startup'\n")
        f.write(f"chmod -x {process_name}\n")

create_scramble_script(detected_abnormal_code)