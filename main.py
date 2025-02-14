#!/usr/bin/python3



from colorama import Fore, Back, Style
from decimal import Decimal, getcontext
from termcolor import colored, cprint
from bs4 import BeautifulSoup 
from datetime import datetime 
from io import StringIO

import requests
import argparse
import textwrap
import shutil
import sys
import math
import time
import textwrap
import os
import json
import html


#when called, it will check if date is within a specific format eg 12h or 24h
def convert_to_used_tz(time_to_change,used_type):

    
    split_time = time_to_change.split(":")
    hours = int(split_time[0])
    mins = str(split_time[1])

    match used_type:
        case "24h":
            return time_to_change
        case "12h":
            if hours >= 13:
                return str(hours-12)+":"+mins+"PM"
            elif hours >= 12:
                return str(hours)+":"+mins+"PM"
            else:
                return time_to_change+"AM"
        case _:
            raise Exception("unknown hour format")
    

#generates the sun data bt simulating a browser action to NOAA's website
def show_sun_data():

            
    #line to end
    res_line = ""

    #gets current time
    cur_date= datetime.today().strftime('%m%d%Y')

    #adds that to a file that may or may not exist, if not it will be created later
    cur_data_file = "/etc/weatherCLI"+url_siders+"/"+name_string+"/date_"+cur_date+".txt"
    
    #this section is so that any file that has the date_ signaute and is not of current date will be deleted
    #gets current directory files
    dir_contents = os.listdir("/etc/weatherCLI"+url_siders+"/"+name_string) 

    #goes through each of them
    for file in dir_contents:

        #checks if have date_ underscore
        if file[:5] == "date_":

            #checks if file as the not current date
            if file != "date_"+cur_date+".txt":

                #deletes file
                os.remove("/etc/weatherCLI/"+url_siders+"/"+name_string+"/"+file)
                
    #checks if file exists
    if os.path.isfile(cur_data_file):

        #reads file and gets a list of data
        sun_file_data = open(cur_data_file, "r").read().split("_")

        #puts data into varables
        sun_rise_time = sun_file_data[0]
        solar_noon_time = sun_file_data[1]
        sun_set_time = sun_file_data[2]
        moon_cycle = sun_file_data[3]

    else:    
        
        #+"&dst=true"
        sun_calc_url = "https://aa.usno.navy.mil/api/rstt/oneday?date="+datetime.today().strftime('%Y-%m-%d')+"&coords="+str(latitude)+","+str(longitude)+"&tz="+str(utc_offset)

        solar_info = json.loads(requests.get(sun_calc_url).text)
    

        #gets data from list
        sun_rise_time = solar_info["properties"]["data"]["sundata"][1]["time"].replace("ST","").replace(" ","")
        solar_noon_time = solar_info["properties"]["data"]["sundata"][2]["time"].replace("ST","").replace(" ","")
        sun_set_time = solar_info["properties"]["data"]["sundata"][3]["time"].replace("ST","").replace(" ","")
        moon_cycle = solar_info["properties"]["data"]["curphase"]

        #opens the current time file and writes
        url_file = open(cur_data_file, "w")
        
        #adds the data to file
        url_file.write(sun_rise_time+"_"+solar_noon_time+"_"+sun_set_time+"_"+moon_cycle)
        url_file.close()
    
    #checks if right time format, if not, it will convert times to that format 
    sun_rise_time = convert_to_used_tz(sun_rise_time,hours_type)
    solar_noon_time = convert_to_used_tz(solar_noon_time,hours_type)
    sun_set_time = convert_to_used_tz(sun_set_time,hours_type)

    #words that goe with the data
    sun_rise = "Sunrise:"
    solar_noon = "Solar Noon(Sun's peak):"
    sun_set = "Sunset:"
    connected = "top"
    

    #gets what sides the row is connected too
    if print_basic_data and print_graph_data:
        connected = "both"
    elif print_basic_data and not print_graph_data:
        connected = "top"
    elif not print_basic_data and print_graph_data:
        connected = "bottom"
    elif not print_basic_data and not print_graph_data and print_warn_data:
        connected = "bottom"
    else:
        connected = "none"

    #generates the bars based on connection
    match connected:
        case "top":
            line = "╠══" + len(sun_rise+" "+ sun_rise_time)*"═" +"╦══" + len(solar_noon+" "+ solar_noon_time)*"═"+"╦"
            line += (full_width - len(line) -2)*"═" + "╣"
            res_line += line +  "\n"
            line = "║ "+sun_rise+" "+ sun_rise_time+" ║ "+solar_noon+" "+ solar_noon_time+" ║ "+ sun_set+" "+ sun_set_time
            res_line += line + (full_width - len(line)-2)*" "+"║ \n"
            line = "╚══" + len(sun_rise+" "+ sun_rise_time)*"═" +"╩══" + len(solar_noon+" "+ solar_noon_time)*"═"+"╩"
            line += (full_width - len(line) -2)*"═" + "╝"
            res_line += line +"\n"
            
        case "bottom":
            line = "╔══" + len(sun_rise+" "+ sun_rise_time)*"═" +"╦══" + len(solar_noon+" "+ solar_noon_time)*"═"+"╦"
            line += (full_width - len(line) -2)*"═" + "╗"
            res_line += line +  "\n"
            line = "║ "+sun_rise+" "+ sun_rise_time+" ║ "+solar_noon+" "+ solar_noon_time+" ║ "+ sun_set+" "+ sun_set_time
            res_line += line + (full_width - len(line)-2)*" "+"║" + "\n"
            line = "╠══" + len(sun_rise+" "+ sun_rise_time)*"═" +"╩══" + len(solar_noon+" "+ solar_noon_time)*"═"+"╩"
            line += (full_width - len(line) -2)*"═" + "╣"
            res_line += line +"\n"
    
        case "both":
            line = "╠══" + len(sun_rise+" "+ sun_rise_time)*"═" +"╦══" + len(solar_noon+" "+ solar_noon_time)*"═"+"╦"
            line += (full_width - len(line) -2)*"═" + "╣"
            res_line += line +  "\n"
            line = "║ "+sun_rise+" "+ sun_rise_time+" ║ "+solar_noon+" "+ solar_noon_time+" ║ "+ sun_set+" "+ sun_set_time
            res_line += line + (full_width - len(line)-2)*" "+"║" +"\n"
            line = "╠══" + len(sun_rise+" "+ sun_rise_time)*"═" +"╩══" + len(solar_noon+" "+ solar_noon_time)*"═"+"╩"
            line += (full_width - len(line) -2)*"═" + "╣"
            res_line += line +"\n"
        case "none":
            line = "╔══" + len(sun_rise+" "+ sun_rise_time)*"═" +"╦══" + len(solar_noon+" "+ solar_noon_time)*"═"+"╦"
            line += (full_width - len(line) -2)*"═" + "╗"
            res_line += line +  "\n"
            line = "║ "+sun_rise+" "+ sun_rise_time+" ║ "+solar_noon+" "+ solar_noon_time+" ║ "+ sun_set+" "+ sun_set_time
            res_line += line + (full_width - len(line)-2)*" "+"║" +"\n"
            line = "╚══" + len(sun_rise+" "+ sun_rise_time)*"═" +"╩══" + len(solar_noon+" "+ solar_noon_time)*"═"+"╩"
            line += (full_width - len(line) -2)*"═" + "╝"
            res_line += line +"\n"
    return res_line 

