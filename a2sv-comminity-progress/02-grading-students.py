#!/bin/python3

import math
import os
import random
import re
import sys



# 93 - add 2
# 98 - add 2

# 94 - add 1
# 99 add 1

def gradingStudents(grades):
    finalGrades = []
    for grade in grades:
        print("processing grade",  grade);
        if grade < 38: finalGrades.append(grade)
        else:
            grade = str(grade)
            if (grade[-1] == '3' or grade [-1] == '8'):
                finalGrades.append(int(grade) + 2)
            elif (grade[-1] == '4' or grade [-1] == '9'):
                finalGrades.append(int(grade) + 1)
            else:
                finalGrades.append(int(grade))
    
    return (finalGrades)

if __name__ == '__main__':
    grades = [73,67,38,33];
    print(gradingStudents(grades))