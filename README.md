# Flipper Animation Manifest Helper
This is a small python script that can be used to quickly make `manifest.txt` files, for the different Flipper Animation folders that are out there. A quick overview on how to use this:


## How To Use
1. Find animations to be added to the Flipper Zero. Here is a link where there are a good collection of different creators who make custom animations, check them out: https://github.com/RogueMaster/awesome-flipperzero-withModules/tree/rogue_main/dolphin-all

2. Gather folders of the different custom animations you would want to load in the flipper. Recommend placing this in it's own directory. With all of the custom animation folders in their own directory, we can now move the `manifest_help.py` to the same directory:
![Alt text](/gifs/save2folder.gif)

3. We can now run the `manifest_help.py` that is saved in the same directory. You can run this in any way you would normally execute a ptyhon script. In this example I have python loaded in windows and I can execute it with the `python` command (but another method could also be using wsl or any linux environment with python):
![Alt text](/gifs/pythonexecute_censor.gif)

4. We should now see the `manifest.txt` file was created with all of the custom animations mentioned within this file. We can now delete the `manifest_help.py` file and copy over the rest of the directory to the flipper zero. We can do this using the qflipper program, navigating to /sd card/dolphin folder, and pasting all of the custom animation folders with the `manifest.txt` file: 
![Alt text](/gifs/save2flipper.gif)

5. Enjoy! I originally created this since there are so many good custom animations out there that I would like to use many but did not want to manually change the `manifest.txt` file everytime. This tool is made for dealing with a bulk of files, and less of updating files one at a time.