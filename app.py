from flask import Flask, jsonify, request

from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

def setup_gspread():
    scope = [
        "https://spreadsheets.google.com/feeds", 
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file", 
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("MyHearing").sheet1

    return sheet

def insert_row_to_sheet(location, noise_level, timestamp):
    sheet = setup_gspread()
    row = [location, noise_level, timestamp]
    sheet.append_row(row)


@app.route('/api/v1/insert', methods=['POST'])
def insert():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    noise_level = data.get('noise_level')
    timestamp = data.get('timestamp')
    
    if latitude is None or longitude is None or noise_level is None or timestamp is None:
        return jsonify({'success': False, 'error': 'Missing data'}), 400

    location = f"{latitude}, {longitude}"

    insert_row_to_sheet(location, noise_level, timestamp)
    return jsonify({'success': True})


@app.route('/api/v1/get')
def get():
    sheet = setup_gspread()
    records = sheet.get_all_records()
    return jsonify(records)

@app.route('/')
def index():
    return jsonify({'success': True, 'message': 'Hello World!'})

if __name__ == '__main__':
    app.run(debug=True)
