import serial
ser = serial.Serial('/dev/ttyACM0',9600) #initializes serial reading
while True:
  if(ser.inWaiting()>0):  #Checks if there is data to read
    myData=ser.readline() #reads data and stores in myData variable
    print(myData)
