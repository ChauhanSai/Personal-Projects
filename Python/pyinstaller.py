import subprocess


# pyinstaller -F --icon "icon.ico" --onefile xxx.py

def pyinstallerIcon(loc, icon):
    """
    Takes directory, *loc*, and uses *icon* as icon.
    :type loc: basestring
    :type icon: basestring
    """
    file, dir = getDir(loc)
    args = ['pyinstaller', '-F', '--icon', icon, '--onefile', file]
    print(' '.join(args))
    subprocess.run(args, cwd=dir)


def pyinstaller(loc):
    """
    Takes directory, *loc*, and uses 'icon.ico' as icon.
    :type loc: basestring
    """
    file, dir = getDir(loc)
    args = ['pyinstaller', '-F', '--icon', '"icon.ico"', '--onefile', file]
    print(' '.join(args))
    subprocess.run(args, cwd=dir)


def getDir(loc):
    """
    Takes full directory returns file & working directory.
    :rtype: tuple
    :type loc: basestring
    """
    file = loc[loc.rindex('\\') + 1:]
    dir = loc[:loc.rindex('\\') + 1]

    return file, dir


dirInput = input("Relative Python\\\\ Directory: ")
icoInput = input("Icon File (Empty for icon.ico): ")
if icoInput == '':
    pyinstaller(dirInput)
else:
    pyinstallerIcon(dirInput, icoInput)

again = input("Run again? (true/false): ")
if again:
    if icoInput == '':
        pyinstaller(dirInput)
    else:
        pyinstallerIcon(dirInput, icoInput)
