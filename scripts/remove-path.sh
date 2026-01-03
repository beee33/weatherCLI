


if [ -e ~/.zshrc ]
then
	check_is_added=$(grep "export PATH=\$PATH:~/.local/bin/weather-machine" ~/.zshrc)
	if [ "$check_is_added"  != "" ]
	then
		
		script_val=$( grep -v "export PATH=\$PATH:~/.local/bin/weather-machine" ~/.zshrc | cat )
	       	echo "$script_val" > ~/.zshrc
		echo "removed ~/.zshrc path";
	fi


fi


if [ -e ~/.bashrc ]
then
	check_is_added=$(grep "export PATH=\$PATH:~/.local/bin/weather-machine" ~/.bashrc)
	if [ "$check_is_added"  != "" ]
	then
	
                script_val=$( grep -v "export PATH=\$PATH:~/.local/bin/weather-machine" ~/.bashrc | cat )
                echo "$script_val" > ~/.bashrc
		echo "removed ~/.bashrc path";
	fi
fi



