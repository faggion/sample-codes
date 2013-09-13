LOOP = 50
OFF2ON = 10
ON2OFF = 10

import android
import urllib,urllib2,random,time

def make_random_num(count):
    return ''.join(map(lambda x: str(random.randint(1,9)), range(count)))

droid = android.Android()

for i in range(LOOP):
    # to offline
    droid.toggleAirplaneMode()
    print("offline...")
    time.sleep(OFF2ON)
    # to online
    droid.toggleAirplaneMode()
    print("online...")
    time.sleep(ON2OFF)
    print("execute something ...")



