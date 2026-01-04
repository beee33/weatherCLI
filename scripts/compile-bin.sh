

#install_folder=$(mktemp -d)


#echo $install_folder;
#cd $install_folder;


# will loop untill user selects valid responce
while true
do


	# reads user input
	echo "";
	echo "";

	echo "What version do you want to compile?";
	echo "1) compile from latest stable version source (Recommended)";
	echo "2) compile directly from github source";
	echo -n ">";
	read is_version;
	echo "";
	if [ "$is_version" = "1" ] || [ "$is_version" = "2" ]
	then
		break
	fi
	
done


check_command_git_install=$(command -v git)
check_command_python3_install=$(command -v python3) 

if [ -n "$check_command_git_install" ] 
then
	if [ -n "$check_command_python3_install" ] 
	then
		
		if [ $is_version = "2" ]
		then
			#echo "cloning weatherCLI";
			#git clone https://github.com/beee33/weatherCLI
	
			#cd weatherCLI
		#else
			echo "cloning latest version:";
			download_link=$(curl -s https://api.github.com/repos/beee33/weatherCLI/releases/latest | grep "tarball_url" | cut -d '"' -f 4)
			echo $download_link;
			curl -L $download_link -o latest.tar.gz

			tar -xf latest.tar.gz

			file_to_goto=$(ls | grep weatherCLI)
			cd $file_to_goto

		fi

		echo "creating virtual environment";
		python3 -m venv venv

		echo "entering virtual environment";
		source venv/bin/activate

		echo "installing dependencys";
		python3 -m pip install -r requirements.txt

		echo "installing pyinstaller"
		python3 -m pip install pyinstaller

		echo "compiling";
		pyinstaller main.py --onefile

		mv dist/main weatherCLI

		mkdir ~/.local/bin/weather-machine/
		cp weatherCLI ~/.local/bin/weather-machine/weatherCLI
		chmod +x ~/.local/bin/weather-machine/weatherCLI

		

	else
		echo "python3 not installed. Exiting.";
		exit
	fi

else
	echo "git not installed. Exiting.";
	exit
fi

