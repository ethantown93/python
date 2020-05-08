import requests

api_key = '177590d4ced1c92728f2563be3fa6f12'

# function which makes a call to the API and returns the status code it receives. All data is hard coded so the return status
# should always be 200

def api_test():
    try:
        test_request = 'http://api.openweathermap.org/data/2.5/weather?q=san%20diego&appid=177590d4ced1c92728f2563be3fa6f12'
        response = requests.get(test_request).json()
        return response
    except:
        print('An error has occured')

response_status = api_test()


# Main function:
# function which retrieves the API data, and is called after the API test has passed. 
def get_weather_data(city, key):

    if len(city) < 2:
        print('Please enter the name of a real city')
    
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q='+user_city+'&appid='+api_key

    json_data_response = requests.get(api_url).json()

    weather_desc = json_data_response.get('weather')
    weather_temp = json_data_response.get('main')  

    # store some of the json data into variablse
    weather_description = str(weather_desc[0].get('description'))
    weather_tempurature = str(weather_temp.get('temp'))
    weather_temp_feels_like = str(weather_temp.get('feels_like'))
    
    # print weather data to the console
    print('The weather forcast for ' + city + ' is: ' + '1. Weather description: ' + weather_description + ', ' + '2. Tempurature: ' + weather_tempurature + ', ' + '3. Feels like: ' + weather_temp_feels_like )

# if else statement to check connectivity to API
if response_status.get('cod') == '404':
    print('Status code: 404, connection to API was unsuccessful')
else:
    print('Status code: 200, connection to API was successful')  
    user_city = input('City Name: ')    
    get_weather_data(user_city, api_key)  

