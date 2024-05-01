x = int(input('Ener a number: '))

# matchcase statements are like switch case statements in c++, however here we do not need to add break ni every case. It automatically breaks the case after being fullfilled
# _ is used to denote default case
match x:
    case 0:
        print('The number is 0')
    case _ if x>0 and x<10:
        print('The number is greater than 0 and less than 10')
    case _ if x>=10:
        print('The number is greater than or equal to 10')