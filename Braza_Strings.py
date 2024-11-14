count = []
i = 0
words = input("Input any value that you would like to filter: ")

while True:
    while i != 10:
        insert = input("Insert 10 words: ")
        i += 1
        long = len(insert)
        if int(long) == int(words):
            count.append(insert)
            continue
    else:
        break
        
print(f"words that have been filtered: {count} ")