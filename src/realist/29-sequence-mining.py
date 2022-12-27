import itertools, collections

def create_substrings(data, max_int):
    for seq_index, seq in enumerate(data):
        for step in range(1, max_int+1):
            for sub_seq in range(len(seq) - (step - 1)):
                slice_ = seq[sub_seq:sub_seq+step]

                yield seq_index, slice_



def seq_mining(data, prop, max_int):
    positions = collections.defaultdict(set)
    max_length = max([len(sequence) for sequence in data])
    max_int = max_length if max_int > max_length else max_int

    for i, seq in create_substrings(data, max_int):
        positions[seq].add(i)

    data_len = len(data)
    counter = collections.Counter()

    for l, t in positions.items():
        t_len = len(t)

        if t_len/data_len < prop:
            continue

        counter[l] = len(t)
    
    return counter