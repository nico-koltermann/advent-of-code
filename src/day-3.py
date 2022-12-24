import numpy as np

# c3 is optional. Needed for part b
def calculate_priority(c1, c2, c3=None):
    score = 0

    if c3 == None:
        c3 = c2

    set1 = set(c1)
    set2 = set(c2)
    set3 = set(c3)

    for e in list(set1.intersection(set2).intersection(set3)):
        if e.islower():
            score += ord(e) - 96
        else:
            score += ord(e) - 38

    return score


def first_task(Lines):
    priority = 0

    for line in Lines:

        r_lenght = int(len(line) / 2)

        comp1 = line[:r_lenght]
        comp2 = line[r_lenght:]

        priority += calculate_priority(comp1, comp2)

    print(priority)


def second_task(Lines):
    priority = 0

    i = 0
    while i+2 < len(Lines):

        comp1 = Lines[i]
        comp2 = Lines[i+1]
        comp3 = Lines[i+2]
        i += 3

        priority += calculate_priority(comp1.replace("\n",""), comp2.replace("\n",""), comp3.replace("\n",""))

    print(priority)


def main():
    f = open('data', 'r')
    Lines = f.readlines()
      
    first_task(Lines)
    second_task(Lines)


if __name__ == '__main__':
    main()