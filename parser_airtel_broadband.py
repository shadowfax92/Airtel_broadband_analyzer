import csv
import sys
import re

# Steps
#   - Dates are there in 1st and 2nd column
#   - Days are in 0th column
#   - Data used in 10KB is in 9th column

input_file='/Users/nsonti/github_projects/airtel_broadband_data_parser/airtel_usage_feb_9'

def remove_multiple_instances_from_list(list):
    new_list=[]
    for val in list:
        if val not in new_list:
            new_list.append(val)
    return new_list

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

# This function gets the data form *output_col_no when input_col_no matches input_col_value
def get_data_from_column_where(file_name,delimiter,input_col_no,input_col_value,*output_col_no):
    fh = open(file_name,'rb')
    col = []
    for line in csv.reader(fh,delimiter=' ',skipinitialspace=True):
        store_string=""
        if line[input_col_no]==input_col_value:
            for cols in output_col_no:
                store_string=store_string+str(line[cols])+" "
            tmp = store_string.rstrip()
            col.append(tmp)
    return col

def get_output_dic_day_based():
    global input_file
    day_list_tmp = get_data_from_column(input_file,' ',0)
    day_list = remove_multiple_instances_from_list(day_list_tmp)
    print str(day_list)

    for days in day_list:
        print str(days)
        tmp_day_out = map(int,get_data_from_column_where(input_file,' ',0,str(days),9))
        print str(sum(tmp_day_out)*10/1024)+" MB"
    return

def main():
    global input_file
    get_output_dic_day_based()
    #print '1st'
    #print str(get_data_from_column(input_file,' ',9))
    #print '2nd'
    #print str(get_data_from_column(input_file,' ',1,2))
    #print '3rd'
    #print str(get_data_from_column(input_file,' ',0))

main()
