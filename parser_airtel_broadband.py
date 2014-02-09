import csv
import sys
import re

# Steps
#   - Dates are there in 2nd and 3rd col
#   - Days are in 1st column
#   - Data used in 10KB is in 9th column

input_file='/Users/nsonti/github_projects/airtel_broadband_data_parser/airtel_usage_feb_9'

def get_data_from_column(file_name,delimiter,*col_no):
    fh = open(file_name,'rb')
    col = []
    for line in csv.reader(fh,delimiter=' ',skipinitialspace=True):
        store_string=""
        for cols in col_no:
            store_string=store_string+str(line[cols])+" "
        tmp = store_string.rstrip()
        col.append(tmp)

    return col

def get_output_dic_day_based():
    return

def main():
    global input_file
    print '1st'
    print str(get_data_from_column(input_file,' ',9))
    print '2nd'
    print str(get_data_from_column(input_file,' ',1,2))
    print '3rd'
    print str(get_data_from_column(input_file,' ',0))

main()
