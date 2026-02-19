import os  # Importing the os module to interact with the OS
import googlemaps  # Importing the googlemaps module to use Goog le Maps API
import requests  # Importing the requests module to make HTTP requests
import time  # Importing the time module to handle time-related tasks
import sys  # Importing the sys module to access system-specific parameters and functions

GEOCODE_API_KEY = "insert ur key here"  # API key for Google Maps Geocoding
WEATHER_API_KEY = "insert ur key here"  # API key for OpenWeatherMap API
map_client = googlemaps.Client(key=GEOCODE_API_KEY)  # Creating a Google Maps client using the API key

history = []  # List to store a history of user actions and results

# Clear the terminal screen depending on the OS
if os.name == 'nt':
    os.system('cls')  # Clear screen for Windows
else:
    os.system('clear')  # Clear screen on other UNIX-like OS

print("Welcome to Weather Python!")  # Welcome message
print("This is a simple weather application built in Python!.")  # Info message
print("⚠︎ This application will only work in the United States ⚠︎")  # Warning message
input("Press Enter to continue...")  # Wait for user input to continue

# Clear screen again
if os.name == 'nt':
    os.system('cls')  # Clear screen on Windows
else:
    os.system('clear')  # Clear screen on other UNIX-like OS

area = str(input("Please enter your State and Town or Zip Code (Ex: New York, NY OR 10001): "))  # Prompt user for location input

# Clear screen again
if os.name == 'nt':
    os.system('cls')  # Clear screen on Windows
else:
    os.system('clear')  # Clear screen on other UNIX-like OS

def loading(duration):  # CREATED WITH CHATGPT ASSISTANCE and THIS IS MY STUDENT-DEVELOPED PROCEDURE
    # Function to simulate a loading animation
    end_time = time.time() + duration  # Calculate end time based on current time (CHATGPT CREATED THIS LINE)
    dots = ["", ".", "..", "..."]  # Animation frames (CHATGPT CREATED THIS LINE)
    i = 0  # Index for animation frames (CHATGPT CREATED THIS LINE)

    while time.time() < end_time:  # Loop until duration ends (CHATGPT CREATED THIS LINE)
        # IF STATEMENT: Change message if duration is long
        if duration > 5:
            message = "Loading Please Wait"
        else:
            message = "Loading Please Wait (This may take a while)" #Loading Message
        sys.stdout.write("\r" + message + dots[i % len(dots)])  # Print loading message(CHATGPT CREATED THIS LINE)
        sys.stdout.flush()  # Flush stdout (CHATGPT CREATED THIS LINE)
        time.sleep(0.5)  # Wait for 0.5 seconds (CHATGPT CREATED THIS LINE I EDITED THE TIME)
        i += 1  # Increment index

    sys.stdout.write("\rDone!     \n")  # Print done message

loading(6)  # Run loading animation

def location_place(place):  # Function to get lat/lng from location name and
    gecode_result = map_client.geocode(place)  # Call Google Maps geocode API
    get_location = gecode_result[0]['geometry']['location']  # Extract location coordinates
    return get_location  # Return location

def get_weather(api_key, location):  # Function to get weather data using lat/lng
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={location['lat']}&lon={location['lng']}&appid={WEATHER_API_KEY}&units=imperial"  # Construct API URL
    response = requests.get(url)  # Make HTTP GET request
    if response.status_code == 200:  # If request is successful
        return response.json()  # Return response JSON
    else:
        return None  # Return None if request failed

# Clear screen again
if os.name == 'nt':
    os.system('cls')  # Clear screen on Windows
else:
    os.system('clear')  # Clear screen on other UNIX-like OS

# Gives user options to choose from to help get weather data in a simpler format than the one from the API.
# Instead of showing everything in the dictionary, it shows only the data that is listed in the available options.
# Instead of printing each option, it uses a list to store the options and then loops through that list to print them.
menu_options = [
    "Check Temp.",
    "Check Feels like Temp.",
    "Check Humidity.",
    "Check Wind Speed.",
    "Check Visibility.",
    "View History & Exit."
]

