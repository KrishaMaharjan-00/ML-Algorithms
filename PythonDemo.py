from time import sleep
print('This is my file to demonstrate python practices')

def process_data(data):
    print('Beginning data processing...')
    modified_data = data + " that has been modified"
    sleep(3)
    print('Data Processing Finished')
    return modified_data

def read_data_from_web():
    print('Reading Data From The Web')
    data = input("Data From The Web:  ")
    return data

def write_data_to_database(data):
    print('Printing Data To Database')
    print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)


if __name__ == "__main__":
    main()