import numpy as np

def main():
    # Using readlines()
    file1 = open('data', 'r')
    Lines = file1.readlines()
      
    all_entries = []
    single = []
    # Strips the newline character
    for line in Lines:
        if not line.strip():
            all_entries.append(np.array(single).sum())
            single = []
        else: 
            single.append(int(line))

    all_entries = np.array(all_entries)
    ind = np.argpartition(all_entries, -4)[-3:]

    print(all_entries.max())
    print(all_entries[ind].sum())


if __name__ == '__main__':
    main()