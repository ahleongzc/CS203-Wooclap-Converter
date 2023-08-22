import csv

fileName = "Week1"

format = ".csv"
filePath = "./" + fileName + format

print("Steps to use this code:")
print("1. Download the file from ELearn")
print("2. Save the file to .csv ")
print("3. Rename it to 'Week<Number>' with no spaces")
print("4. Change the fileName variable at the top to the file to 'Week<Number>'")
print("\t* Not necessary to follow step 3 and 4\n")

with open(filePath, "r") as file:

    print("!! " + fileName + " Wooclap !!")
    print("----------\n")
    number = 1
    reader = csv.reader(file)
    next(reader, None)

    for row in reader:
        questionType = row[0]
        questionTitle = row[1]
        answerIndex = row[2].split(",")
        answerIndex = [int(answer) for answer in answerIndex if answer != ""]

        print(f"Question {number}")
        print(f"Type: {questionType}\n")
        print(questionTitle)
        choices = row[3:]

        if questionType == "MCQ":
            start = 'A'
            count = 0
            map = {}

            for choice in choices:
                if choice != "":
                    map[chr(ord('A') + count)] = choice
                    print(f"{chr(ord('A') + count)}. {choice}")
                    count += 1

            correctAnswers = [choices[index - 1]
                              for index in answerIndex if choices[index - 1] != ""]

            print("\nCorrect answers:")

            for correctAnswer in correctAnswers:
                ch = list(map.keys())[list(map.values()).index(correctAnswer)]
                print(ch + ". " + correctAnswer)

        if questionType == "Poll" or questionType == "Rating":
            start = 'A'
            count = 0

            for choice in choices:
                if choice != "":
                    print(f"{chr(ord('A') + count)}. {choice}")
                    count += 1

        print("\n----------\n")
        number += 1
