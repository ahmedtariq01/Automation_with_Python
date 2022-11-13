import subprocess

subprocess.run(['date'])

subprocess.run(['sleep', '2'])

result = subprocess.run(['ls','this_file_does_not_exist'])

result = subprocess.run(['host', '8.8.8.8'])
print(result.returncode)
print(result.stdout)
print(result.stdout.decode().split())
result = subprocess.run(['rm', 'does_not_exist'], capture_output=True)

