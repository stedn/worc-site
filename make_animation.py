import os

v_x_start = 93
v_y_start = 49
v_x_mid = 94
v_y_mid = 36
v_x_end = 128
v_y_end = 38
v_x_inc = (v_x_mid-v_x_start)/20
v_y_inc = (v_y_mid-v_y_start)/20
v_x = v_x_start
v_y = v_y_start


x_start = 94
y_start = 90
x_mid = 131
y_mid = 71
x_end = 185
y_end = 95
x_inc = (x_mid-x_start)/60
y_inc = (y_mid-y_start)/60
x = x_start
y = y_start
for n in range(60):
    cmd1 = f'sed s#tst/0000.png#tst/{n:04}.png#g truck_animator_tst.svg | sed s/90.604576/{x}/g | sed s/89.336151/{y}/g | sed s/127.54842/{v_x}/g | sed s/38.246628/{v_y}/g > svg{n:04}.svg'
    os.system(cmd1)
    cmd2 = f'inkscape svg{n:04}.svg --export-filename png{n:04}.png'
    os.system(cmd2)
    x += x_inc
    y += y_inc
    v_x += v_x_inc
    v_y += v_y_inc
    if n==20:
        v_x_inc = (v_x_end-v_x_mid)/40
        v_y_inc = (v_y_end-v_y_mid)/40
x_inc = (x_end-x_mid)/60
y_inc = (y_end-y_mid)/60
for n in range(60):
    cmd1 = f'sed s#tst/0000.png#tst/{59-n:04}.png#g truck_animator_tst.svg | sed s/90.611111/{x}/g | sed s/89.311111/{y}/g > svg{60+n:04}.svg'
    os.system(cmd1)
    cmd2 = f'inkscape svg{60+n:04}.svg --export-filename png{60+n:04}.png'
    os.system(cmd2)
    x += x_inc
    y += y_inc
# os.system('convert png0* truck_animation.gif')

# insert

import os

k = 120
x_start = 184
y_start = 72
x_end = 107
y_end = 115
x_inc = (x_end-x_start)/k
y_inc = (y_end-y_start)/k
x = x_start
y = y_start
x0 = 350
y0 = 150
x0_inc = -3.55*(196-115)/k
y0_inc = -3.55*(78-124)/k
xw = 1920/2.2
yw = 1080/2.2
for n in range(k):
    cmd1 = f'sed s#png0119.png#png{n:04}.png#g road.svg | sed s/183.96089/{x}/g | sed s/72.750175/{y}/g > nyroad{n:04}.svg'
    os.system(cmd1)
    cmd2 = f'inkscape nyroad{n:04}.svg --export-area={int(x0)}:{int(y0)}:{int(x0+xw)}:{int(y0+yw)} --export-filename myroad{n:04}.png'
    os.system(cmd2)
    x0 += x0_inc
    y0 += y0_inc
    x += x_inc
    y += y_inc
os.system('convert myroad* -delay 5 road_animation.gif')
