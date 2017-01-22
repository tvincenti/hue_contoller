
import requests
import json
import time
import os
import pprint
from random import randint

try:
    from conn_info import id,ip

except:
    os.system('clear')
    ip = raw_input('Enter IP address of the hue bridge: ')
    id = raw_input('Enter the api user account: ')
    f = open( 'conn_info.py', 'w' )
    f.write('ip = ' + '\'' + ip + '\'' + '\n' )
    f.write('id = ' + '\'' + id + '\'' + '\n')
    f.close()

#Color
color_max = 65535
color_min = 0
interval = 360
light_num = raw_input('Enter the ID of the light you want to control: ')
url = 'http://' + ip + '/api/' + id + '/lights/' + light_num + '/state'

def change_light():    
    global url
    global light_num
    light_num = raw_input('Enter the ID of the light you want to control: ')
    url = 'http://' + ip + '/api/' + id + '/lights/' + light_num + '/state'

def ping_lights():
    url_ping = 'http://' + ip + '/api' + id + '/lights/'
    r = requests.get(url_ping)
    print r.status_code
    print r.text
    time.sleep(15)
     
def light_on():
    on = json.dumps({"on":True})
    r = requests.put(url,data=on)

def light_off():
    off = json.dumps({"on":False,"sat":254})
    r = requests.put(url,data=off)

def flash():
    for flash in range(0,3):
        light_on()
        time.sleep(.75)
        #print str(flash) + ' Light Response: '
        light_off()
        time.sleep(.75)
        #print str(flash) + ' Light Repsonse:'

def color_range():
    light_on()    
    for i in range(0,1):
        for x in range(color_min, color_max, interval):
            hue = json.dumps({"hue":x})
            payload = hue
            r = requests.put(url, data=payload)
            #print x

def rand_sleep():
    id = randint(0,3)
    if id == 0:
        time.sleep(.25)
    elif id == 1:
        time.sleep(.50)
    elif id == 2:
        time.sleep(.75)
    else:
        time.sleep(.1)

def manual():
    hcc = raw_input("Enter Hue Color Code(0-65535): ") 
    hue = json.dumps({"hue":int(hcc)})
    payload = hue
    r = requests.put(url,data=payload)

#def try_connect():
    

def prog_dance():
    id = 0
    while True:    
        if id == 0:
            light_off()
            time.sleep(1)
            light_on()            
        elif id == 1:
            color_red()
        elif id == 2:
            color_blue()
        elif id == 3:
            color_purple()
        elif id == 4:
            color_green()
        elif id == 5:
            color_white()
        elif id == 6:
            color_orange()
        else:
            color_white()
        id = randint(0,6)
        rand_sleep()

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
    for p in range(0,10):
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
    color = json.dumps({"hue":46920})
    r = requests.put(url,data=color)

def color_orange():
    color = json.dumps({"hue":10800})
    r = requests.put(url,data=color)

def color_pink():
    color = json.dumps({"hue":56100})
    r = requests.put(url,data=color)

def color_yellow():
    color = json.dumps({"hue":12750})
    r = requests.put(url,data=color)

def color_purple():
    color = json.dumps({"hue":49680})
    r = requests.put(url,data=color)

def color_red():
    color = json.dumps({"hue":65280})
    r = requests.put(url,data=color)

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

 
def main():
    print
    print 'TVz Hue Controller'
    print '-----------------------------------------'
    print 'Light #: ' + light_num  
    print 'Bridge Address: ' + url
    print 
    print '    Select Hue Command:'
    print 
    print '        - ping lights'
    print '        - on'
    print '        - off'
    print '        - dim'
    print '        - dim percent'
    print '        - change light'
    print
    print '        - orange'
    print '        - white'
    print '        - red'
    print '        - blue'
    print '        - yellow'
    print '        - pink'
    print '        - purple'
    print '        - green'
    print '        - manual'
    print
    print '        - dance'
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
    
    elif option == 'purple':
        light_on()
        color_purple()

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

    elif option == 'ping lights':
        ping_lights()

    elif option == 'dance':
        prog_dance()

    elif option == 'manual':
        manual()

    elif option == 'exit':
        exit()

    elif option == 'change light':
        change_light()

    elif option == 'dim':
        dim()
    else:
        print 'What the what? That is not a valid hue setting!'
        time.sleep(2)

    os.system('clear')
    return main()

if __name__ == "__main__":
    main()
