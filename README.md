# gitNotify
Simple python app that allows github repository notifications in your desktop  
With this app you can follow commit branches.  

## Supports
- One repository per app  
- Multiple branches from the repository  
- Thread support  
- Notifications by pynotify and windows 10 toast

## Dependencies

To use this app you need :  
- Python 2.7 
- pynotify  (Linux)
- urllib2  
- xml.etree.ElementTree as ET  
- windows 10 toast ( https://github.com/jithurjacob/Windows-10-Toast-Notifications )
- easyGUI
  
## Instalation/how to

- Clone the project  
- Get the URL from the repository you want to follow(browser URL)  
- Get the branches names you want to follow as well   
- python run.py

Example(without user interface):  python gitTify.py https://github.com/pedrooct/gitNotify master (other branches can be added) !  

## Next update
- Optimization of CPU usage!  done!
- Grafical Interface ! small user interface... NEEDS to be updated
- More branches in the future !
- create full app

Developed by : Pedrooct  
