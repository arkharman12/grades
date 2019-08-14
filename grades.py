def typeYourGrade():
    grade1 = float( input( "Please enter the score of your first test: " ) )
    grade2 = float( input( "Please enter the score of your second test: " ) )
    grade3 = float( input( "Please enter the score of your third test: " ) )
    grade4 = float( input( "Please enter the score of your fourth test: " ) )
    grade5 = float( input( "Please enter the score of your fifth test: " ) )
    finAverage = (grade1 + grade2 + grade3 + grade4 + grade5)/5
    return grade1, grade2, grade3, grade4, grade5, finAverage

def dictateGrade(studentGrade, finAverage):
    if( studentGrade < 60):
        return "F"
    elif( studentGrade < 69):
        return "D"
    elif( studentGrade <72):
        return "C-"
    elif( studentGrade <75):
        return "C"
    elif( studentGrade <78):
        return "C+"
    elif( studentGrade <80):
        return "B-"
    elif( studentGrade <83):
        return "B"
    elif( studentGrade <86):
        return "B+"
    elif( studentGrade <90):
        return "A-"
    elif( studentGrade <96):
        return "A"
    elif( studentGrade <100):
        return "A+"

def printResults(grade1, grade2, grade3, grade4, grade5, finAverage):
    print( "Grade\tYour Grade" )
    print( str( grade1 ) + "\t" + dictateGrade( grade1 ), \
           str( grade2 ) + "\t" + dictateGrade( grade2 ), \
           str( grade3 ) + "\t" + dictateGrade( grade3 ), \
           str( grade4 ) + "\t" + dictateGrade( grade4 ), \
           str( grade5 ) + "\t" + dictateGrade( grade5 ), sep = "\n" )
    finalAverage = (grade1 + grade2 + grade3 + grade4 + grade5)/5
    print("Your final average is: {} ".format(finalAverage))

def main():
    grade1, grade2, grade3 ,grade4, grade5 = typeYourGrade()
    printResults( grade1, grade2, grade3 ,grade4, grade5 )
main()



