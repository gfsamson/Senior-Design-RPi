import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
A = ser.write('0')
A = ser.read()
print(A)
A = ser.read()
print(A)
A = ser.read()
print(A)
A = ser.read()
print(A)
A = ser.read()
print(A)
