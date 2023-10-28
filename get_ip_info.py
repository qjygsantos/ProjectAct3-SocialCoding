from flask import Flask, render_template
import requests

app = Flask(__name__)

def getIP():
    url = "https://ipapi.co/json/"
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        location = f"{json_data['city']}, {json_data['region']}, {json_data['country_name']}"
        return {
            "IPv6 Address": json_data['ip'],
            "Location": location,
            "ISP": json_data['org'],
            "ASN": json_data['asn'],
            "Country Code": json_data['country'],
            "Postal Code": json_data['postal'],
            "Timezone": json_data['timezone'],
            "Calling Code": json_data['country_calling_code'],
            "Latitude": json_data.get('latitude'),
            "Longitude": json_data.get('longitude')
        }
    else:
        return {
            "Error": "Failed to retrieve IP address information",
            "Status Code": response.status_code
        }

@app.route('/')
def display_ip_info():
    ip_info = getIP()
    return render_template('index.html', ip_info=ip_info)

if __name__ == '__main__':
    app.run()
