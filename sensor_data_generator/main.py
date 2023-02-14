
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time
import math
import index

makerobo_DO = 17                    
makerobo_Buzz = 18                 
GPIO.setmode(GPIO.BCM)              
#GPIO.setwarnings(False)            


def makerobo_setup():
	ADC.setup(0x48)                      
	GPIO.setup	(makerobo_DO,GPIO.IN)    
	GPIO.setup	(makerobo_Buzz,GPIO.OUT) 
	GPIO.output	(makerobo_Buzz,1)        

# Print message 
def makerobo_Print(x):
	if x == 1:     
		print ('')
		print ('   ******************')
		print ('   *  Safe~ *')
		print ('   ******************')
		print ('')
	if x == 0:   
		print ('')
		print ('   ************************')
		print ('   * Danger Gas! *')
		print ('   ************************')
		print ('')

# loop
def makerobo_loop():
	makerobo_status = 1   
	makerobo_count = 0    
	while True:    
		print (ADC.read(0)) 
		dat = ADC.read(0)
		index.send(dat)
		makerobo_tmp = GPIO.input(makerobo_DO)  
		if makerobo_tmp != makerobo_status:     
			makerobo_Print(makerobo_tmp)        
			makerobo_status = makerobo_tmp      
		if makerobo_status == 0:                
			makerobo_count += 1                 
			
			if makerobo_count % 2 == 0:         
				GPIO.output(makerobo_Buzz, 1)
			else:
				GPIO.output(makerobo_Buzz, 0)
		else:
			GPIO.output(makerobo_Buzz, 1)      
			makerobo_count = 0                  
				
		time.sleep(0.2)                        


def destroy():
	GPIO.output(makerobo_Buzz, 1)   
	GPIO.cleanup()         


if __name__ == '__main__':
	try:
		makerobo_setup()   
		makerobo_loop()   
	except KeyboardInterrupt: 
		destroy()  