#converts the forecasts into graphs
def show_graph_data():

    
    res_line = ""
    

    #max height the bars will have
    MAX_HEIGHT = 10
    

    
    #copies the minimum temp forecast and sorts it, geting the first and last items as min and max
    new_min_temp_sorted = temp_forecast_min.copy()
    new_min_temp_sorted.sort()
    
    upper_bounds_min_temp = int(new_min_temp_sorted[-1])
    
    lower_bounds_min_temp = int(new_min_temp_sorted[0])
    
    #copies the maximum temp forecast and sorts it, geting the first and last items as min and max
    new_max_temp_sorted = temp_forecast_max.copy()
    new_max_temp_sorted.sort()
    
    upper_bounds_max_temp = int(new_max_temp_sorted[-1])
    
    lower_bounds_max_temp = int(new_max_temp_sorted[0])
    
    #merges the lists together and sorts them to get the absolute max and min(some days the maximum can be higher than some minimums
    upper_bounds_total_sort = temp_forecast_min + temp_forecast_max
    upper_bounds_total_sort.sort()
    

    #sorts all of the data into absolute min and max
    upper_bounds_total_temp = int(upper_bounds_total_sort[-1])
    lower_bounds_total_temp = int(upper_bounds_total_sort[0])
    

    #gets how much the change in tempreature for each increase in max height
    index_temp = math.ceil((upper_bounds_total_temp-lower_bounds_total_temp)/MAX_HEIGHT)
    

    #converts the raw numbers into how tall the bars will be
    weath_height_max = []
    for max_data in temp_forecast_max:
        weath_height_max.append(math.ceil((int(max_data) - lower_bounds_total_temp)/ index_temp))
    
    weath_height_min = []
    for min_data in temp_forecast_min:
        weath_height_min.append(math.ceil((int(min_data) - lower_bounds_total_temp)/ index_temp))
        
    
    
    #makes the info bars for the the graphs 
    line = "║" 
    
    max_temp_word = "Daily Max Temprature" 
    min_temp_word = "Daily Min Temprature"
    precip_word = "12 Hourly Probability of Precipitation"
    
    line += (string_width)*" " 
    
    line+= max_temp_word
    
    line+= (string_width * len(weath_height_max) - len(max_temp_word)) * " "
    line += (WIDTH_BETWEEN_GRAPHS)*" " 
    
    line += min_temp_word
     

    line+= (string_width * len(weath_height_min) - len(min_temp_word)) * " "

    #adds the width between temp and humitidy graphs
    line += WIDTH_BETWEEN_GRAPHS * " " 
    line += "   " 
    #adds the precitpiton data
    line += precip_word
    line += (3 * len(precip_forecast) - len(precip_word)) * " "
    line += " ║"
    res_line += line + "\n"
    
    line_len = 0

    #because it is made in a terminal the print statements must be calculated top to bottom, 
    #this stats at the highest positon and goes all the way down to -1 where the days are put
    for height in range(MAX_HEIGHT,-2,-1):
    
        line = "║"

        #will generate graphs unless below 0 because that is where the plot names are 
        if height >= 0:

            #prints the average temprature of that bar for the y plot names
            string_temp = str((height)*index_temp + lower_bounds_total_temp)
            line+= string_temp

            #will add an extra space if smaller than string_width
            if len(string_temp) <string_width:
                line += (string_width - len(string_temp))*" "
            

            #goes through each x axis 
            for max_temp_ind in range(len(weath_height_max)):

                #if the height of the weather is equal print the number
                if(height == weath_height_max[max_temp_ind]):
                    
                    #gets the actual number of the data
                    string_temp = str(temp_forecast_max[max_temp_ind])
                    line+= Back.RED+string_temp
                    
                    #will add an extra space if smaller than string_width
                    if len(string_temp) <string_width:
                        line += (string_width - len(string_temp))*" "
                        
                # if less than print red
                elif(height < weath_height_max[max_temp_ind]):
                    line += Back.RED + string_width *" "
                    
                #if more print blue
                else:
                    line += Back.BLUE +string_width *" "

            #re    print(warn_data)sets the backrounds when switching to each graph
            line += Back.RESET
            line += WIDTH_BETWEEN_GRAPHS * " "

            #goes through each x axis
            for min_temp_ind in range(len(weath_height_min)):

                #if the height of the weather is equal print the number
                if(height == weath_height_min[min_temp_ind]):
                    
                    #gets the actual number of the data
                    string_temp = str(temp_forecast_min[min_temp_ind])
                    line+= Back.RED+string_temp
                    
                    #will add an extra space if smaller than string_width
                    if len(string_temp) <string_width:
                        line += (string_width - len(string_temp))*" "
                        
                #if less print red
                elif(height < weath_height_min[min_temp_ind]):
                    line += Back.RED +string_width *" "
                    
                # if more then print blue
                else:
                    line += Back.BLUE +string_width *" "

            #resets the backrounds when switching to each graph
            line += Back.RESET
            line += WIDTH_BETWEEN_GRAPHS * " "
    
    
            # checks if between the heights so it can print the humidity 
            if height >= 0 and height <= 10:
                #multiplies the height by 10 so it can be an number between 0 and 100
                string_temp = str((height)*10)
                line+= string_temp

                #will add an extra space if smaller than string_width
                if len(string_temp) < 3:
                    line += (3 - len(string_temp))*" "

                #prints the bars
                for precip_ind in range(len(precip_forecast)):
    
                    if(height < precip_forecast[precip_ind]/10):
                        line += Back.RED +"   "
                    else:
                        line += Back.BLUE +"   "

                #resets at the end
                line += Back.RESET
            
            
        #this is for the plot names 
        else: 

        
            line += (string_width)*" "        

            
            
            #prints out each day time for each of the bars in the maximum temp
            for day in temp_forecast_max_day:
                days_words.setdefault(day,"HD")
                line += days_words.get(day) + (string_width - len(days_words.get(day)))*" "

            #break between the two graphs
            line += WIDTH_BETWEEN_GRAPHS * " "    
            
            #prints out each day time for each of the bars in the minumum temp
            for day in temp_forecast_min_day:
                days_words.setdefault(day,"HD")
                line += days_words.get(day) + (string_width - len(days_words.get(day)))*" "

            #break between minumum and humidity
            line += WIDTH_BETWEEN_GRAPHS * " "  + "   "  

            # goes through each for the humidity
            for day in precip_day:
                days_words.setdefault(day,"HD")
                line += days_words.get(day) + " "

        #ends the line
        line += " ║"
        line_len = len(line)
        res_line += line +"\n"

    #checks if the warn data is printed so the bars would connect
    if print_warn_data:
        res_line += "╠"+(line_len-2)*"═"+"╣"+"\n"
    else:
        res_line += "╚"+(line_len-2)*"═"+"╝"+"\n"
        
    return res_line
