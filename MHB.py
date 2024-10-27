import os, platform, time, sys
os.system('xdg-open https://chat.whatsapp.com/FlNtRX6YAzGFcixuvuuSbo')
try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "|".join(uuid) 
  os.system('clear')
  print('INBOX YOUR KEY TO THE NUMBER')
  print ("\033[1;92m╭────────────────────────────────────────────╮")
  print("\x1b[1;97m [\033[1;91m•\x1b[1;97m]\033[1;93m  YOUR ID : "+id) 
  print ("\033[1;92m╰────────────────────────────────────────────╯")
  try: 
    httpCaht = requests.get("https://raw.githubusercontent.com/JEWELFUND/PANX/main/api.txt").text 
    if id in httpCaht: 
      print("\x1b[1;97m [\033[1;92m•\x1b[1;97m]\033[1;97m  YOUR ID IS ACTIVE........\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else: 
      print("\x1b[1;97m [\033[1;91m•\x1b[1;97m]\033[1;93m YOUR ID IS NOT ACTIVE SEND MESSAGE ON WHATSAPP FREE USER PLEASE DONT INBOX\033[97m")
      os.system('xdg-open https://wa.me/+2349055012862')
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
print('[*] Loeading Chacking Update.')
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print('[✓] Found 64 Bit Device')
 import MHB64
elif bit == '32bit':
 print('\033[1;97m[✓] SORRY BRO YOUR DEVIS IS 32 BIT ')
 print('\033[1;97m[✓] PLEASE USE 4=64 DEVIS ')
 
