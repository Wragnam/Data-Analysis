import pandas as pd


def data_headers(file):

    file_type = file[file.index('.'):]
    df = []
    file_name =  'data/'+str(file)
    
    if file_type == '.xlsx':
        df = pd.read_excel(file_name)
    elif file_type == '.csv':
        df = pd.read_csv(file_name)
    else:
        print("Only support of CSV and Excel files")
        exit()

    return [df.columns.values,df]

def full_evaluation(data):
    described = data.describe()
    print(described)

def totals(header, data):
    print(header)

    sort_by = input('Enter value of totals you want: ')

    print(data.groupby(str(sort_by)).size())

def main():
    #get filename in data folder
    file_name = input("File name/ File path: ")

    #get dataframe of file
    header,data = data_headers(file_name)


    options = {0: "Full Evaluation", 1: "Totals of Elements"}

    for k, v in options.items():
        print(k,':', v)

    try:
        data_option = int(input('Enter number of option: '))
        data_option = options[data_option]

        if data_option == "Full Evaluation":
            full_evaluation(data)
        elif data_option == "Totals of Elements":
            totals(header,data)

    except Exception as e:
        print("Must be a valid integer", e)

if __name__ == '__main__':
    main()

