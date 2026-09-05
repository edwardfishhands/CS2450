###############################################

Date 8/30/2026 | Subject: SSH Keys

Finally figured out why my remote repo wouldn't let me push.  I was confused because the instructions for creating an ssh key were for wsl-- I created my cs2450 directory in cmd, not wsl. My key was stuck in wsl and wasn't talking to my repo. I was able to fix it by making a new ssh key in cmd, and I was finally able to submit my assignments for this week.


###############################################

Date 9/5/2026 | Subject: Making files in CMD

I found out that I'm not able to use touch in cmd, its a command specifically for wsl. Instead of making files the long way-- using file explorer-- I decided to look up an alternative. I learned that you can use "type nul > filename" instead of touch to make files-- which helped me out with the flask assignment!

###############################################