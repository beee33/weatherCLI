#!/bin/bash

# check if running root, if not exit
if [[ $UID != 0 ]]
then
 	echo "script requires sudo permissions";
	exit 1;
fi

# function to remove only the binary file
remove_weather_cli() {
	
	# checks if file exists if not tell the user, having not binary is not a catastrophic problem
	if [ -e /usr/bin/weatherTUI ]
        then

		# deletes file
		rm /usr/bin/weatherTUI;
		echo "deleted: /usr/bin/weatherTUI";
	else
		echo "ERROR: data directory not found, so not deleting";
	fi

	
}

# removes all of the config files within /etc/weatherTUI
remove_weather_cli_files() {


	# checks if file exists
	if [ -e /etc/weatherTUI ] 
	then 
		rm -r /etc/weatherTUI 
		echo "deleted: /etc/weatherTUI";
	else
		echo "ERROR: weatherTUI file not found, so not deleting";
	fi
}

# runs both deleting functions to fully remove the program from your computer
remove_all() {
	remove_weather_cli 
	remove_weather_cli_files
}

# installer function
install_weather() {
	echo "installing";
	
	# downloads latest file
        wget https://github.com/beee33/weatherTUI/releases/latest/download/weatherTUI
   	echo "downloaded files";
	
	if [ -f weatherTUI ] 
	then
       		mv weatherTUI /usr/bin/weatherTUI
        	echo "moved to bin";		
	else
		echo "ERROR: weatherTUI is a directory, dont use installer in the same direcory as weaterCLI directory";
		exit 1;
	fi


	# checks if data directory already exists
	if [ -e /etc/weatherTUI ]
	then
		echo "directory /etc/weatherTUI already exists";
	else
		# makes config directory
		mkdir /etc/weatherTUI
		echo "made data directory";

		# gives 777 perms to directory(directory meant to be accessable by all users
		chmod 777 -R /etc/weatherTUI
		echo "perms given to file";
	fi

	# gives permitions to execute and read binary, but can only write if root
	chmod 755 /usr/bin/weatherTUI
}

# runs loop to so it will the user will have to put in the right input
while true
do
	echo "weatherTUI installer";
	echo " 1) install weatherTUI";
	echo " 2) remove weatherTUI";
	echo " 3) exit";

	# prints out a command prompt that reads to the install_type variable
	echo -n ">";
	read install_type;
	
	# this is called when exit command issued
	if [ $install_type = "3" ]
	then
		exit
	fi

	# this is called wether install or remove command issued, the program continues to run
	if [ "$install_type" = "1" ] || [ "$install_type" = "2" ]
	then
		break
	fi
done


# checks if installing
if [ $install_type = "1" ]
then	

	# checks if binary exists, if so then tell user if they want to delete extra files
	if [ -e /usr/bin/weatherTUI ]
	then
		# will run a loop untill the user selects the one of the options
                while true
			do

        		# reads user input
			echo -n "weatherTUI already exists, would you like to delete it? [Y/N]";
        		read is_delete;
        	
			if [ "$is_delete" = "Y" ] || [ "$is_delete" = "y" ]
        		then
               			remove_weather_cli
				break
        		fi
			if [ "$is_delete" = "N" ] || [ "$is_delete" = "n" ]
			then
				break
			fi
		done
	fi

	# calls function to install the weather command
	install_weather
fi

# checks if removing
if [ $install_type = "2" ] 
then

	# checks if prevous configuration files exist in file system 
	if [ -e /etc/weatherTUI ]
	then

		# will loop untill user selects valid responce
		while true
		do

			# reads user input
        		echo -n "Would you like to delete the configuration files(will delete all stored data)? [Y/N]";
			read is_purge;
			if [ "$is_purge" = "Y" ] || [ "$is_purge" = "y" ] 
			then 
				remove_all
				break
			else
				remove_weather_cli
				break
			fi
		done
	else
		# if not other files detected, then just delete the cli
		remove_weather_cli
	fi
fi

echo "Script Completed";




