# weatherCLI

weatherCLI is a Linux command line UI based application that shows the user the weather and sun information from the National Weather Service written in Python. 
Because of this, weatherCLI is only available in the United States, and its territories, However, the sun calculation is worldwide.

<img src="https://github.com/user-attachments/assets/eb9a932e-d8c4-4070-9cf4-cd73e49b40bb" width="100%" ></img>

AI Statment
-----------
NO AI was used in making this program

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


Human readable worded weather from NOAA's API (example: Partly cloudy, with a low around 32. West wind 5 to 14 mph):
- Both day and night are unique
- Up to one week forecast


Graphs:
- Precipitation type & Probability 
- Daily low
- Daily high


Sun data:
- Sunrise
- Sunset
- Solar noon
- Moon info


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


weather warnings (example: Frost Advisory, Winter Storm Warning or Severe Thunderstorm Warning) 



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

## Install
You can either run the program as a Python binary though the script, run it in a virtual envirotment with venv and compile it yourself without the instlation script(only usefull if you helping develop this software).


<details>
  <summary>
      <h3> Option 1: download instlation script</h3>
  </summary>
Depenencies:
    
- python3
- git
- curl

__Instlation Script:__

    curl https://raw.githubusercontent.com/beee33/weatherCLI/master/main.py -o install-non-root.sh 


__Read script, this is optional. However you should always review programs before you give them access to your computer:__
    
    less install-non-root.sh 

__Make Executable:__

    chmod +x install-non-root.sh 

__Run Script__

This script gives you a choice on either to compile it yourself or just download the binary. Try compiling it if you are on a non Intel based processor.
    

    ./install-non-root.sh 


</details>
<details>
  <summary>
    <h3>Option 2: Run in a Virtual Enviorment and Compile it yourself</h3>
  </summary>
      Depenencies:
    
- python3
- git

__Download this git:__

    git clone https://github.com/beee33/weatherCLI
    cd weatherCLI

__Make Virtual Enviorment__

    python3 -m venv <name>

__Enter Virtual Enviroemnt__

    source <name>/bin/activate

__Install Dependencies__

    python3 -m pip install -r requirements.txt

__Prepare the Configuration locations__
Your system may not have ~/.config folder, and you may need to make it.

    mkdir ~/.config/weatherCLI
    

__Run the Program__
The program should work as expected, but you may want to compile it into a binary using pyinstaller
    
    python main.py


## Compiling this program
I used pyinstaller to make this python program into a binary that has all depencenices bundled in, and this is how I make the binaries for this project. For this to work you need to have created your virtual envorment and installed all the depenencies.

    pip install pyinstaller

Compile the Program:

    pyinstaller main.py --onefile

Your binary should be ./dist/main 

    mv dist/main weatherCLI

make executable with:

    chmod +x weatherCLI
    

### leaving the virtual enviorment

    deactivate

</details>


## generating requiremnts.txt
only needed to do if you installed some new packages for this program.
   
    pip freeze > requirements.txt


## How does weatherCLI know the location?

WeathterCLI uses OpenStreetMaps’s geocoding API to get latitude and longitude positions from user input. It converts the latitude and longitude into a url that has the XML data. This url is stored in “/etc/weatherCLI/&lt;towns/zipcode/places&gt;/&lt;queryname&gt;/url.txt” an example is: “/etc/weatherCLI/towns/Boston\ MA/url.txt”.  The data for the sun positions are only calculated once per day per location, and the output is put in a file so that the user doesn't have to recalculate the same sun data for each day. All of the urls and sun data is stored in “/etc/weatherCLI/”

# CLI examples:
<br>

    weatherCLI "city:Boston MA" -t most -s 

<img src="https://github.com/user-attachments/assets/24a22a27-4192-432b-adff-5109ccf5ceaf" width="100%" ></img>
-----------------

    weatherCLI "poi:Rochester Institute of Technology" -t most
<img src="https://github.com/user-attachments/assets/e9955d3a-bd70-4731-a5d7-b129e0f2eeea" width = "100%"></img>
-----------------

    weatherCLI "zip:10001" -t most -s 
<img src="https://github.com/user-attachments/assets/4770f279-50a9-418a-8fe1-b2222a0430f5" width = "100%"></img>
-----------------

    weatherCLI "city:Palm Beach FL" -t all -s 
<img src="https://github.com/user-attachments/assets/31e768aa-64ec-4379-a70b-2972c2a859dc" width = "100%"></img>
-----------------

    weatherCLI "city:Seattle WA" -t24 -t onlysun
<img src="https://github.com/user-attachments/assets/d42893ca-a9ac-4d9e-8e21-eeacacc07755" width = "100%"></img>
-----------------

    weatherCLI "city:Salt Lake City UT" -t onlyworded
<img src="https://github.com/user-attachments/assets/1cc6b228-3e84-417f-9105-aaf94733fe82" width = "100%"></img>