while True:  # Infinite loop to display the menu until the user chooses to exit
    for i, option in enumerate(menu_options, start=1):  # Loop through menu options with numbering
        print(f" {i}. {option}")  # Print each menu option

    try:
        choice = int(input("Enter the number of your choice: "))  # Prompt user for menu choice
    except ValueError:
        print("Invalid input. Please enter a number.")  # Handle non-integer inputs
        continue  # Skip to next loop iteration

    if choice == 1:  # Option 1: Temperature
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
            os.system('clear')  # Clear screen on other UNIX-like OS
        temp = get_weather(WEATHER_API_KEY, location_place(area))['main']["temp"]  # Fetch temperature from dictionary
        print("Choose your unit Fahrenheit(F), Celsius(C), Kelvin(K)")  # Ask for unit
        unit_chosen = input("Choose your unit: ")  # Get unit input
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
            os.system('clear')  # Clear screen on other UNIX-like OS
        if unit_chosen == "F":
            result = f"The forecast right now is {round(temp)}°F"  # Display in Fahrenheit
        elif unit_chosen == "C":
            result = f"The forecast right now is {round((temp - 32) / 1.8)}°C"  # Display in Celsius
        elif unit_chosen == "K":
            result = f"The forecast right now is {round((temp - 32) / 1.8 + 273.15)} K"  # Display in Kelvin
        print(result)
        history.append(f"Checked temperature in {area}: {result}")  # Add action/result to history
        input("Press Enter to go back to selection...")  # Go Back to selection
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
            os.system('clear')  # Clear screen on other UNIX-like OS

    elif choice == 2:  # Option 2: Feels like temperature
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
            os.system('clear')  # Clear screen on other UNIX-like OS
        feels_like = get_weather(WEATHER_API_KEY, location_place(area))['main']['feels_like']  # Fetch 'feels like' temp from dictionary
        print("Choose your unit Fahrenheit(F), Celsius(C), Kelvin(K)")
        unit_chosen = input("Choose your unit:")  # Get unit input
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
            os.system('clear')  # Clear screen on other UNIX-like OS
        if unit_chosen == "F":
            result = f"Today's forecast feels like {round(feels_like)}°F right now"
        elif unit_chosen == "C":
            result = f"Today's forecast feels like {round((feels_like - 32) / 1.8)}°C right now"
        elif unit_chosen == "K":
            result = f"Today's forecast feels like {round((feels_like - 32) / 1.8 + 273.15)} K right now"
        print(result)
        history.append(f"Checked 'feels like' temperature in {area}: {result}")  # Add action/result to history
        input("Press Enter to go back to selection...")  # Go Back to selection
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
            os.system('clear')  # Clear screen on other UNIX-like OS

    elif choice == 3:  # Option 3: Humidity
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
            os.system('clear')  # Clear screen on other UNIX-like OS
        humid = get_weather(WEATHER_API_KEY, location_place(area))['main']["humidity"]  # Fetch humidity from dictionary
        result = f"It is {humid}% humid right now."  # Display humidity
        print(result)
        history.append(f"Checked humidity in {area}: {result}")  # Add action/result to history
        input("Press Enter to go back to selection...")  # Go Back to selection
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
            os.system('clear')  # Clear screen on other UNIX-like OS

    elif choice == 4:  # Option 4: Wind Speed and Direction
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
            os.system('clear')  # Clear screen on other UNIX-like OS
        weather_data = get_weather(WEATHER_API_KEY, location_place(area))  # Get full weather data
        wind = weather_data["wind"]["speed"]  # Extract wind speed from dictionary
        direction = weather_data["wind"]["deg"]  # Extract wind direction in degrees from dictionary
        # Convert degrees to cardinal directions
        if direction >= 0 and direction < 90:
            direction_str = "North-East"
        elif direction >= 90 and direction < 180:
            direction_str = "South-East"
        elif direction >= 180 and direction < 270:
            direction_str = "South-West"
        elif direction >= 270 and direction <= 360:
            direction_str = "North-West"
        result = f"The wind speed is {wind} m/s at {direction_str} right now."  # Display wind info
        print(result)
        history.append(f"Checked wind in {area}: {result}")  # Add action/result to history
        input("Press Enter to go back to selection...")  # Go Back to selection
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
            os.system('clear')  # Clear screen on other UNIX-like OS


    elif choice == 5:  # Option 5: Visibility
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
            os.system('clear')  # Clear screen on other UNIX-like OS
        visibility = get_weather(WEATHER_API_KEY, location_place(area))["visibility"]  # Fetch visibility from dictionary
        result = f"The visibility is {visibility} m right now."  # Display visibility
        print(result)
        history.append(f"Checked visibility in {area}: {result}")  # Add action/result to history
        input("Press Enter to go back to selection...")  # Go Back to selection
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
            os.system('clear')  # Clear screen on other UNIX-like OS

    elif choice == 6:  # Option 6: View history & Exit
        loading(3)  # Loading message
        print("~~~~~History~~~~~")  # Display history header
        for entry in history:
            print(entry) #Displays History
        input("Press Enter to exit...") # Wait for user to read history
        print("Exiting...") # Exit message
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
                os.system('clear')  # Clear screen on other UNIX-like OS
        break  # Exit program

    else: # Invalid choice
        print("Invalid choice. Please enter a number between 1 and 6.")  # Handle invalid menu input
        input("Press Enter to try again...")
        if os.name == 'nt':
            os.system('cls')  # Clear screen on Windows
        else:
            os.system('clear')  # Clear screen on other UNIX-like OS
