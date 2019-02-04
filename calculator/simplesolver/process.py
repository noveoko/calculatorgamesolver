import re

class Parse:

    def __init__(self):
        pass

    def extract_numbers(self, button_string):
        if re.match('\d+', button_string): #numbers in string
            return re.findall('(\d+)',button_string)
        else:
            return button_string

    def extract_buttons(self, string_of_buttons):
        """takes a string '+2,+5,/7' and converts it to button tuples"""
        buttons = set()
        list_buttons = string_of_buttons.split(",")
        r = re.compile("((?P<add>\+(\d+))|(?P<multiply>x(\d+))|(?P<divide>\/(\d+))|(?P<balance>\((\d+)\))|(?P<subtract>\-(\d+))|(?P<delete_last>\<\<)|(?P<replace_num>(\d+)\=\>(\d+))|(?P<insert_number>(\d)))")
        for button_string in list_buttons:
            matches = r.finditer(button_string)
            for m in matches:
                for k,v in m.groupdict().items():
                    if v!=None:
                        print(k,self.extract_numbers(v))      
      

class Calculator:
    
      # `+` button
    @staticmethod
    def add(self, inputNum, balance):
        return balance + inputNum

    # `-` button
    @staticmethod
    def minus(self, inputNum , balance):
        return balance - inputNum

    # `x` or `*` button
    @staticmethod
    def multiply(self, inputNum, balance):
        return balance * inputNum

    # `/` button
    @staticmethod
    def divide(self, inputNum, balance):
        return balance / inputNum

    # `<<` button
    @staticmethod
    def removeDigit(self, balance):
        return str(balance)[0:-2] 

    # `1=>2` button
    @staticmethod
    def firstDigitToSecond(self, balance, firstNum, secondNum):
        """Replaces all occurances of first number with second number"""
        return str(balance).replace(str(firstNum),str(secondNum))

    # `SUM` button
    @staticmethod
    def sumNumbers(self, balance):
        return sum([int(a) for a in str(balance)])

    @staticmethod
    def storeNumber(self, number):
        pass

    @staticmethod
    def invX(self, balance,x=10):
        pass


    
if __name__ == "__main__":
    pass