#!/bin/bash

# Disable GUI to free up more RAM
# sudo systemctl set-default multi-user

# Keep GUI Enabled for testing
sudo systemctl set-default graphical.target

# Disable ZRAM
sudo systemctl disable nvzramconfig.service

# Default to Max-N power mode
sudo nvpmodel -m 0

