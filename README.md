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

API for sun information from Astronomical Applications Department
-----------------------------------------------------------------
https://aa.usno.navy.mil/data/api
<br>
https://aa.usno.navy.mil/api/
<br>

Geocoding for latitude and longitude using data from OpenStreetMap
------------------------------------------------------------------


https://nominatim.openstreetmap.org/
<br>
https://openstreetmap.org/copyright   
<br>


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

The National Weather Service allows you to generate XML files showing weather data from a specific longitude and latitude. This program reads those XML files and presents them to the user as readable data. To get the sun positions, the program uses the US Navy's API for getting sun info expressed in json, and prints the result out on terminal.

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

#### 1. Dependencys: wget

Can be installed from almost all package managers:

Debian/Ubuntu/Mint:

    sudo apt install wget

Arch:

    pacman -S wget

Fedora

    sudo dnf install wget
    
*may already be installed
    
#### 2. download installer script:

    wget https://raw.githubusercontent.com/beee33/weatherCLI/main/installer.sh 
#### 3. run script:

    sudo sh installer.sh

### Only run python file instead:

#### 1. download repo and download dependencies

[Follow Build from source instructuions until the end of step 4](#build-from-source)


#### 2. Run python fille

    python3 main.py

### Build from source:

#### 1. Install git

Instructions to install git are on: [Git's website](<https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>)
however you can just use:

Debian/Ubuntu/Mint:

    sudo apt install git

Fedora

    sudo dnf install git

#### 2. download repo

    git clone "https://github.com/beee33/weatherCLI"

#### Configure venv

#### 3. cd into weatherCLI directory

    cd weatherCLI

#### 4a. Recommended: use python venv 

Create new virtual enviroment using python's venv

    python3 -m venv <name>

Enter venv

    
    source <name>/bin/activate
*Note: if venv works, your shell should have (&lt;name&gt;) in prompt
Install dependencys

    python3 -m pip install -r requirements.txt
<br>
<br>

#### 4b. Not recommended: run without venv
:exclamation: some Operating Systems eg: Debian, dont like you to install packages in the default python environment, as it may override system packages that are needed. I have bricked a VM by doing this.
<br>
<br>
Install dependencys

    python3 -m pip install -r requirements.txt


<br>
<br>

#### 5. install pyinstaller

    pip install pyinstaller

or

    python3 -m pip install pyinstaller

*Note, you may have to use a virtual enviroment for some systems. You can use something like pyenv to create instances of python with diffrent versions: https://github.com/pyenv/pyenv 
<br>
For this program I would reccomend using python 3.10, as that is what version this program is written for. If not, try to rename all instances of it to your python version





#### 6. compile to standalone binary if you use venv

This adds the new venv site packages path to pyinstaller, so it can use it. You should replace python3.10 with your python version eg python3.11
    
    pyinstaller main.py --onefile --paths "<name>/lib/python3.10/site-packages"


Leave virtual enviroment

    deactivate

<br>
<br>

#### 7. compile to standalone binary if you dont use venv

    pyinstaller main.py --onefile

<br>
<br>
<br>
<br>

#### 8. Copy the new binary to the bin directory so it can be accessed by users
    sudo cp dist/main /usr/bin/weatherCLI

#### 9. Change perms so that any user can access it,but not modify it's code
    sudo chmod 755 /usr/bin/weatherCLI

#### 10. make the data directory
    sudo mkdir /etc/weatherCLI

#### 11a. change access to all users

    sudo chmod 777 -R /etc/weatherCLI

**_*note this directory and its subdirectorys is intended to be accessible for all users_**

#### 11b. if you only want people with sudo perms to access it:

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

