## GUI



### Installing Qt:  

    $ sudo apt-get update  
    $ sudo apt-get install build-essential  
    $ sudo apt-get install qtcreator  
    $ sudo apt install qt5-default  



### Running Qt (From project directory):
#### Initial Setup: 
    $ qmake -project  
open `GUI.pro` in a text editor and add `QT += gui widgets` at line 8 right under `INCLUDEPATH +=`  

    $ qmake GUI.pro
 
 #### Running: 
    $ make
    $ ./GUI
  


### GUI current look:
![GUI](https://i.imgur.com/acMqOJO.png)
