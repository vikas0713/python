#!/bin/python

time = raw_input().strip()
if "AM" in time:
    time = time.replace("AM","")
    split_time = time.split(":")
    hour = split_time[0]
    if hour == "12":
        split_time[0] = "00"
        rl_time = ""+split_time[0]
        for i in split_time[1:]:
            rl_time+=":"+str(i)
        print rl_time
    else:
        print time.replace("AM","")
elif "PM" in time:
    time = time.replace("PM","")
    split_time = time.split(":")
    hour = split_time[0]
    rl_time_hour = int(hour) + 12
    if hour == "12":
        print time
    elif rl_time_hour == 24:
        split_time[0] = "00"
    else:
        split_time[0] = str(rl_time_hour)
    rl_time = ""+split_time[0]
    for i in split_time[1:]:
        rl_time+=":"+str(i)
    print rl_time