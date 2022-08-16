# NieR Automata Weapon Conversion Tool

Make a weapon model replace any weapon in game!


## Stuff you need to be able to use the tool:
- Python 3
- A weapon mod
- literally anything that can edit a text file

## how to use the thing:
1. Replace the weapon IDs in config.ini with the weapon you would like the mod to replace. (Don't forget to save the .ini file.) (Default is Virtuous weapons)
![The lines you need to edit in config.ini](/assets/weaponsintheconfigfile.png)
3. Drag the folder containing your modded weapons onto NAWCT.py
    1. The tool works recursively, if the dat/dtt is anywhere inside the folder you dragged, it will convert it.
4.The converted files will exported next to the original dtt/dat files.

## FAQ but just the answers
- You cannot convert between categories. 
    1. (eg. Spear to Spear works, Spear to Sword doesn't work)
- Make sure the folder you're dragging onto the NAWCT.py is A FOLDER, not a zip or anything else 
- Make sure the default app to open a .py file is actually Python

## haha
Let me know if this readme file needs more information.

##### Massive thanks to Woeful_Wolf, without him this wouldn't be possible.
