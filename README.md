# Auto_pronote_openning
This script connects to your personnal pronote page thanks to python3 's selenium module

First in order to connect you automaticly you need store your credentials (user=prenom.nom, password).
It is safer to store an hashed password, that's why the script create_sha256_hashed_password.py provides you your hashed password.
You must modify in the main.py script the line 5 to put your credentials and the programm will use those 
credentials to authentificate you.

Once the main.py script is built or configured.
When you lauch it, it will ask your unhashed password and if it's the right password it  will authentificates you on https://ent.iledefrance.fr/login/ and 
then it will open your personal pronote page in a new tab.

Feel free to share any improvements.   
