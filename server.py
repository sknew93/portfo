from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def homepage():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name=None):
    return render_template(page_name)


def dataprinter(input):
	with open('./database.txt', mode='a') as my_file:
		email = input['email']
		subject = input['subject']
		message = input['message']
		text = my_file.write(f'\n{email},{subject},{message}')
		print('WRITTEN TO DATABASE SUCCESSFUllY.')

def csvprinter(input):
	with open('./CSVdatabase.csv', newline="", mode='a') as my_file2:
		email = input['email']
		subject = input['subject']
		message = input['message']
		csv_writer = csv.writer(my_file2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
		print('WRITTEN TO CSV DATABASE SUCCESSFUllY.')

@app.route('/submit_form', methods=['POST', 'GET']) #GET-send information POST - save information
def submit_form():
	if request.method == "POST":
		try:
			# data = request.form['email']
			data = request.form.to_dict()
			csvprinter(data)
			dataprinter(data)
			print(data)
			return redirect('/thankyou.html')

		except:
			return "ERROR! DID NOT SAVE TO DATABASE."

	else:
		return "SOMETHING WENT WRONG! TRY AGAIN."
    