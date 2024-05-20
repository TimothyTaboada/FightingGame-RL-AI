# FightingGame-RL-AI
by "Team" NYHaruka  
Members:  
Timothy Janssen B. Taboada, CIT-U BSCS
## How can I run this?
### Requirements:
1. Python
2. Docker
3. [DIAMBRA Account](https://diambra.ai/)
4. [Link to DIAMBRA repository just in case](https://github.com/diambra)
### Running the thing:
#### Initializing (for fresh download/clone):
1. `pip install requirements.txt`
2. Download the model [here](https://drive.google.com/file/d/1igtZyrMhgBdwCauXGNLSPSnVUT3oMgTO/view?usp=sharing) (or train one yourself, if you want to start from scratch)
#### Training & Testing
1. Launch Docker
2. Run `diambra run -r "your directory to DIAMBRA roms folder" python test.py` (sample is in auto-train.bat)
3. Run ./auto-train.bat if you want to train with periodic stops, or just modify `total_timesteps` in `test.py` if you want one session to train for a longer period of time (30000 steps = ~60 mins, may vary due to hardware capabilities)
# [Link to Research Paper](https://www.overleaf.com/read/qtqxtmcsdzns#a284f3)
## What is this project?
I tried out DIAMBRA Arena and decided to use it to train an AI to play Q from Street Fighter III - Third Strike, mostly on a whim. I watched a somewhat outdated YouTube video on how to do it with OpenAIGym, and wanted to see how a different machine learning AI training platform would perform.
