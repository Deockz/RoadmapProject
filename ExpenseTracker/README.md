# Expense Tracker

This program is based on https://roadmap.sh/projects/expense-tracker project.

## Installation

To use this program first clone the repository

```
git clone https://github.com/Deockz/RoadmapProject/
cd ExpenseTracker
```

## Usage

Run the aplication. As first argument is required the action to perform.
**Important**. The first time you run the program the file 'expensesDatabase.csv' will be created.

### Add an expense
Add an expense to the databse. Must include the description and the amount 
```
python ExpenseTracker.py add --description 'Expense Description' --amount 20
```

### Update an expense
Update an expense. Inlude the expense id, the description and the amount 
```
python ExpenseTracker.py update --id 1 --description 'Expense Description' --amount 20
```

### Delete an expense
Delete a expense. Inlude the expense id
```
python ExpenseTracker.py update --id 1
```

### Show all the expenses
Show the list of expenses
```
python ExpenseTracker.py list
```

### Summary of expenses. General and per month
Show a summary of all expenes. An optional argument can be added to show the summary per month
```
python ExpenseTracker.py summary
```
or
```
python ExpenseTracker.py summary --month 1
```