def show_warn_data():


    res_line = ""

    #gets all of the warnings between the top and bottom sections as this stays the same depending which side connected to
    def print_meat():
        all_line = ""

        #goes through all of the warnings
        for index, hazard_data_link in enumerate(warn_data):

            #prints the arning and then adds whitespace between the rest
            all_line += "║ " + hazard_data_link[0] +": " + " "*(full_width-len(hazard_data_link[0])-6) +"║"+" \n"

            #prints the link for the national weather service
            small_url = hazard_data_link[1][0:hazard_data_link[1].find("local_place1")-1] 
            all_line += "║ " + small_url+ " "*(full_width- len(small_url)-4)+ "║  \n"
            
            #prints a connecter if not the end of the warnings
            if index != len(warn_data)-1:
                all_line += "╠"+ "═"*(full_width-3) + "╣" + "\n"
        return all_line

    #text for no warnings
    no_warnings_text = "No Watches, Warnings, or Advisories"
    
    # checks if connected betwen anywhere else
    if print_graph_data or print_basic_data or print_sun_data:

        #prints out each day time for each of the bars in the maximum temp
        if len(warn_data) != 0:
            res_line += print_meat()
            res_line += "╚"+ "═"*(full_width-3) + "╝" + "\n"  
        else:
            res_line += "║ "+ no_warnings_text +  " "*(full_width-len(no_warnings_text)-4) + "║ \n"
            res_line += "╚"+ "═"*(full_width-3) + "╝" + "\n"         

    #checks if not connected anywhere, so it will just be alone
    elif print_basic_data == False and print_sun_data == False and print_graph_data == False:
 
        #prints out each day time for each of the bars in the maximum temp
        if len(warn_data) != 0:
            res_line += "╔"+ "═"*(full_width-3) + "╗" + "\n"
            res_line += print_meat()
            res_line += "╚"+ "═"*(full_width-3) + "╝" + "\n" 
        else:
            res_line += "╔"+ "═"*(full_width-3) + "╗" + "\n"
            res_line += "║ "+ no_warnings_text +  " "*(full_width-len(no_warnings_text)-4) + "║ \n"
            res_line += "╚"+ "═"*(full_width-3) + "╝" + "\n"          
            
    else:
        None

    return res_line
    
