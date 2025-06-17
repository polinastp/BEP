Weather Simulation with Markov Chains and Monte Carlo Methods
A comprehensive statistical approach for generating synthetic weather time series with user-defined constraints using Markov chains and Monte Carlo simulations. This project is designed for energy system stress testing under various extreme weather conditions.
📋 Project Overview
This research project investigates how statistical models can generate realistic multivariate weather time series while incorporating user-defined constraints. The approach uses Markov chains trained on 15 years of historical weather data from Eindhoven, Netherlands, to create controllable weather sequences for testing renewable energy systems.
Key Features

Markov Chain Weather Modeling: Statistical weather simulation based on transition probabilities
Constrained Generation: Three types of constraints for specific weather scenario modeling
Monte Carlo Validation: 1000+ iteration validation with 100% constraint satisfaction rates
Energy System Applications: Targeted scenarios for renewable energy stress testing
Real-time Generation: Computationally efficient for rapid scenario creation

🏗️ Project Structure
├── data/                          # Weather data and processed datasets
├── figs/                          # Generated visualizations and plots
├── eda.ipynb                      # Exploratory Data Analysis notebook
├── 1dayMC.ipynb                   # One-day constraint implementation
├── k-dayMC copy.ipynb            # K-day constraint (backup)
├── k-dayMC-1h.ipynb              # K-day constraint (1-hour version)
├── k-dayMC-heatwave.ipynb        # Heatwave scenario simulation
├── k-dayMC-rain-spring.ipynb     # Rainy spring scenario
├── k-dayMC-solar-drought.ipynb   # Solar drought scenario
├── k-dayMC.ipynb                 # Main k-day constraint notebook
├── no-dayMC.ipynb                # No-day constraint implementation
└── README.md                     # This file

🎯 Constraint Types
1. One-Day Constraint
Ensures that generated weather sequences contain at least one occurrence of a specified weather state.
Use Case: Guaranteeing minimum exposure to specific conditions

Example: At least one day with high temperature and low precipitation

2. No-Day Constraint
Completely excludes unwanted weather states from generated sequences.
Use Case: Testing systems under prolonged absence of certain conditions

Example: Extended periods without sunny weather (solar drought simulation)

3. K-Day Constraint
Generates sequences with exactly k consecutive days of a target weather state.
Use Case: Modeling extreme weather events

Example: 14-day heatwaves, 10-day solar droughts, 15-day rainy periods

🌡️ Weather State Definition
Weather states are defined using temperature and precipitation categories:

Temperature: Low, Medium, High (based on 33rd and 66th percentiles)
Precipitation: Low, Medium, High (based on 33rd and 66th percentiles)

Combined States:

Low-Low, Low-Medium, Low-High
Medium-Low, Medium-Medium, Medium-High
High-Low, High-Medium, High-High

📊 Key Notebooks
eda.ipynb - Exploratory Data Analysis

Historical weather data preprocessing
State categorization and transition matrix creation
Baseline Markov chain model validation
Statistical analysis of weather patterns

1dayMC.ipynb - One-Day Constraint

Implementation of minimum occurrence constraints
Monte Carlo validation of constraint satisfaction
Comparison with unconstrained simulations

no-dayMC.ipynb - No-Day Constraint

Weather state exclusion methodology
Transition matrix probability redistribution
Analysis of constraint effects on weather distributions

k-dayMC.ipynb - K-Day Constraint

Consecutive day constraint implementation
Matrix boosting techniques for constraint enforcement
Validation of exact k-day sequences

Scenario-Specific Notebooks

k-dayMC-heatwave.ipynb: 14-day summer heatwave simulation (High-Low states)
k-dayMC-solar-drought.ipynb: 10-day winter solar drought (Medium-High states)
k-dayMC-rain-spring.ipynb: 15-day rainy spring conditions

🚀 Getting Started
Prerequisites
pythonimport pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from scipy.stats import chisquare
Basic Usage

Load and explore the data:
python# Start with eda.ipynb for data understanding
# This creates transition matrices and baseline models

Apply constraints:
python# Use specific constraint notebooks based on your needs
# Each notebook includes Monte Carlo validation

Generate scenarios:
python# Use scenario notebooks for energy system testing
# Includes visualization and continuous value mapping
