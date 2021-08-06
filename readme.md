# Camel Up Monte Carlo Simulations

Ever wondered whether the board game *Camel Up* is every bit as random as it feels? Well now you can spice up your board game nights and amaze your friends with insights into the game!

## Features
- Calculate the probability for a particular camel to win the leg, win the race or finish last for any game state.
- Simulate an entire race with these same probabilities displayed for every camel moved.
- Beautfil displays of the state of the race.
- Plot win chance vs turn for each camel.
- Amaze your friends!

## Installation using Anaconda
1. Clone repository
2. From the base directory, create evironment `conda env create -f environment.yml`
3. Activate environment `conda activate camelup`

### On each login
`conda activate camelup`

## Basic usage
1. Run race_baseline.py in your favourite IDE
2. Profit

## Slightly more advanced usage
Save plots by opening constants.py and setting `PLOT_METHOD = 1`

Running race_baseline.py will now save the plots

## Even more advanced usage
Use compiled C++ modules for extra performance. This currently only works in linux environments.

Requires boost C++ libraries to be installed.
1. Compile the library with `make`
2. In constants.py set `USE_CPP_CLASSES = True`
3. Use is the same before, e.g. `python race_baseline.py` will do the same as previously but quicker

#### Disclaimer
By using this code, you agree that if the game is ruined for you it's your own fault.