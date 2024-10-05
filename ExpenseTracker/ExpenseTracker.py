import pandas as pd
import argparse
import datetime
import os.path

csv_file_name = 'expensesDatabase.csv'
current_time = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')

'''test_dir= [
        {'id':1,'date':current_time,'description':'test value 1','amount':0},
        {'id':2,'date':current_time,'description':'test value 2','amount':10},
        {'id':3,'date':current_time,'description':'test value 3','amount':20}
]'''

#Fuction to parse arguments
def parseArguments():
    parser = argparse.ArgumentParser(description='Expense Tracker Program')
    parser.add_argument('Action', type=str.lower,nargs='+', choices= ['add','update','delete','list','summary'], help='Action to be done')
    parser.add_argument('--description', nargs='?',default='Expense',help='Description of Expense to be Added or Updated')
    parser.add_argument('--amount', type=int,nargs='?',default=0,help='Amount of Expense to Add or change')
    parser.add_argument('--id', type=int, nargs='?',default=1,help='Expense ID')
    parser.add_argument('--month', nargs='?',default=1,help='Month to view on Summary')
    args = parser.parse_args()    
    return args

#Fuction to get csv data. If file do not exist call createDatase()
def getExpenseData():
    try:
        with open(csv_file_name, encoding='utf-8') as expensesData:
            df =pd.read_csv(expensesData)
            return df
    except Exception as Error:
        if type(Error).__name__ == 'FileNotFoundError':
            createDatabase()
        else:
            print('An exception ocurr: ',Error,)

#Fuction to update database or create empty database if not exist
def updateDatabase(data):
    if os.path.isfile(csv_file_name):
        df = pd.DataFrame(data)        
        df.to_csv(csv_file_name,index=False) 
    else:
        empty_dataBase = {'expenses':[],'expenseID' : 0}
        df = pd.DataFrame(empty_dataBase)        
        df.to_csv(csv_file_name,index=False) 
        print(f'DataBase do not exist. Empity database created with name: {csv_file_name}')

#Add a new expense
def addExpense(description,amount):
   data = getExpenseData()
   id = data.id.max() + 1
   data.loc[len(data.index)] = [id,current_time,description,amount]  
   updateDatabase(data)
   print(f'Expenses added with id: {id}')

def updateExpense(id, description,amount):
    df = getExpenseData()
    print(df)
    row = df[df['id'] == id].index
    df.loc[row,['description','amount']] = [description,amount]
    updateDatabase(df)

def deleteExpense():
    print('Expense deleted')

def listExpense():
    print('Expenses: ')

def summaryExpense():
    print('This is the summary')

def main ():
    arguments = parseArguments()
    if arguments.Action[0] == 'add':
        addExpense(arguments.description,arguments.amount)
    elif arguments.Action[0] == 'update':
        updateExpense(arguments.id,arguments.description,arguments.amount)
    elif arguments.Action[0] == 'delete':
        deleteExpense()
    elif arguments.Action[0] == 'list':
        listExpense()
    elif arguments.Action[0] == 'summary':
        summaryExpense()
    else:
        print('Command invalid')
    getExpenseData()


if __name__ == '__main__':
    main()