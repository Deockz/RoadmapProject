import pandas as pd
import argparse

def parseArguments():
    parser = argparse.ArgumentParser(description='Expense Tracker Program')
    parser.add_argument('Action', type=str.lower,nargs='+', choices= ['add','update','delete','list','summary'], help='Action to be done')
    parser.add_argument('--description', nargs='?',default='Expense',help='Description of Expense to be Added or Updated')
    parser.add_argument('--amount', nargs='?',default=0,help='Amount of Expense to Add or change')
    parser.add_argument('--id', nargs='?',default=0,help='Expense ID')
    parser.add_argument('--month', nargs='?',default=1,help='Month to view on Summary')
    args = parser.parse_args()    
    return args

def getExpenseData():
    try:
        with open('expenseDatabase.csv', encoding='utf-8') as expensesData:
            df =pd.read_csv(expensesData)
            return df
    except Exception as Error:
        if type(Error).__name__ == 'FileNotFoundError':
            print('DataBase do not exist. Add the first Expense to Create One')
        else:
            print('An exception ocurr: ',Error,)

def createDatabase():
    print('DatabaseReady')

def addExpense():
    print('Expense Added.')

def updateExpense():
    print('Expense updated')

def deleteExpense():
    print('Expense deleted')

def listExpense():
    print('Expenses: ')

def summaryExpense():
    print('This is the summary')

def main ():
    arguments = parseArguments()
    if arguments.Action[0] == 'add':
        addExpense()
    elif arguments.Action[0] == 'update':
        updateExpense()
    elif arguments.Action[0] == 'delete':
        deleteExpense()
    elif arguments.Action[0] == 'list':
        listExpense()
    elif arguments.Action[0] == 'summary':
        summaryExpense()
    else:
        print('Command invalid')
    #getExpenseData()


if __name__ == '__main__':
    main()