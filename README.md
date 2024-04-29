# FightingGame-RL-AI
by "Team" NYHaruka  
Members:  
Taboada, Timothy Janssen B.
## How can I run this?
### Requirements:
1. Python
2. Docker
3. [Link to DIAMBRA repository just in case](https://github.com/diambra)
### Running the thing:
0. (For fresh download/clone) `pip install requirements.txt`
1. Run Docker
2. Download the model [here](https://drive.google.com/file/d/1igtZyrMhgBdwCauXGNLSPSnVUT3oMgTO/view?usp=sharing) (or train one yourself, if you wanna start from scratch)
3. Run `diambra run -r "your directory to DIAMBRA roms folder" python test.py` (sample is in auto-train.bat)
4. Run ./auto-train.bat if you want to train with periodic stops, or just modify `total_timesteps` if you want one session to train for a longer period of time (30000 steps = ~60 mins, may vary due to hardware capabilities)
# [Link to Research Paper](https://www.overleaf.com/read/qtqxtmcsdzns#a284f3)
## What is this project?
I tried out DIAMBRA Arena and decided to use it to train an AI to play Q from Street Fighter III - Third Strike, mostly on a whim. I watched a somewhat outdated YouTube video on how to do it with OpenAIGym, and wanted to see how a different machine learning AI training platform would perform and somehow managed to pass it off as my thesis project.