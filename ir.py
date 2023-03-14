import RPi.GPIO as io

io.setmode(io.BOARD)

io.setup(3,io.OUT)
io.setup(5,io.IN)

while 1:
    if (io.input(5)==False):
        io.output(3,True)
        print('Object detected')
    else:
        print('Object removed')
        io.output(3,False)