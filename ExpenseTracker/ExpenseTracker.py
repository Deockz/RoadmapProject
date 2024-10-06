import pandas as pd
import argparse
import datetime
import os.path

csv_file_name = 'expensesDatabase.csv'
current_time = datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')

#Fuction to parse arguments
def parseArguments():
    parser = argparse.ArgumentParser(description='Expense Tracker Program')
    parser.add_argument('Action', type=str.lower,nargs='+', choices= ['add','update','delete','list','summary'], help='Action to be done')
    parser.add_argument('--description', nargs='?',default='Expense',help='Description of Expense to be Added or Updated')
    parser.add_argument('--amount', type=int,nargs='?',default=0,help='Amount of Expense to Add or change')
    parser.add_argument('--id', type=int, nargs='?',default=1,help='Expense ID')
    parser.add_argument('--month',type=int, nargs='?',default=None,help='Month to view on Summary')
    args = parser.parse_args()    
    return args

#Fuction to get csv data. 
def getExpenseData():
    try:
        with open(csv_file_name, encoding='utf-8') as expensesData:
            df =pd.read_csv(expensesData)
            return df
    except Exception as Error:
        if type(Error).__name__ == 'FileNotFoundError':
            print('File not Found')            
        else:
            print('An exception ocurr: ',Error,)

#Fuction to update database 
def updateDatabase(data):
    df = pd.DataFrame(data)        
    df.to_csv(csv_file_name,index=False) 
    
#Add a new expense
def addExpense(description,amount):
   data = getExpenseData()
   id = data.id.max() + 1
   data.loc[len(data.index)] = [id,current_time,description,amount]  
   updateDatabase(data)
   print(f'Expense added with id: {id}')

#Update de description and de amount of a expense
def updateExpense(id, description,amount):
    df = getExpenseData()
    row = df[df['id'] == id].index
    if  df.loc[row,['description','amount']].empty:
        print('Index not found')
    else:
        df.loc[row,['description','amount']] = [description,amount]
        updateDatabase(df)
        print(f'Expense with id {id} updated')

#Delete a row from de database
def deleteExpense(index):
    df = getExpenseData()
    if index in df['id'].values:
        df2 = df[df.id != index]
        updateDatabase(df2)
        print(f'Expense with id {index} deleted')
    else:
        print('Error. Expense ID not found')
    
#Print the database
def listExpense():
    df = getExpenseData()
    print(df)

#Print summary of all expenses or expeneses by month
def summaryExpense(month):
    df = getExpenseData()
    try:
        if month == None:
            total_amount=0
            for x in df['amount']:
                total_amount+=x
            print(total_amount)
        else:
            total_amount= 0
            for i in range(0,len(df)):
                expenseDate = df.iloc[[i]].date.values[0]             
                date_mont = datetime.datetime.strptime(expenseDate, "%m/%d/%Y %H:%M:%S").month      
                if date_mont == month:
                    total_amount += df.iloc[[i]].amount.values[0]
            month_name = datetime.datetime(1,month,12).strftime('%B')
            print(f'Total amount of expenses in {month_name}: {total_amount}')
    except ValueError as Error:
        print('Month not in range. Use numbre between 1 - 12')

#Main function
def main ():
    if os.path.isfile(csv_file_name):
        arguments = parseArguments()
        if arguments.Action[0] == 'add':
            addExpense(arguments.description,arguments.amount)
        elif arguments.Action[0] == 'update':
            updateExpense(arguments.id,arguments.description,arguments.amount)
        elif arguments.Action[0] == 'delete':
            deleteExpense(arguments.id)
        elif arguments.Action[0] == 'list':
            listExpense()
        elif arguments.Action[0] == 'summary':
            summaryExpense(arguments.month)
        else:
            print('Command invalid')
    else:
        empty_dataBase = [{'id':0,'date':current_time,'description': 'DataBase Created','amount':0}]
        df = pd.DataFrame(empty_dataBase)        
        df.to_csv(csv_file_name,index=False) 
        print(f'DataBase do not exist. Empity database created with name: {csv_file_name}')
        print(df)


if __name__ == '__main__':
    main()