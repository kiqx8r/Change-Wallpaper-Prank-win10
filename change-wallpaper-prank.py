import struct
import ctypes
import urllib3
import os

os.chdir("C:/Users/Public/Pictures")

url = input('Insira URL:')
connection_pool = urllib3.PoolManager()
resp = connection_pool.request('GET',url )
f = open('file.jpg', 'wb')
f.write(resp.data)
f.close()
resp.release_conn()

SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = 'C:/Users/Public/Pictures/file.jpg'

def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64


def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)

    # When the SPI_SETDESKWALLPAPER flag is used,
    # SystemParametersInfo returns TRUE
    # unless there is an error (like when the specified file doesn't exist).
    if not r:
        print(ctypes.WinError())

change_wallpaper()