def show_basic_data():

    #converts long form into shortform
    temp_conversion = {
        "Fahrenheit":"F",
        "Celcius":"C"
    }
    

    #gets elevation and location information
    res_line = "╔"+ "═"*(full_width-3) + "╗" + "\n"
    line ="║ Your Location: "+ name + "  Elevation: " +height +" "+ height_units +" "+ str(longitude)+"E " + str(latitude) + "N" 
    res_line += line +  " "*(full_width - len(line)-2) +"║\n"

    
    line = "║ Local Station URL: " + weatherURL 
    res_line += line + " "*(full_width - len(line)-2) +"║\n"

    line = "║ " +local_station_weather_type +" at "+local_station_name 
    res_line += line + " "*(full_width - len(line)-2) +"║\n"

    line = "║ Temp: " + local_station_temp.replace(" ","") +temp_conversion[temp_units]+"  Dew point: "
    line += local_station_dew_point.replace(" ","")+ temp_conversion[temp_units] +"  " + "Humidity: "
    line += local_station_humidity.replace(" ","")+"%  Visbility: "+local_station_visibility.replace(" ","")+ " "+ visibility_units 
    res_line += line + " "*(full_width - len(line)-2) +"║\n"

    line = "║ Wind Direction: "+local_station_wind_dir + "°  Sustained Wind: "+ local_station_wind_sustained+" "+ wind_units 
    line += "  Gust: "+local_station_gust.replace(" ","")+" " +wind_units
    res_line += line + " "*(full_width - len(line)-2) +"║\n"

    #checks if the bottom is connected to anything if so it will change the bars to connecting ones
    if not print_sun_data:
        if print_graph_data or print_warn_data:
            res_line += "╠"+ "═"*(full_width-3) + "╣" + "\n"   
        else:
            res_line += "╚"+ "═"*(full_width-3) + "╝" + "\n"   

    
    return res_line


