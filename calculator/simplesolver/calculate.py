class Calculator:
    
      # `+` button
    @staticmethod
    def add(inputNum, balance):
        number = Utilities.listToNumber(balance)
        return number + inputNum

    # `-` button
    @staticmethod
    def minus(inputNum , balance):
        assert inputNum, '`inputNum` must not be empty'
        num = inputNum
        if type(inputNum) is list and inputNum!='':
            num = int("".join(inputNum))
        number = Utilities.listToNumber(balance)
        return number - num

    # `x` or `*` button
    @staticmethod
    def multiply(inputNum, balance):
        number = Utilities.listToNumber(balance)
        return number * inputNum

    # `/` button
    @staticmethod
    def divide(inputNum, balance):
        number = Utilities.listToNumber(balance)
        return number / inputNum

    # `<<` button
    @staticmethod
    def removeDigit(balance):
        if type(balance) == list:
            balance.pop()
            return balance
        elif type(balance) == int:
            temp = [a for a in str(balance)]
            temp.pop()
            return temp      

    # `1=>2` button
    @staticmethod
    def firstDigitToSecond(balance):
        def returnNumber(inputnum ,number_1, number_2):
            if inputnum == number_1:
                return number_2
            else:
                return inputnum
        if len(balance) >= 2:
            first_digit = balance[0]
            second_digit = balance[1]
            return [returnNumber(a, first_digit, second_digit) for a in balance]
        elif len(balance) == 1:
            return balance
        else:
            return 'problem with list input'

    # `SUM` button
    @staticmethod
    def sumNumbers(list_of_numbers):
        return sum(list_of_numbers)

    @staticmethod
    def storeNumber(number):
        number = number

    @staticmethod
    def invX(balance,x=10):
        return [a-x for a in balance]