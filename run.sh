# Start a detached screen session
# Before you can run this file, please execute this command: chmod +x run.sh
# Substitue <accountName> with the name of your account specified in the config file

screen -S Appx_LiveAccount_10220915_TMlive10_15K_Slave_Account -d -m python3 main.py run-ddr --account Appx_LiveAccount_10220915_TMlive10_15K_Slave_Account 

# To connect to any individual screen session, use: screen -r <screenName>
# To disconnect from a screen session, use: Ctrl+A, D
# To list all screen sessions, use: screen -ls
# To kill a screen session, use: screen -X -S <screenName> quit
# To kill all screens at once use: pkill screen