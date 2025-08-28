import requests
import json
import os
from dotenv import load_dotenv


# Load enviroment variables from the .env file (if present)
load_dotenv()


# Latitude and Longtitude for Lewisham, London (51.4612, 0.0073)
lat = 51.4612
lon = 0.0073

# Determine the unit of measurement, for us: Metric
units = "metric"

# What we do not want from the weather data API response
exclude = "minutely,hourly,alerts"

## Our temp API key
API_KEY = os.getenv('WEATHER_API_KEY')


# Gets the data from the OpenWeatherAPI in the form of a response object.
# response = requests.get("api.openweathermap.org/data/2.5/forecast?lat=" + str(lat) + "&lon=" + str(lon) + "&units=" + units +"&appid=" +  API_KEY).json()


# response = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&appid=" + API_KEY_2).json()


# Example API call
response = requests.get("http://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&units=" + units  + "&appid=" + API_KEY).json()
#print(response)

# Getting the latest temperature, in celsius because of our units variable in our API Call
temp = response["list"][0]["main"]["temp"]

description = response["list"][1]["weather"][0]["description"]




## function - get_weather()
## input, long, lat and units
## output, our desired weather report statement


# Returns our desired weather statement for the given lat, long. In the specified units.
def get_weather(long, lat, units):
    
    # Assigning the longtitude, latitude and units.
    long, lat, units=long, lat, units

    # API Call to OpenWeather, 
    url ="http://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&units=" + units  + "&appid=" + API_KEY
    
    # Our HTTP Get method retriving the OpenWeather data, returning a response object.
    r = requests.get(url)

    # Error handling
    try:
        # Handle any issues with the status of the API Get request.
        # The `ok` method retunrs `True` if the status_code of the request less than 400.
        #   Successful responses   (200 - 299) [e.g 200 OK - meaning successful]
        #   Client error responses (400 - 499)
        #   Server error responses (500 - 599)
        if (r.ok != True):
            print("Error in the Get request, status is: " + r.reason)

        # Handle any issues with the json decoding.
        # Decodes the JSON response body as a Python object.
        response = r.json()
    
    
    except requests.RequestException:
        # There was an ambiguous exception that occurred while handling the request.
        result = "Error with the request"
        return result

    except requests.JSONDecodeError:
        # Couldn’t decode the text into json.
        result = "The response could not be decoded into json"
        return result

    
    # Getting the latest temperature variable in our API Call. (in celsius as units = metric)
    temp = response["list"][0]["main"]["temp"]

    # Getting the weather condition
    description = response["list"][1]["weather"][0]["description"]

    # Return our weather report with the data from the API Call
    result = f"🌞 Good day! Today in Lewisham, the weather can be described as: {description}, with a temp of {temp} degrees celsius." 
    return result


# Function Call
weather = get_weather(0.0073, 51.4612, "metric")
print(weather)



## TODO Get our WEATHER message sent!!!
## TODO Get our basic secrets/env variables hidden




def send_d_message(channel_id, d_auth, message):
    channel_id = channel_id
    d_auth = d_auth

    # discord URL
    d_url = f"https://discord.com/api/v9/channels/{channel_id}/messages"



    # Headers for our POST request to discord servers 
    headers = {
        "Authorization" : d_auth
    }

    
    # The content in our POST request, our actual message.
    payload = {
        "content" : message
    }
    
    # Handle any issues with the status of the API POST request.
    try:
        # POST Request, request to post our message to discord.
        #   "The POST method submits an entity to the specified resource, 
        #   often causing a change in state or side effects on the server." - MDN 
        d_request = requests.post(d_url, payload, headers=headers)
        
        # The `ok` method retunrs `True` if the status_code of the request less than 400.
        #   Successful responses   (200 - 299) [e.g 200 OK - meaning successful]
        #   Client error responses (400 - 499)
        #   Server error responses (500 - 599)
        if (d_request.ok != True):
            print("Error in the Get request, status is: " + r.reason)

    except requests.RequestException:
        print("Error with the request")




# ID for the weather-report discord server, channel: weather-report.
channel_id = os.getenv('DISCORD_CHANNEL_ID')

# SECRET
# discord authorisation
d_auth = os.getenv('DISCORD_AUTH')

# The message that will be sent to discord using our POST request.
message = get_weather(0.0073, 51.4612, "metric")


# Function call 
send_d_message(channel_id, d_auth, message)






## Error handling for the request method
r = requests.get('http://github.com/')

# try:
    # the `ok` retunrs true if the status_code of the request less than 400.
   # '''
    #Informational responses (100 - 199)
    #Successful responses (200 - 299) [e.g 200 OK - meaning successful]
    #Redirection messages (300 - 399)
    #Client error responses (400 - 499)
    #Server error responses (500 - 599)

    #if (r.ok != True):
        #print("Error in the Get request, status is: " + r.reason)
    

# There was an ambiguous exception that occurred while handling your request
#except requests.RequestException:
 #   print("Error with the request")
# Couldn’t decode the text into json
#except requests.JSONDecodeError:
 #   print("The response could not be decoded into json")







## TODO
# [X] - Get the basic desired output printed to the console
# [X] - Get the mvp output printed with functions
# [X] - Include try and except blocks 

## TO ADD to Notes
## - What a enviroment variable is [python programmer video and techlro video, python venv documentation] 
#  - How to create virtual enviroment variables in python for each project and 
#    the benefits when working with third party packages. (like requests)
#  - learnt about HTTP status codes for requests
#  - the method: GET
#  - try and execute blocks, handling exceptions.
#       - get requests requests.RequestException:
#       - json decoding requests.JSONDecodeError:
#  - Question: We are told by the py docs, "You should exclude your virtual environment directory 
#    from your version control system using .gitignore or similar.", what does this mean??
#  - Question: In the dotenv module, `what does load_env()` do? Ans is GeeksforGeeks
#  - 