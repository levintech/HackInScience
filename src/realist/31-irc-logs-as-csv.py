import csv

if __name__ == '__main__':
    pairs = {}

    with open('francejs.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        msg_logs = [row for row in reader if row[0] == '1']
        usernames = [log[2] for log in msg_logs]

        for log in msg_logs:
            for username in usernames:
                if username in log[3]:
                    pair_name = (log[2], username) if log[2] < username else (username, log[2])
                    if pair_name in pairs.keys():
                        pairs[pair_name] += 1
                    else:
                        pairs[pair_name] = 1
        
    
    pairs = sorted(pairs, key=lambda x:x[1], reverse=False)
    print(pairs[0][0] + ", " + pairs[0][1])