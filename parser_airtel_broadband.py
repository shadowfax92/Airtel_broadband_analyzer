#!/usr/bin/python
import csv
import sys
import re 
import pylab as pl

# Steps
#   - Dates are there in 1st and 2nd column
#   - Days are in 0th column
#   - Data used in 10KB is in 9th column

input_file='/Users/nsonti/github_projects/airtel_broadband_data_parser/data_feb_12.txt'

month_number_dict = {'Jan': 1, 'Feb' : 2, 'Mar' : 3, 'Apr' : 4, 'May' : 5, 'Jun' :6, 'Jul' : 7, 'Aug' : 8, 'Sep' : 9, 'Oct' : 10, 'Nov' : 11, 'Dec' : 12}
day_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def plot_graph(input_dict, graph_type, out_file_name="Default.pdf"):
    x_axis=[]
    y_axis=[]
    sorted_date_dict = {} # indexed by key like 'Jun 26' = 626. Value is June 26
    if graph_type == "date":
        for key in input_dict.keys():
            month, date = key.split(' ')
            new_key = int(str(month_number_dict[month])+str(date))
            sorted_date_dict[new_key] = key 
        print sorted_date_dict

        for key in sorted(sorted_date_dict.keys()):
            if sorted_date_dict[key] in input_dict:
                x_axis.append(sorted_date_dict[key])
                y_axis.append(input_dict[sorted_date_dict[key]])

    elif graph_type == "day": # for the day case
        for day in day_list:
            if day in input_dict:
                x_axis.append(str(day))
                y_axis.append(input_dict[day])
            else:
                x_axis.append(str(day))
                y_axis.append(0)

    else:
        x_axis=input_dict.keys()
        y_axis=input_dict.values()

    int_x_axis=range(len(x_axis))
    print 'input dict : '+str(input_dict)
    print 'x_axis : '+str(x_axis)
    print 'y_axis : '+str(y_axis)

    fig = pl.figure()
    ax = pl.subplot(111)
    #pl.plot(range(len(x_axis)),y_axis,width=100)
    pl.ylabel('MB',fontsize='20')
    pl.xlabel('Time',fontsize='20')
    pl.subplots_adjust(bottom=0.25)
    pl.xticks(range(len(x_axis)),x_axis,rotation='vertical')
    ax.bar(range(len(x_axis)),y_axis,align='center')
    #pl.show()
    pl.savefig(out_file_name)


    #fig = pl.figure()
    #ax = pl.subplot(111)
    #ax.bar(range(len(x_axis)),y_axis)
    #pl.savefig(out_file_name)
    return

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

# custom function to get data for each date like Feb 01, Jan 29
def custom_get_data_from_column_where(file_name,delimiter,input_col_month,input_col_date,input_col_value,*output_col_no):
    fh = open(file_name,'rb')
    col = []
    for line in csv.reader(fh,delimiter=' ',skipinitialspace=True):
        store_string=""
        if str(line[input_col_month]+" "+line[input_col_date])==input_col_value:
            for cols in output_col_no:
                store_string=store_string+str(line[cols])+" "
            tmp = store_string.rstrip()
            col.append(tmp)
    return col

def get_output_dic_day_based():
    global input_file
    out_dict={}
    day_list_tmp = get_data_from_column(input_file,' ',0)
    day_list = remove_multiple_instances_from_list(day_list_tmp)
    #print str(day_list)

    for days in day_list:
        tmp_day_out = map(int,get_data_from_column_where(input_file,' ',0,str(days),9))
        out_val= sum(tmp_day_out)*10/1024
        print str(days)+" : "+str(sum(tmp_day_out)*10/1024)+" MB"
        out_dict[str(days)]=out_val

    plot_graph(out_dict, "day", "my_day_based_output")
    return

def get_output_dic_date_based():
    global input_file
    out_dict={}
    date_list_tmp = get_data_from_column(input_file,' ',1,2)
    date_list = remove_multiple_instances_from_list(date_list_tmp)
    #print 'Date list\n'+str(date_list)
    for date in date_list:
        tmp_date_out = map(int, custom_get_data_from_column_where(input_file,' ',1,2,str(date),9))
        print str(date)+" : "+str(sum(tmp_date_out)*10/1024)+" MB"
        out_dict[str(date)]=sum(tmp_date_out)*10/1024

    plot_graph(out_dict, "date", "my_date_based_output")
    return

def main():
    global input_file
    if len(sys.argv)>0:
        input_file=sys.argv[1]
        print 'Input file: '+str(input_file)+'\n'
    else:
        print 'Defulat input file: '+str(input_file)+'\n'
    get_output_dic_day_based()
    get_output_dic_date_based()

main()
