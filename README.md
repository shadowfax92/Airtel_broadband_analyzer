Airtel broadband data analyzer
=========================

This is a simple python script that takes the Airtel data for a cycle and plots two graphs. One of them is "per day" (like data usage for jan 1,jan2...) data usage and second one is "day of the week" (data usage for sunday,monday...) data usage.

Python modules Required:
- matplotlib
- numpy

Usage:
Change the "input_file" parameter in the script to point to your input file.

Sample input_file:

Sat Jan 11 02:04:57 AM IST 2014 11.11 MB    1138    0

Sat Jan 11 06:51:52 PM IST 2014 1.2 GB      125321  0

Sat Jan 11 11:51:52 PM IST 2014 113.27 MB   11599   0

Sun Jan 12 12:21:52 AM IST 2014 1.53 MB     157     0

Sun Jan 12 10:36:16 AM IST 2014 244.79 MB   25067   0

Sun Jan 12 11:36:16 AM IST 2014 1.74 GB     182913  0

Sun Jan 12 03:36:17 PM IST 2014 20.91 MB    2142    0

Sun Jan 12 04:55:09 PM IST 2014 196.91 MB   20164   0

Sun Jan 12 05:55:09 PM IST 2014 578.51 MB   59240   0

Sun Jan 12 11:55:09 PM IST 2014 315.93 MB   32352   0

Mon Jan 13 12:25:09 AM IST 2014 14.83 MB    1519    0

Mon Jan 13 09:14:31 AM IST 2014 54.35 MB    5566    0

Mon Jan 13 11:14:31 AM IST 2014 3.62 MB     371     0

Mon Jan 13 08:03:39 PM IST 2014 620.78 MB   63568   0

Mon Jan 13 09:03:39 PM IST 2014 6.97 MB     714     0

Mon Jan 13 09:33:10 PM IST 2014 65.42 MB    6700    0


Column description:
  - col 2,3 cumulatively represents the date
  - col 1 respresents the day of the week
  - col 9 represents the data in 10KB

Sample Plotted graphs:
  - Date based output
![Image](https://raw.github.com/shadowfax92/Airtel_broadband_analyzer/master/date_based_output.png)
  - Day based output
![Image](https://raw.github.com/shadowfax92/Airtel_broadband_analyzer/master/day_based_output.png)



