import os
import subprocess
from sound import Sound


def shutdown():
    os.system('shutdown /s')


def restart():
    os.system('shutdown /r')


def volume_up():
    Sound.volume_up()


def volume_down():
    Sound.volume_down()


def volume_mute():
    Sound.mute()


def start_preset(path):
    subprocess.Popen(path, shell=True)
