question = [
    {
        'Question:' : '2 + 2 equals?',
        'Options:' : [1, 4, 5, 2],
        'Answer:' : '4'   
    },
    {
        'Question:' : '7 + 2 equals?',
        'Options:' : [3, 4, 9, 1],
        'Answer:' : '9'   
    },
    {
        'Question:' : '6 * 2 equals?',
        'Options:' : [2, 44, 15, 12],
        'Answer:' : '12'   
    }
]

counter = 0

for x in range(3):
    for key in question[x]:
        if key == 'Question:':
            print(key, question[x][key], '\n')
        if key == 'Options:':
            print(key)
            for i in range(4):
                print(f'{i}) {question[x][key][i]}')
            choosen_option = int(input("Choose an option: "))
            answer = str(question[x][key][choosen_option])
        if key == 'Answer:':
            if answer == question[x][key]:
                print("You're right!\n")
                counter += 1
            else:
                print("You're wrong!\n")

print(f'You made {counter} question(s) out of 3!')