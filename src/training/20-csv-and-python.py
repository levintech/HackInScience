import csv
import datetime

def generate_csv(a_list):
    dict_list = []
    for itemSet in a_list:
        temp_dict = dict((x, y) for x, y in itemSet)
        temp_dict['date'] = temp_dict['date'].strftime('%m/%d/%Y')
        temp_dict['locations'] = ','.join(temp_dict['locations'])
        dict_list.append(temp_dict)
    
    print(dict_list)
    
    with open('results.csv', 'w', newline='') as csvfile:
        fieldnames = ['temperature', 'date', 'locations', 'weather']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for item in dict_list:
            writer.writerow(item)

def parse_csv():
    dict_list = []

    with open('students.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            month, day, year = row['Birthdate'].split('/')
            row['Birthdate'] = datetime.date(int(year), int(month), int(day))
            row['Marks'] = [int(item) for item in row['Marks'].split(',')]
            dict_list.append(row)
    
    return dict_list