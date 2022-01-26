import os
pyinstaller -F --icon "icon.ico" --onefile xxx.py

dir = input(".Py Directory: ")
file = dir[dir.rindex('\\')+1:]
dir = dir[:dir.rindex('\\')]

os.chdir(dir)
cmd = ''
cmd += 'cmd /k "'
cmd +=
os.system('cmd /k "Your Command Prompt Command"')