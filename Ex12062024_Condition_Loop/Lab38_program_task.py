# write a program that calculate amd display the letter
# given numerical score ( e.g., A, B, C ,D, E, F)
# based on the following grading scale:
# input-score - 89
# output-B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# E: 50-59
# F: 0-49

# multiple condition

# step-1  --> logic building
# Input --> score --> int
score = int(input("Enter the score\n"))
# output --> string -> A, B, C ,D, E, F

# step-2
# wright the rough logic and convert into real
# score >= 90 and score <= 100 --> A
# score >= 80 and score <= 89 --> B
# score >= 70 and score <= 79 --> C
# score >= 60 and score <= 69 --> D
# score >= 50 and score <= 59 --> E
# score >= 0 and score <= 49 --> F

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score >= 50 and score <= 59:
    print("E")
elif score >= 0 and score <= 49:
    print("F")
else:
    print("Invalid score")



