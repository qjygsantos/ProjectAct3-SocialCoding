#get_ip_info.py

from flask import Flask, render_template
import requests
import speedtest


app = Flask(__name__)

# Function to fetch IP information using the ipapi.co API
def getIP():
    url = "https://ipapi.co/json/"
    response = requests.get(url)

    if response.status_code == 200:
        # Parse JSON response
        json_data = response.json()

        # Create a formatted location string
        location = f"{json_data['city']}, {json_data['region']}, {json_data['country_name']}"

        # Check internet speed
        st = speedtest.Speedtest()
        download_speed = st.download()
        upload_speed = st.upload()

        # Add internet speed information to the dictionary
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
            "Longitude": json_data.get('longitude'),
            "Download Speed": download_speed,
            "Upload Speed": upload_speed
        }
    else:
        # Return an error dictionary if the request fails
        return {
            "Error": "Failed to retrieve IP address information",
            "Status Code": response.status_code
        }


# Define a route for the root URL ('/')
@app.route('/')
def display_ip_info():
    # Call getIP() to fetch IP information
    ip_info = getIP()

    # Render an HTML template and pass IP information to it
    return render_template('index.html', ip_info=ip_info)

# Run the Flask app if this script is the main entry point
if __name__ == '__main__':
    app.run()

