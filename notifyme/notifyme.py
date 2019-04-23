import subprocess

def notify(func_name, step):
    subprocess.call(["notify-send", '%s: %s Done.' % (func_name, step)])
    subprocess.call(['/usr/bin/canberra-gtk-play', '--id', 'bell'])
