# 1. Program to return the lesser number from the List if it has two even number and greater number if it has odd number in List
#Normal way
def less_number(num1,num2):
    '''
    This function utilizes simple if else techniques to compute the problem
    '''
    if num1%2 == 0 and num2%2 == 0:
        if num1 < num2:
            result = num1
        else:
            result = num2

    else:
        if num1 > num2:
            result = num1
        else:
            result = num2

    return result 

#Using inbuilt function
def less_number2(num1,num2):
    """
    This function uses min() and max() inbuilt functions 
    """
    if num1%2 == 0 and num2%2 == 0:
        result = min(num1,num2)
    else:
        result = max(num1,num2)

    return result


# 2. Program which takes two-words string and returns true if noth words begin with same letter 
def animal_crackers(string1):
    '''
    This funtion utilizes very usefull string methods, lower() and split() where lower 
    converts charatcers into lower case and split converts string into seperate lists.
    '''
    wordlist = string1.lower().split()
      
    return wordlist[0][0] == wordlist[1][0]

# 3. Write a function that capitalizes first and fourth letters of a name

#First way
def tocapitalize(string2):
    '''
    This function uses string indexing for its computation
    '''
    first_char = string2[0]
    inbetween_char = string2[1:3]
    fourth_char = string[3]
    rest_char = string2[4:]

    return first_char.upper() + inbetween_char + fourth_char.upper() + rest_char
#Second way

def tocapitalize(string2):
    '''
    This funtion uses capitalize() method to capitalize first and fourth lettter of string
    by splitting the list.
    '''
    first_half = string2[:3]
    second_half = string2[3:]

    return first half.capitalize() + second_half.capitalize()


# 4. Given a sentence return the sentencce with the words reversed  

def rev_sentence_words(letter):
    '''
    This function uses join() method, In join method the string left to the keyword is 
    attached in between the list of stings
    '''
    wordlist = letter.split()
    reverse_list = wordlist[::-1]
    return ' '.join(reverse_list)    


# 5. Given a list return true if the array contains a 3 next to 3 somewhere.
    '''
    This function uses len() function to check length of the string. 
    '''
    def check_conseq_3(text):
        for i in range(0:len(text)-1):
            if text[i] == 3 and text [i+1] == 3:
                return True

        return False

# 6. Given a string, return a string where for every character in the original there
#    are three characters

    def concat_string(txta):
        result = ''

        for i in txta:
            result += i*3

        return result

# 7. To print all prime numbers upto the given number

    def prime_upto(num):
        '''
        Prime number logic using python langauge
        '''
        primelist = [2]

        x = 3

        for y in range(3:x:2):
            if x%y == 0:
                x +=2

                break
        else:
            primelist.append(x)
            x +=2


