import os
import time
import datetime
import subprocess
import msvcrt

# scanner setting
width = 210
height = 297
dpi = 600
color = 'RGB'
format = 'JPG'
output_file = 'scan'

path = r'C:\Users\CorporateDrone\Desktop\scanner'
scan_path = r'C:\Users\CorporateDrone\Desktop\scanner\output'


def timestamp():
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, '%Y%m%d_%H%M%S')


def compile_cmd():
    # https://github.com/nagimov/wia-cmd-scanner/releases
    #wia-cmd-scanner.exe /w 210 /h 297 /dpi 600 /color RGB /format JPG /output test600.jpg

    output_file = 'scan_' + timestamp() + '.jpg'
    cmd = r'{path}\wia-cmd-scanner.exe /w {w} /h {h} /dpi {dpi} /color {clr} /format {frmt} /output {out}'.format(
            path = path,
            w = width,
            h = height,
            dpi = dpi,
            clr = color,
            frmt = format,
            out = scan_path + '\\' + output_file)
    return cmd


while True:
    os.system('cls')
    os.system('color 2')
    print('Pripraven skenovat.')
    print('Stiskni klavesu.')
    c = msvcrt.getch()
    if c == b'q':
        exit()  
    
    os.system('cls')
    os.system('color 4')
    subprocess.call(compile_cmd(), shell=True)

    print('\n---------------------------------------\nDokonceno')
    print('Pripravuji dalsi')
    time.sleep(5)
