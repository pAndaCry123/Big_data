import pandas
from group_d.models import Exsam

def sorting_dataframe(group,data_frame):
    return  data_frame[data_frame['race/ethnicity'] == 'group ' +group.upper()]



def sort_group(intput_group = None ,data_frame = None):
    input_types = ['A','B','C','D','E']
    if (intput_group or data_frame) and intput_group.upper() in input_types:
        result = sorting_dataframe(intput_group,data_frame)
        return result
    else:
        #Trow exception
        print("Cannot pass nothing")


def return_data_frame(csv_file):
    if csv_file:
        return  pandas.read_csv(csv_file)
    else:
        # Trow exception
        print("Cannot pass nothing")



def return_list(result):
    list = []
    for item in result.values:
            list.append(Exsam(item))

    return list

def return_from_main(group):
    data_frame = return_data_frame('exams.csv')
    result = sort_group(group,data_frame)
    print(result)
    return return_list(result)


if __name__ == '__main__':
    return_from_main('a')