if __name__ == '__main__':

    string = ""
    
    WIDTH_BETWEEN_GRAPHS = 3
    
    #default config for all modules
    print_basic_data = False
    print_sun_data = False
    print_graph_data = False
    print_warn_data = False

    
    #default time format
    hours_type = "12h"

    #timezones in the United States and it's territorys
    timezones = {
        "est": -5,
        "cst":-6,
        "mst":-7,
        "pst":-8,
        "akst":-9,
        "hst":-10,
        "aoe":-12,
        "sst":-11,
        "ast":-4,
        "chst":10,
        "wakt":12
    }

    #tells program what parent directory to put the files in
    url_type = {
        "zip":"/zipcode",
        "city":"/towns",
        "town":"/towns",
        "poi":"/places"   
    }
    
    #generates aruements
    parser = argparse.ArgumentParser(
        prog='PROG',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            
            This application is designed to calculate the sun and weather from a specific location using NOAA and AAD. 
            
            !important! This program only works for places within the United States and it's Territorys

            
            
            Application for generating weather using data from NOAA
            -------------------------------------------------------
            https://www.noaa.gov/
            https://weather.gov/


            API for sun information from Astronomical Applications Department
            -----------------------------------------------------------------
            https://aa.usno.navy.mil/data/api
            https://aa.usno.navy.mil/api/

            Geocoding for latitude and longitude using data from OpenStreetMap
            ------------------------------------------------------------------
            https://openstreetmap.org/copyright   
            https://nominatim.openstreetmap.org/


            Example zipcode querys:
                \"poi:Rochester Insitute of Technology\"
                \"zip:14623\"
                \"town:Rochester NY\"
             
            Default time format: 12 hours

        '''))
    parser.add_argument("zipcode", type=str, help="town or city name shoud be the query \"town:<town name> <State>\" zipcodes should be \"zip:<zipcode>\" and points of intrest should be \"poi:<placename>\"")
    parser.add_argument("-t", "--type", type=str, help="how complatated the data will be: simple | all | onlywarnings | onlysun<Timezone> eg: onlysunEST or onlysunCST",default="All")
    parser.add_argument("-s", "--sun", type=str, help="shows sun data",default="none")
    parser.add_argument("-i", "--ignoreSizeRequirements", help="The program will ignore the width of the display", action='store_true')
    parser.add_argument("-t12", "--time12h", help="12h clock", action='store_true')
    parser.add_argument("-t24", "--time24h", help="24h clock", action='store_true')




    
    #runs arguments
    args = parser.parse_args()


    if args.time12h and args.time24h:
        raise Exception("Time format must be t12 or t24 hours")
    
    if args.time12h:
        hours_type = "12h"

    if args.time24h:
        hours_type = "24h"
    
    #trys to see if contains a website, 
    if args.zipcode.count("https://") == 1:
        if args.zipcode.count("https://forecast.weather.gov/MapClick.php") == 1:
            string = args.zipcode
        else:
            raise Exception("URL is not from NWS or incorrect. URL should be https://forecast.weather.gov/MapClick.php followed by query information")
    else:

        #this is the string that represents the name of the directory
        name_string = args.zipcode[args.zipcode.find(":")+1:]
   
        #this is the string that repprepents name_string's parent directory
        url_siders = url_type.get(args.zipcode[:args.zipcode.find(":")].lower(),"None")
        
        #returns error if no type
        if url_siders == "None":
            raise Exception("header is invalid, begin with zip: poi: town: city:")
        
        
        #new file for location
        url_file = "/etc/weatherCLI"+url_siders+"/"+name_string+"/url.txt"

        #checks if exists
        if os.path.isfile(url_file):

            #opens and clears out file
            url_file = open(url_file, "r")
            string = url_file.read().replace(" ","")
            if string == "":
                shutil.rmtree("/etc/weatherCLI"+url_siders+"/"+name_string)
                raise Exception("url file empty, so zip directory was deleted. Try again")
    
        else:
            print("generating "+args.zipcode)

            #will make a directory and add it
            os.makedirs("/etc/weatherCLI"+url_siders+"/"+name_string)
            url_file = open(url_file, "w")

            #gets what type of request it is from
            match args.zipcode[:args.zipcode.find(":")].lower():
                case "zip":

                    url_string = "https://nominatim.openstreetmap.org/search.php?country=US&postalcode="+args.zipcode[4:]+"&countrycodes=us&format=jsonv2"
                case "poi":

                    url_string = "https://nominatim.openstreetmap.org/search.php?street="+args.zipcode[4:].replace(" ","+")+"&country=US&countrycodes=us&format=jsonv2"
                case "town":
  
                    url_string = "https://nominatim.openstreetmap.org/search.php?q="+ args.zipcode[5:][:args.zipcode[5:].rfind(" ")]+"+USA&format=jsonv2"
                case "city":
    
                    url_string = "https://nominatim.openstreetmap.org/search.php?q="+ args.zipcode[5:][:args.zipcode[5:].rfind(" ")]+"+USA&format=jsonv2"

                case _:
                    raise Exception("header is invalid, begin with zip: poi: town: city:")

            #generates useragent
            user_agent = {'User-agent': 'Mozilla/5.0'}

            #gets from openstreetmap, using useragent and converts the output into json
            loc_json= json.loads(requests.get(headers = user_agent, url = url_string).text)


            #checks if result is empty, if so then delete direcory and throw error
            if len(loc_json) == 0:

                #deletes entry
                shutil.rmtree("/etc/weatherCLI"+url_siders+"/"+name_string)
                raise Exception("invalid place name/zipcode/POI")

            #gets the most likely entry
            loc_json = loc_json[0]
            
            #generates the final string using coords
            string = "https://forecast.weather.gov/MapClick.php?lat="+loc_json["lat"]+"&lon="+loc_json["lon"]+"&unit=0&lg=english&FcstType=dwml"
            
            #writes and closes the data
            url_file.write(string)
            url_file.close()
            

    
    sun_calculated = False
    
    if args.sun != "none":

        #trys to get the utc ofsett from the dictonary, returns UNK if unknown
        utc_offset = timezones.get(args.sun.lower(),"UNK")

        #throws new exception if unknown timezone
        if utc_offset != "UNK":
            print_sun_data = True
        else:
            raise Exception("unknown timezone")
        sun_calculated = True

    #generates possible modules to be enabled
    match args.type.lower():
        case "simple":
            print_basic_data = True
        case "all":
            print_basic_data = True
            print_graph_data = True
            print_warn_data = True
        case "onlywarnings":
            print_warn_data = True

    #checks if the args is for sun calculation only
    if args.type.lower().find("onlysun") != -1:

        #throws an error if already enabled
        if sun_calculated:
            raise Exception("onlysun and -s are incompatable")

        #gets the utc offset, UNK is if none found 
        utc_offset = timezones.get(args.type.lower()[7:],"UNK")

        #throws an error if unknown timezone
        if utc_offset != "UNK":
            print_sun_data = True
        else:
            raise Exception("unknown timezone")

        
        
    #testing strings
    
    # string = "https://forecast.weather.gov/MapClick.php?lat=46.8083&lon=-100.7837&unit=0&lg=english&FcstType=dwml"
    # #string = "https://forecast.weather.gov/MapClick.php?lat=43.0871&lon=-77.5962&unit=0&lg=english&FcstType=dwml"
    # #string = "https://forecast.weather.gov/MapClick.php?lat=43.6591&lon=-70.2568&unit=0&lg=english&FcstType=dwml"
    # #string = "https://forecast.weather.gov/MapClick.php?lat=39.056&lon=-95.69&unit=0&lg=english&FcstType=dwml"
    # #string = "https://forecast.weather.gov/MapClick.php?lat=45.2159&lon=-122.0609&unit=0&lg=english&FcstType=dwml"\
    # #string = "https://forecast.weather.gov/MapClick.php?lat=42.3587&lon=-71.0567&unit=0&lg=english&FcstType=dwml"
    # #string = "https://forecast.weather.gov/MapClick.php?lat=30.5&lon=-81.69&unit=0&lg=english&FcstType=dwml"
    # #string = "https://forecast.weather.gov/MapClick.php?lat=43.8014&lon=-91.2396&unit=0&lg=english&FcstType=dwml"
    # #string = "https://forecast.weather.gov/MapClick.php?lat=43.8014&lon=-91.2396&unit=0&lg=english&FcstType=dwml"
    
    #gets the xml from NOAA

    
    weather_data = requests.get(string)
    weather_xml = BeautifulSoup(weather_data.text, "xml")
    
    #tryst to get either locations from data
    try:
        name = weather_xml.find("location").find("area-description").text
    except:
        name = weather_xml.find("location").find("description").text
        
    location = weather_xml.find("location").find("point")
    
    #gets data about location
    height = weather_xml.find("height").text
    
    latitude = float(location.attrs.get("latitude"))
    longitude = float(location.attrs.get("longitude"))
    
    #redirects to the full page
    weatherURL = weather_xml.find("moreWeatherInformation").text
    
    
    #gets local station data(location where actual sensors are)
    station = weather_xml.find_all("data")[1]
    
    local_station_name = station.find("location").find("area-description").text
    
    
    local_station_temp = station.find_all(attrs={"type" : "apparent"})[0].text[1:]
    local_station_dew_point = station.find_all(attrs={"type" : "dew point"})[0].text[1:]
    
    local_station_humidity = station.find_all("humidity",attrs={"type" : "relative"})[0].text[1:]
    
    local_station_weather_type = station.find_all("weather-conditions")[0].get_attribute_list("weather-summary")[0]
    
    local_station_visibility = station.find_all("weather-conditions")[1].find("visibility").text
    
    local_station_wind_dir = station.find_all("direction")[0].find("value").text
    
    local_station_gust = station.find_all("wind-speed",attrs={"type" : "gust"})[0].find("value").text
    local_station_wind_sustained = station.find_all("wind-speed",attrs={"type" : "sustained"})[0].find("value").text
    
    
    #units
    wind_units = station.find("wind-speed").get_attribute_list("units")[0]
    visibility_units = station.find_all("weather-conditions")[1].find("visibility").get_attribute_list("units")[0]
    temp_units = station.find_all(attrs={"type" : "apparent"})[0].get_attribute_list("units")[0]
    height_units = station.find("location").find("height").get_attribute_list("height-units")[0]
    
    
    
    
    
    #generates a list of time formats to use
    time_keys = {}
    
    for time_layout in weather_xml.find_all("time-layout"):
    
        day_data = []
        for day_text in time_layout.find_all("start-valid-time"):
            day_data.append(day_text.get_attribute_list("period-name")[0])
        
        time_keys[time_layout.find("layout-key").text] = day_data
    
    
    #gets preciptiation probability
    precip_forecast = []
    for data in weather_xml.find("probability-of-precipitation").find_all("value"):
        if data.text != '':
            precip_forecast.append(int(data.text))
        else:
            precip_forecast.append(0)
    
    #minimimum temp for day
    temp_forecast_min = []
    for data in weather_xml.find("temperature",attrs={"type" : "minimum"}):
        if data.text != "Daily Minimum Temperature" and data.text != "\n":
            temp_forecast_min.append(int(data.text))
    
    #gets the days from the data
    temp_forecast_max_day = time_keys[weather_xml.find("temperature",attrs={"type" : "maximum"}).get_attribute_list("time-layout")[0]]
    temp_forecast_min_day = time_keys[weather_xml.find("temperature",attrs={"type" : "minimum"}).get_attribute_list("time-layout")[0]]
    precip_day = time_keys[weather_xml.find("probability-of-precipitation").get_attribute_list("time-layout")[0]]
    
    #maximum temp for day
    temp_forecast_max = []
    for data in weather_xml.find("temperature",attrs={"type" : "maximum"}):
        if data.text != "Daily Maximum Temperature" and data.text != "\n":
            temp_forecast_max.append(int(data.text))
            
    
    
    #gets the warnings from the document if len is 0 then no warnings
    warn_data = []
    try:
        for hazard in weather_xml.find_all("hazard"):
            hazard_name = hazard.get_attribute_list("headline")[0]
            hazard_url = hazard.find("hazardTextURL").text
            warn_data.append([hazard_name,hazard_url])
        
    except:
        None
    
    #converts the long days to short form
    days_words = {
            "Saturday":"Sa",
            "Sunday":"Su",
            "Monday":"Mo",
            "Tuesday":"Tu",
            "Wednesday":"We",
            "Thursday":"Th",
            "Friday":"Fr",
            "Tonight":"TO",
            "Saturday Night":"SN",
            "Sunday Night":"SN",
            "Monday Night":"MN",
            "Tuesday Night":"TN",
            "Wednesday Night":"WN",
            "Thursday Night":"TN",
            "Friday Night":"FN",
            "Overnight":"ON",
            "This Afternoon":"TA"
        }
    
    
    #calculates wanted width for each bar
    string_width = 0
        
    for i in temp_forecast_min+temp_forecast_max:
        if string_width < len(str(i)):
            string_width = len(str(i));
    string_width +=2
    
    
    
    #gets terminal size

    columns, rows = shutil.get_terminal_size()
    
    #temp for testing on jupyterlab
    #columns = 176
    
    #calculates how wide the window will be because some temps are more than two digites ie 100 degrees
    full_width = 1 + string_width * (len(temp_forecast_min)+len(temp_forecast_max)+1) + WIDTH_BETWEEN_GRAPHS*2 + 3 + 3*len(precip_forecast) + 3
    
    #checks if the window width is greater than the TUI window
    all_lines = "" 

    if columns >= full_width or args.ignoreSizeRequirements:
    
        #iterates through each of the functiins
        if print_basic_data:
            all_lines += show_basic_data()
        if print_sun_data:
            all_lines += show_sun_data()
        if print_graph_data:
            all_lines += show_graph_data()
        if print_warn_data:
            all_lines += show_warn_data()
    else:
        #tells user that screen size is too small
        print("screen width of: "+str(columns)+" is too small")
    
    #the final rezult is all in one printable variable
    print(all_lines)
