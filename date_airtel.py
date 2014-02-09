import sys
import os
import commands

base_1="cat airtel_usage_feb_9 | grep "
base_2=" | awk 'BEGIN {sum=0;} {sum=sum+$10} END {print (sum*10)/(1024)}'" 
days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
for day in days:
    command = base_1+str(day)+base_2
    #print "Command was : "+str(command)
    stdout = commands.getoutput(command) 
    print str(day)+" : "+str(stdout)+" MB"
