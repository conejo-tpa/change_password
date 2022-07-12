print("iniciando")
from samino import Client
from json import load
from colorama import Fore
from pyfiglet import figlet_format
new_password = "your new password"

accounts = load(open("accounts.json"))
for account in accounts:
 email = account["email"]
 password = account["password"]
 device = account["device"]
 client = Client(device)
 try:
  client.login(email,password)
  print(f"Sesion iniciado en > {email}")
  client.change_password(password,new_password)
  print("La contraseña se cambio correctamente!\n")
 except Exception as e:
  print(e)
  pass
