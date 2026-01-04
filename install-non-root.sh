#!/bin/bash


remove_weathercli() {

	rm -rf ~/.local/bin/weather-machine/

	chmod +x scripts/remove-path.sh  
	sh scripts/remove-path.sh

	echo "removed weathercli";
}
remove_weathercli_files() {
	rm -rf  ~/.config/weatherCLI/
	echo "removed files";
}

remove_all() {

	# checks if data directory already exists
	if [ -e ~/.config/weatherCLI ]
	then
		# will loop untill user selects valid responce
		while true
		do

			# reads user input
			echo -n "Would you like to delete the configuration files(will delete all stored data)? [Y/N]";
			read is_purge;
			if [ "$is_purge" = "Y" ] || [ "$is_purge" = "y" ]
			then
				remove_weathercli_files
				remove_weathercli
				break
			else
				remove_weathercli
				break
			fi
		done

	else
		remove_weathercli_files
		remove_weathercli
	fi
}
add_to_path() {


	# will loop untill user selects valid responce
	while true
	do

	# reads user input
	
	echo "Would you like to add this program to your $PATH, this allows you to type in weatherCLI instead of typing ~/.local/bin/weatherCLI. Default Yes.";

	echo -n "Add to path? [Y/N]";
	read is_purge;
	if [ "$is_purge" = "Y" ] || [ "$is_purge" = "y" ]
	then
		break
	else
		break
	fi
	done


}


install_binary() {

	if [ ! -e ~/.local ] 
	then
		mkdir ~/.local
		echo "made ~/.local";	
	fi

	if [ ! -e ~/.local/bin/ ] 
	then
		mkdir ~/.local/bin/

		echo "made binary folder";
	else
		echo "binary folder already exists";
	fi


	if [ $install_type = "1" ] 
	then 

		install_conf		
		
	        mkdir ~/.local/bin/weather-machine

		install_folder=$(mktemp -d)


		echo $install_folder;
		cd $install_folder;

		
		download_link=$(curl -s https://api.github.com/repos/beee33/weatherCLI/releases/latest | grep "browser_download_url" | cut -d '"' -f 4)
		echo $download_link;
		curl -L $download_link -o weatherCLI

		mv weatherCLI ~/.local/bin/weather-machine/weatherCLI

		chmod +x  ~/.local/bin/weather-machine/weatherCLI


	fi
	
	weather_folder=$(mktemp -d)

	cd $weather_folder

	echo $weather_folder;
	
	git clone https://github.com/beee33/weatherCLI

	cd weatherCLI

	$temp_folder=$(pwd)

	if [ $install_type = "2" ] 
	then 
		chmod +x scripts/compile-bin.sh
		sh scripts/compile-bin.sh
		
	fi

	cd $temp_folder

	chmod +x scripts/add-path.sh 
	sh scripts/add-path.sh

	cd $orignal_location
}

install_conf() {
	if [ ! -e ~/.config ] 
	then
		mkdir ~/.config
		echo "made ~/.config";	
	fi
	
	if [ ! -e ~/.config/weatherCLI ] 
	then
		mkdir ~/.config/weatherCLI
		chmod -R 711 ~/.config/weatherCLI
		echo "made config folder";
	fi
	
}

install_weather() {
	install_conf
	install_binary
	#echo "installed weather";
}
good_install() {
	echo "";
	echo "";
	echo "weatherCLI installed at ~/.local/bin/weather-machine/weatherCLI :3";
	echo "Reload your terminal to have the changes fully applied!";

}
while true
do
        echo "weatherCLI installer";
	echo " 1) install weatherCLI binary (Recommended)";
	echo " 2) install weatherCLI by compiling it yourself";
        echo " 3) remove weatherCLI";
        echo " 4) exit";

        # prints out a command prompt that reads to the install_type variable
        echo -n ">";
        read install_type;
	echo "";
        # this is called when exit command issued
        if [ $install_type = "4" ]
        then
                exit
        fi

        # this is called wether install or remove command issued, the program continues to run
        if [ "$install_type" = "1" ] || [ "$install_type" = "2" ] || [ "$install_type" = "3" ]
        then
                break
        fi
done


orignal_location=$(pwd)


if [ $install_type = "1" ] ||  [ $install_type = "2" ]
then
	if [ -e ~/.local/bin/weather-machine/ ]
	then
		# will run a loop untill the user selects the one of the options
		while true
		do

			# reads user input
			echo -n "weatherCLI already exists, would you like to delete it? [Y/N]";
			read is_delete;
			echo "";

			if [ "$is_delete" = "Y" ] || [ "$is_delete" = "y" ]
			then
				remove_all
				install_weather 
				good_install
				break
			fi
			if [ "$is_delete" = "N" ] || [ "$is_delete" = "n" ]
			then
				break
			fi
		done
	else 
		install_weather
		good_install
	fi
fi


if [ $install_type = "3" ] 
then

	if [ ! -e ~/.local/bin/weather-machine ]
	then 
		if [ -e ~/.config/weatherCLI ]
		then
			# will loop untill user selects valid responce
			while true
			do

				# reads user input
				echo -n "weatherCLI is not installed, however its configuration files still exit do you want to delete it? (will delete all stored data)? [Y/N]";
				read is_purge;
				if [ "$is_purge" = "Y" ] || [ "$is_purge" = "y" ]
				then
					remove_weathercli_files
					break
				else
					echo "Nothing removed. Aborting.";
					exit
				fi
			done
		else
			echo "weatherCLI is not installed. Aborting.";
			exit;
		fi

	else 
		if [ -e ~/.config/weatherCLI ]
                then
			remove_all
		else
			remove_weathercli 
		fi
	fi

fi



