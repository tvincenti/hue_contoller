
import requests
import json
import time
import os

os.system('clear')

url = 'http://10.0.0.62/api/aQuXs1CCrJsRswx8IYuocTTQKS0P5NqK1vP1VljD/lights/4/state'

#Color

color_max = 65535
color_min = 0
interval = 360
 
def light_on():
    on = json.dumps({"on":True})
    r = requests.put(url,data=on)
    #print 'Light Response: ' + r.content

def light_off():
    off = json.dumps({"on":False})
    r = requests.put(url,data=off)
    #print 'Light Response: ' + r.content

def flash():
    for flash in range(0,10):
        light_on()
        time.sleep(.75)
        #print str(flash) + ' Light Response: '
        light_off()
        time.sleep(.75)
        #print str(flash) + ' Light Repsonse:'

def color_range():
    light_on()    
    for x in range(color_min, color_max, interval):
        hue = json.dumps({"hue":x})
        payload = hue
        r = requests.put(url, data=payload)
        #print x
        #print '---------'
        #print r  
        #print r.content

def prog_panic():
    for p in range(0,8):
        light_on()
        color_red()
        time.sleep(1)
        color_white()
        time.sleep(1)

def prog_america():
    color_red()
    time.sleep(1)
    color_white()
    time.sleep(1)
    color_blue()

def prog_five_o():
    for pig in range(0,10):
        light_on()
        color_red()
        time.sleep(.33)
        color_blue()
        time.sleep(.33)

def color_white():
    color = json.dumps({"hue":32040})
    r = requests.put(url,data=color)

def color_green():
    color = json.dumps({"hue":25500})
    r = requests.put(url,data=color)

def color_blue():
    color = json.dumps({"hue":46920,"sat":254})
    r = requests.put(url,data=color)
    #print r
    #print r.content

def color_orange():
    color = json.dumps({"hue":10800})
    r = requests.put(url,data=color)

def color_pink():
    color = json.dumps({"hue":56100})
    r = requests.put(url,data=color)

def color_yellow():
    color = json.dumps({"hue":12750})
    r = requests.put(url,data=color)

def color_red():
    color = json.dumps({"hue":65280,"sat":254})
    r = requests.put(url,data=color)
    #print r
    #print r.content

def dim():
    print 'Select a dim setting: - low, - medium, - high, - full'
    flag = raw_input("- ") 
    
    if flag == 'low':
        low = json.dumps({"bri":74})
        r = requests.put(url,data=low)
    elif flag == 'medium':
        med = json.dumps({"bri":134})
        r = requests.put(url,data=med)
    elif flag == 'high':
        high = json.dumps({"bri":194})
        r = requests.put(url,data=high)
    elif flag =='full':
        full = json.dumps({"bri":254})
        r = requests.put(url,data=full)
    else:
        print 
        print 'What the what? That is not a valid dim setting!'
        print
        dim()

def dim_percent():
    percent = raw_input("Enter a value from 1-100: - ")

    try:
        percent_int = int(percent)
        if 1 <= percent_int <= 100:
            percent_code = percent_int * 2.54
            percent_final = json.dumps({"bri":int(percent_code)})
            r = requests.put(url,data=percent_final)
    except:
        print 'That is not logical, that is not an integer!'
        time.sleep(2)
        dim_percent()       
 
def menu():
    print
    print 'TVz Hue Controller - v1.0 '
    print '-----------------------------------------'
    print 
    print '    Select Hue Command:'
    print
    print '        - on'
    print '        - off'
    print '        - dim'
    print '        - dim percent'
    print
    print '        - orange'
    print '        - white'
    print '        - red'
    print '        - blue'
    print '        - yellow'
    print '        - pink'
    print '        - green'
    print
    print '        - flash'
    print '        - five o'
    print '        - america' 
    print '        - color range'
    print '        - panic'
    print 
    print '        - exit'
    print
    print '-----------------------------------------'

    option = raw_input("-  ")
    
    if option == 'panic':
        prog_panic()
    
    elif option == 'dim percent':
        dim_percent()

    elif option == 'america':
        prog_america()

    elif option == 'orange':
        light_on()
        color_orange()
    
    elif option == 'white':
        light_on()
        color_white()

    elif option == 'green':
        light_on()
        color_green()
 
    elif option == 'pink':
        light_on()
        color_pink()

    elif option == 'yellow':
        light_on()
        color_yellow()

    elif option == 'blue':
        light_on()
        color_blue()
    
    elif option == 'red':
        light_on()
        color_red()
    
    elif option == 'flash':
        flash()
        light_on()
    
    elif option == 'on':
        light_on()

    elif option == 'off':
        light_off()

    elif option == 'five o':
        prog_five_o()
        
    elif option == 'color range':
        color_range()

    elif option == 'exit':
        exit()

    elif option == 'dim':
        dim()
    else:
        print 'What the what? That is not a valid hue setting!'
        time.sleep(2)

    os.system('clear')
    return menu()

menu()
