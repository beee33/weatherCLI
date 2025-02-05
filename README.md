# weatherCLI

WeatherCLI is a Linux command line UI based application that shows the user the weather from the National Weather Service written in Python



## What kind of data can the application show:

weather warnings(eg: Frost Advisory, Winter Storm Warning or Severe Thunderstorm Warning) 

Sun data:

- Sunrise
- Sunset
- Solar noon


Live data from the location’s nearest weather station:
- Temperature
- Humidity
- Visibility
- Dew point
- Name of station
- Wind direction
- Sustained wind speed
- Wind gusts
- Local station url if you want to get more information:

Temperature graphs:
- Daily low
- Daily high

12 hour Precipitation probability graphs

## How does weatherCLI get its data?

The National Weather Service allows you to generate XML files showing weather data from a specific longitude and latitude. This program reads those XML files and presents them to the user as readable data. To calculate the sun positions, the program temporarily downloads the Javascript from NOAA’s old solar calculator: https://gml.noaa.gov/grad/solcalc/sunrise.html, and injects some javascript code to generate sun positions at time and location. It then uses js2py to compile the Javascript to Python.


## Download
### Build from source


#### install pyinstaller

    pip install pyinstaller

#### compile to standalone binary
    pyinstaller main.py --onefile

#### Copy the new binary to the bin directory so it can be accessed by users
    sudo cp dist/main /usr/bin/weatherCLI

#### Change perms so that any user can access it,but not modify it's code
    sudo chmod 755 /usr/bin/weatherCLI

#### make the data directory
    sudo mkdir /etc/weatherCLI

#### change access to all users

    sudo chmod 777 -R /etc/weatherCLI

**_*note this directory and its subdirectorys is intended to be accessible for all users_**

#### if you only want people with sudo perms to access it:

    sudo chmod 711 -R /etc/weatherCLI



#### potental problems with compiling

if you get the error: "[PYI-1890462:ERROR] Failed to load Python shared library '/tmp/_MEIWYQO9N/libpython3.10.so': dlopen: /tmp/_MEIWYQO9N/libpython3.10.so: cannot open shared object file: No such file or directory"

This command fixes that so pyinstaller knows python's path.
This should be replaced with your python version, I was using python 3.10.

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/python3.10


### from installer



## How does weatherCLI know the location?

WeahterCLI uses OpenStreetMaps’s geocoding API to get latitude and longitude positions from user input. It converts the latitude and longitude into a url that has the XML data. This url is stored in “/etc/weatherCLI/&lt;towns/zipcode/places&gt;/&lt;queryname&gt;/url.txt” an example is: “/etc/weatherCLI/towns/Boston\ MA/url.txt”.  The data for the sun positions are only calculated once per day per location, and the output is put in a file so that the user doesn't have to recalculate the same sun data for each day. All of the urls and sun data is stored in “/etc/weatherCLI/”




#### Configurable to the data you want to see:
<video autoplay src=''></video>

#### Calculates sunrise and sunset:
<video autoplay src=''></video>


#### Can get weather from zipcode, town/city name or point of intrest(ie: schools, goverment buildings and airports):
<video autoplay src=''></video>

#### Inbuilt documentation:
<video autoplay src=''></video>

### *video only edited to speed up typing (program running time is at real time speed)
