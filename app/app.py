import uuid, math
from flask import Flask, request, session
from datetime import datetime
app = Flask(__name__)

app.secret_key = 'bad_secret_key'

@app.route('/')
def index():
	return "index page"

@app.route('/receipts/process', methods=['GET', 'POST'])
def process_receipts():
	if request.method == 'POST': 
		receipt_id = uuid.uuid4().hex 
		session[receipt_id] = request.json
		return {'id': receipt_id}
	if request.method == 'GET':
		return 'This endpoint takes POST only'


@app.route('/receipts/<string:id>/points')
def get_points(id): 
    points = 0 

    # One point for every alphanumeric character in the retailer name.
    # points += len(session[id]['retailer']) 
    points += sum(1 for char in session[id]['retailer'] if char.isalnum()) 
    # print(1, points)
    # 50 points if the total is a round dollar amount with no cents.
    total = eval(session[id]['total'])
    if int(total) == total: 
        points += 50
    # print(2, points)
    # 25 points if the total is a multiple of 0.25.
    if int(total * 100) % 25 == 0: 
        points += 25 
    # print(3, points)
    # 5 points for every two items on the receipt.
    points += len(session[id]['items']) // 2 * 5
    # print(4, points)
    # If the trimmed length of the item description is a multiple of 3, 
    # multiply the price by 0.2 and round up to the nearest integer. 
    # The result is the number of points earned.
    for item in session[id]['items']:
        if len(item['shortDescription'].strip()) % 3 == 0: 
            # print(item['shortDescription'])
            price = eval(item['price'])
            points += math.ceil(price * 0.2)
    # print(5, points)
    # 6 points if the day in the purchase date is odd.
    day = datetime.strptime(session[id]['purchaseDate'], '%Y-%m-%d').day
    if day % 2 == 1: 
        points += 6 
    # print(6, points)
    # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    hour, _ = session[id]['purchaseTime'].split(':') 
    if 14 <= int(hour) <16: 
        points += 10
    # print(7, points)
    
    return {'points':points}

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
