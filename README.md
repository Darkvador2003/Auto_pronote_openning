# Auto_pronote_openning
This script connects to your personnal pronote page thanks to python3 's selenium module

First in order to connect you automaticly you need store your credentials (user=prenom.nom, password).
It is safer to store an hashed password, that's why the script create_sha126_hashed_password.py provides you your hashed password.
Once you have your hash you can lauch the build.py script, this script will ask you your credentials in order to build the script especially for your 
credentials.
However if you don't want to build the script you can modify in the main.py script the line 5 to put your credentials and the programm will use those 
credentials to authentificate you.

Once the main.py script is built or configured it will authentificates you on https://ent.iledefrance.fr/login/ and then it will open your personal pronote
page in a new tab.

Feel free to share any improvements.   
