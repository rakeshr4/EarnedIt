from flask import Blueprint, Flask, request
from . import db

blueprint = Blueprint('server', __name__)

@blueprint.route("/")
def index():
    return "Welcome to Earned It!"

@blueprint.route('/getplans')
def getPlans():
	userId = request.args.get('userId', '')
	productId = request.args.get('productId', '')
	userId.strip()

	fitbitUserId = sql_query(f"SELECT fitbit_user_id FROM users WHERE id = '{userId}'")
	totalPrice =  sql_query(f"SELECT price FROM products WHERE id = '{productId}'")

	import fitbitWrap
	averageSteps = fitbit.getAverageSteps(userId)

	# use to test
	# totalPrice = 50.00
	# averageSteps = 15000

	#set average goal days to 30
	defaultDeadline = 15
	priceRate = round(totalPrice/ (averageSteps * defaultDeadline), 4)

	totalSteps = totalPrice/priceRate

	steps = [averageSteps + 3000, averageSteps + 5000, averageSteps + 8000]
	deadlines = [round(totalSteps/i) + 4 for i in steps]

	return str(list(zip(steps, deadlines)))