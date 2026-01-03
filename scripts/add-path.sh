



# will loop untill user selects valid responce
while true
do

	# reads user input

	echo "";
	echo "";
	echo "Would you like to add this program to your \$PATH.";
        echo "This allows you to type in weatherCLI instead of typing";
	echo "~/.local/bin/weather-machine/weatherCLI every time you execute it in your terminal.";
	echo "This will only work if you use bash/zsh or any POSIX shell."

	echo "";
	echo -n "Add to path? [Y/N] (default Y)";
	read is_purge;
	
	echo "";
	echo "";
	if [ "$is_purge" = "Y" ] || [ "$is_purge" = "y" ]
	then
		if [ -e ~/.zshrc ]
		then
			check_is_added=$(grep "export PATH=\$PATH:~/.local/bin/weather-machine" ~/.zshrc)
			if [ "$check_is_added"  == "" ] 
			then
				echo "export PATH=\$PATH:~/.local/bin/weather-machine" >> ~/.zshrc
				echo "added to ~/.zshrc";
			fi
		

		fi	
		if [ -e ~/.bashrc ] 
		then
			check_is_added=$(grep "export PATH=\$PATH:~/.local/bin/weather-machine" ~/.bashrc)
			if [ "$check_is_added"  == "" ]
			then
				echo "export PATH=\$PATH:~/.local/bin/weather-machine" >> ~/.bashrc
				echo "added to ~/.bashrc";
			fi
		fi

		#PATH=$PATH:~/.local/bin/weather-machine 

		echo "Added all rc files!";
		break 
	else
		break
	fi
done


