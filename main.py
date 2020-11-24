from datetime import datetime

def select(a, k):
    start = datetime.now() #start timer
    f = open(a, "r") #open file
    lines = f.readlines() #read file lines
    f.close() #close file
    for idx, line in enumerate(lines): #enumerate each line index
        lines[idx] = int(line.strip()) #strip any spacing
    result = sorted(lines)[k - 1] #result of sorted list. k-1 because we start with 0th character
    end = datetime.now() #stop timer
    duration = end - start #record duration
    return result, duration #return both result and duration


if __name__ == '__main__':

    while True:
        try:
            k = input('k: ') #input for user
            k = int(k)  # convert inputted value to an integer
            result = select('numbers.txt', k) #take result from numbers file
            print(result) #print result
        except ValueError:
            print("Please input an integer")
            continue

