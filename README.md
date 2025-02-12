# weatherCLI

weatherCLI is a Linux command line UI based application that shows the user the weather and sun information from the National Weather Service written in Python. 
Because of this, weatherCLI is only available in the United States, and its territories, However, the sun calculation is available for most of the places that share the same timezones as the United States, examples: Canada, Mexico and parts of western South America.


![weatherCLI_image](https://github.com/user-attachments/assets/48d7198f-9ad0-4703-987c-cde9ec7c40e8)


Application for generating weather using data from NOAA
-------------------------------------------------------
https://www.noaa.gov/
<br>
https://weather.gov/
<br>
https://gml.noaa.gov/grad/solcalc/sunrise.html

Geocoding for latitude and longitude using data from OpenStreetMap
------------------------------------------------------------------
https://openstreetmap.org/copyright   
<br>
https://nominatim.openstreetmap.org/


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
- Wind gusts (will show NA knots if no gusts)
- Local station url if you want to get more information:

Temperature graphs:
- Daily low
- Daily high

12 hour Precipitation probability graphs

## How does weatherCLI get its data?

The National Weather Service allows you to generate XML files showing weather data from a specific longitude and latitude. This program reads those XML files and presents them to the user as readable data. To calculate the sun positions, the program temporarily downloads the Javascript from NOAA’s old solar calculator: https://gml.noaa.gov/grad/solcalc/sunrise.html, and injects some javascript code to generate sun positions at time and location. It then uses js2py to compile the Javascript to Python.

## Supported operating systems
| OS           | Supported?                     |
| :----------- | :--------------:               |
| Debian       | :white_check_mark:             | 
| Ubuntu       | :white_check_mark:             |
| Fedora | :white_check_mark:    |
| Arch | :white_check_mark:  |
| Mint | :large_orange_diamond: |
| Pop OS | :large_orange_diamond: |
| EndeavourOS | :large_orange_diamond: |
| Windows      | :x: |


:white_check_mark:: Supported
<br>
:large_orange_diamond:: Untested
<br>
:x:: Broken

## Download

### from installer:

#### Dependencys: wget

Can be installed from almost all package managers:

Debian/Ubuntu/Mint:

    sudo apt install wget

Arch:

    pacman -S wget

Fedora

    sudo dnf install wget
    
*may already be installed
    
#### download installer script:

    wget https://raw.githubusercontent.com/beee33/weatherCLI/main/installer.sh 
#### run script:

    sudo sh installer.sh

### just run python file instead:
TBD

### Build from source:

#### download file

    wget https://raw.githubusercontent.com/beee33/weatherCLI/main/main.py 

#### install pyinstaller

    pip install pyinstaller

*Note, you may have to use a virtual enviroment for some systems. You can use something like pyenv to create instances of python with diffrent versions: https://github.com/pyenv/pyenv 
<br>
For this program I would reccomend using python 3.10, as that is what version this program is written for. 

cd into weatherCLI directory
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
This should be replaced with your python version and the temp directory may be diffrent, I was using python 3.10.

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/python3.10



## How does weatherCLI know the location?

WeahterCLI uses OpenStreetMaps’s geocoding API to get latitude and longitude positions from user input. It converts the latitude and longitude into a url that has the XML data. This url is stored in “/etc/weatherCLI/&lt;towns/zipcode/places&gt;/&lt;queryname&gt;/url.txt” an example is: “/etc/weatherCLI/towns/Boston\ MA/url.txt”.  The data for the sun positions are only calculated once per day per location, and the output is put in a file so that the user doesn't have to recalculate the same sun data for each day. All of the urls and sun data is stored in “/etc/weatherCLI/”




#### Configurable to the data you want to see:
<video autoplay src='https://github.com/user-attachments/assets/0d54eb4c-fbcb-4a5f-94e7-dd34c54d86c7'></video>





#### Calculates sunrise and sunset:
<video autoplay src='https://github.com/user-attachments/assets/055b9d86-cfbb-4416-9768-d3c778f76a3a'></video>






#### Can get weather from zipcode, town/city name or point of intrest(ie: schools, goverment buildings and airports):
<video autoplay src='https://github.com/user-attachments/assets/01623921-4ded-4bad-91e4-9441a3886d2e'></video>


#### Can Combine multiple tags:
<video autoplay src='https://github.com/user-attachments/assets/c7cb0ef4-c09d-4883-9a77-504ab44887d4'></video>

#### Inbuilt documentation:
<video autoplay src='https://github.com/user-attachments/assets/e87a1e42-ea32-45a8-bb17-eb480c3a8ebd'></video>

### *video only edited to speed up typing (program running time is at real time speed)

