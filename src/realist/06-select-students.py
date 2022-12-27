def select_student(students, threshold):
    result_dict = {
        'Accepted': [],
        'Refused': []
    }
    
    for student in students:
        if student[1] >= threshold:
            result_dict['Accepted'].append(student)
        else:
            result_dict['Refused'].append(student)
    
    # sort Accepted and Refused students with their score
    result_dict['Accepted'] = sorted(result_dict['Accepted'], key=lambda x: x[1], reverse=True)
    result_dict['Refused'] = sorted(result_dict['Refused'], key=lambda x: x[1])

    return result_dict