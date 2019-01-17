# name: get_data_list
# param: FILE_NAME <str> - the file's name you saved for the stock's prices
# brief: get a list of the stock's records' lists
# return: a list of lists <list>
def get_data_list(FILE_NAME):
    file = open(FILE_NAME, "r")
    file1 = file.readlines()[1:]
    file.close()
    result = []
    for line in file1:
        result.append(line.split(","))
    return result


# name: get_monthly_averages
# param: data_list <list> - the list that you will process
# brief: get a list of the stock's monthly averages and their corresponding dates
# return: a list <list>
def get_monthly_averages(data_list):
    volumes={}
    stock_value={}
    average={}
    for (date, vol, adjclose) in data_list:
        year,month,day= (date.split("-"))
        month_year=month+"-"+year
        if (month_year in volumes):
            volumes[month_year]+=float(vol)
            stock_value[month_year]+=float(adjclose)*float(vol)
        else:
            volumes[month_year]=float(vol)
            stock_value[month_year]=float(adjclose)*float(vol)

    for month_year in volumes:
        average[month_year]=stock_value[month_year]/volumes[month_year]

    return average

# name: print_info
# param: monthly_average_list <list> - the list that you will process
# brief: print the top 6 and bottom 6 months for Google stock
# return: None
def print_info(monthly_average_list):
    sorted_average_list = [(k, monthly_average_list[k]) for k in sorted(monthly_average_list, key=monthly_average_list.get, reverse=True)]
    file_to_write = open('monthly_averages.txt', 'w')
    ptf = (lambda x: print(x,file=file_to_write))
    ptf("6 best months for google stock:")
    for k, v in sorted_average_list[:6]:
        ptf(str(k)+", %.2f"%v)
    sorted_average_list = [(k, monthly_average_list[k]) for k in sorted(monthly_average_list, key=monthly_average_list.get, reverse=False)]
    ptf("6 worst months for google stock:")
    for k, v in sorted_average_list[:6]:
        ptf(str(k)+", %.2f"%v)
    file_to_write.close()
    return


# call get_data_list function to get the data list, save the return in data_list

# call get_monthly_averages function with the data_list from above, save the
# return in monthly_average_list
print_info(get_monthly_averages(get_data_list("stocks.csv.csv")))
# call print_info function with the monthly_average_list from above
