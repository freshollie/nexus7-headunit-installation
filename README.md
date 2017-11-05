# Nexus 7 2013 Headunit Builder

This repository contains a script to automatically patch my nexus 7 tablet to be a headunit

## Requirements

- Linux
- Python
- adb and fastboot in system path
- pip3

## Instructions

1. `sudo pip3 install gplaycli` 
2. `./fetch_requirements.sh`
3. Ensure tablet is connected
4. `python build_headunit.py`
5. Follow instructions
