from handler import CommandHandler
from command.commands import CreateExpenseCommand
from datetime import datetime
from psycopg2 import IntegrityError
from repository.expenses import ExpenseRepository, Expense


class CreateExpenseCommandHandler(CommandHandler):

    def __init__(self, expense_repository: ExpenseRepository):
        self.expense_repository = expense_repository

    def handle(self, command: CreateExpenseCommand):
        expense = Expense(**command.to_primitive())
        self.expense_repository.create_expense(expense)


        