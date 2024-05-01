''' Code by kinza'''

import sys, time
import sevseg

try:
    while True:
        print('\n'* 60)
        current_time=time.localtime()
        hour=str(current_time.tm_hour % 12)
        if hour=='0':
            hour='12'
        minutes=str(current_time.tm_min)
        seconds=str(current_time.tm_sec)

        hours_digits=sevseg.getSevSegStr(hour,2)
        htop_row, hmiddle_row, hbuttom_row=hours_digits.splitlines() 


        min_digits=sevseg.getSevSegStr(minutes,2)
        mtop_row, mmiddle_row, mbuttom_row=min_digits.splitlines()

        sec_digits=sevseg.getSevSegStr(seconds,2)
        stop_row, smiddle_row, sbuttom_row=sec_digits.splitlines()

        # now we will display the digits
        print(f"{htop_row}      {mtop_row}       {stop_row}")
        print(f"{hmiddle_row}    * {mmiddle_row}     * {smiddle_row}"  )
        print(f"{hbuttom_row}    * {mbuttom_row}     * {sbuttom_row}")
        
        print("\nPress Ctrl+C to quit")

        while True:
            time.sleep(1)  
            if time.localtime().tm_sec!= current_time.tm_sec:
                break

except KeyboardInterrupt:
    print("Code by Kinza")



