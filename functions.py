#!/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import random
import time
from numpy.random import normal
import numpy as np
from sklearn.linear_model import LinearRegression
import math
import sys

# run a specific amount of trials with type, number of trials, binsize, rfrac, rweld, events
# this funciton runs thhe model, choosing imputs for the variables

def main(init_type, trial_amount, binsize, rfrac, rweld, events):
    init_type = int(init_type)
    trial_amount = int(trial_amount)
    binsize = int(binsize)
    rfrac = float(rfrac)
    rweld = float(rweld)
    events = int(events)
    averages = {}
    floe_averages = {}
    total = {}
    for i in range(trial_amount):
        if init_type == 1:
        # calls fsd function to get a dict for that init_type
        # starts with one big flow
            result = one_big(events, rfrac, rweld)
            fsd = result[0]
            floe_times = result[1]
            for value in fsd:
                if value in averages:
                    averages[value].append(fsd[value])
                else:
                    averages[value] = []
                    averages[value].append(fsd[value])
                    
            for value in floe_times:
                if value in floe_averages:
                    floe_averages[value].append(floe_times[value])
                else:
                    floe_averages[value] = []
                    floe_averages[value].append(floe_times[value])
        
        elif init_type == 2:
        # calls fsd function to get a dict for that init_type
        # starts with a large normal distribution
            result = big_normal(events, rfrac, rweld)
            fsd = result[0]
            floe_times = result[1]
            for value in fsd:
                if value in averages:
                    averages[value].append(fsd[value])
                else:
                    averages[value] = []
                    averages[value].append(fsd[value])
            
            for value in floe_times:
                if value in floe_averages:
                    floe_averages[value].append(floe_times[value])
                else:
                    floe_averages[value] = []
                    floe_averages[value].append(floe_times[value])
                    
        elif init_type == 3:
        # calls fsd function to get a dict for that init_type
        # starts with a small normal distribution
            result = small_normal(events, rfrac, rweld)
            fsd = result[0]
            floe_times = result[1]
            
            for value in fsd:
                if value in averages:
                    averages[value].append(fsd[value])
                else:
                    averages[value] = []
                    averages[value].append(fsd[value])
                    
            for value in floe_times:
                if value in floe_averages:
                    floe_averages[value].append(floe_times[value])
                else:
                    floe_averages[value] = []
                    floe_averages[value].append(floe_times[value])
                    
        elif init_type == 4:
        # calls fsd function to get a dict for that init_type
        # starts with one large floe, but breaks into 2 instead of 4
            result = one_big2(events, rfrac, rweld)
            fsd = result[0]
            floe_times = result[1]
            
            for value in fsd:
                if value in averages:
                    averages[value].append(fsd[value])
                else:
                    averages[value] = []
                    averages[value].append(fsd[value])
                    
            for value in floe_times:
                if value in floe_averages:
                    floe_averages[value].append(floe_times[value])
                else:
                    floe_averages[value] = []
                    floe_averages[value].append(floe_times[value])
                    
        elif init_type == 5:
        # calls fsd function to get a dict for that init_type
        # starts with one large floe, but uses area instead of radius
            result = one_big_area(events, rfrac, rweld)
            fsd = result[0]
            floe_times = result[1]
            
            for value in fsd:
                if value in averages:
                    averages[value].append(fsd[value])
                else:
                    averages[value] = []
                    averages[value].append(fsd[value])
                    
            for value in floe_times:
                if value in floe_averages:
                    floe_averages[value].append(floe_times[value])
                else:
                    floe_averages[value] = []
                    floe_averages[value].append(floe_times[value])
                    
        elif init_type == 6:
        # calls fsd function to get a dict for that init_type
        # starts with a power law
            result = power_law(events, rfrac, rweld)
            fsd = result[0]
            floe_times = result[1]
            
            for value in fsd:
                if value in averages:
                    averages[value].append(fsd[value])
                else:
                    averages[value] = []
                    averages[value].append(fsd[value])
                    
            for value in floe_times:
                if value in floe_averages:
                    floe_averages[value].append(floe_times[value])
                else:
                    floe_averages[value] = []
                    floe_averages[value].append(floe_times[value])
    
    # this portion computes the average values for the trial_amount value 
    for value in averages:
        total = 0
        for number in averages[value]:
            total += number
        if total/trial_amount >= 1:
            averages[value] = (total/trial_amount)
        elif total/trial_amount >=.5 and total/trial_amount < 1:
            averages[value] = 1
        else:
            averages[value] = 0
            
    for value in floe_averages:
        total = 0
        for number in floe_averages[value]:
            total += number
        if total/trial_amount >= 1:
            floe_averages[value] = (total/trial_amount)
        elif total/trial_amount >=.5 and total/trial_amount < 1:
            floe_averages[value] = 1
        else:
            floe_averages[value] = 0     
    
    # binning the trials with binning function
    bin_dict = log_binning(averages, binsize)
    #bin_dict = binning(averages, binsize)
    ratio = rfrac/rweld
    graphing(bin_dict, ratio, init_type)
    floes_at_time(floe_averages, ratio, init_type)
    return print(bin_dict, floe_averages)

# bin the dictionary based 
def log_binning(dictionary, binsize):
    binned = {}
    bins = {}
    sizes = []
    for i in range(5000):
        if i != 0:
            sizes.append((binsize)**i)
    for size in sizes:
        binned[size] = 0
        
    for value in dictionary:
        if value > 0:   #change to 40, any val, allows for small floe condition
            floe_count = dictionary[value]
            if (type(floe_count)) == list:
                floe_count = floe_count[0]
            opt_out = 0
            for size in sizes:
                if opt_out == 1:
                    continue
                elif value < size and value > 0:
                    binned[size] += floe_count
                    opt_out = 1
        for key in binned:
            if binned[key] > 0:
                bins[key] = binned[key]
        
    return bins

# takes in a dictionary and a bin size, then it sorts the dictionary and bins it
def binning(dictionary, binsize):
    binned = {}
    bins = {}
    sizes = []
    for i in range(5000):
        if i != 0:
            sizes.append(i*binsize)
    for size in sizes:
        binned[size] = 0
        
    for value in dictionary:
        if value > 0:   #change to 40, any val
            floe_count = dictionary[value]
            opt_out = 0
            for size in sizes:
                if opt_out == 1:
                    continue
                elif value < size and value > 0:
                    binned[size] += floe_count
                    opt_out = 1
        for key in binned:
            if binned[key] > 0:
                bins[key] = binned[key]
        
    return bins


# gets the coefficient for the graph
def log_coeff(sizes, counts):
    log_size = []
    log_count = []
    if counts[0] == 0.0:
        sizes = sizes[1:]
        counts = counts[1:]
    for val in sizes:
        size = math.log(val,10)
        log_size.append(size)

    for val in counts:
        count = math.log(val,10)
        log_count.append(count)
    
    m, b = np.polyfit(log_size, log_count, 1)
    #poly1d_fn = np.poly1d(coef) 
    return (m, b)

# graphs the plot from the bin dictionary, and labels with the ratio and the initial condition
def graphing(my_dict, ratio, type_init):
    dictionary = {}
    for key in my_dict:
        if key >= 0: # only graph greater than or equal to this value
            dictionary[key] = my_dict[key]
            
    myKeys = list(dictionary.keys())
    myKeys.sort()
    sorted_dict = {i: dictionary[i] for i in myKeys}
    sizes = list(sorted_dict.keys())
    counts = list(sorted_dict.values())
    total_count = sum(counts)
    fig = plt.figure()
    plt.scatter(sizes, counts)
    plt.plot(sizes, counts)
    plt.xlabel("Width (m)")
    plt.ylabel("Count")
    plt.yscale("log")
    plt.xscale("log")
    m, b = log_coeff(sizes, counts)    
    title_string = "FSD for " + str(ratio) + " " + "Type = " + str(type_init)
    subtitle_string = "Exponent Value: " + str(m)
    plt.suptitle(title_string, y=1.05, fontsize=18)
    plt.title(subtitle_string, fontsize=10)
    x = str(ratio).replace(".", "_")
    fname = str(x) + "_type_" + str(type_init)
    plt.savefig(fname + ".jpg")
    plt.close(fig)
    
# this functions creates a graph for tbe amount of floes over time, labeled with the ratio and the init type
def floes_at_time(dictionary, ratio, type_init):
    myKeys = list(dictionary.keys())
    myKeys.sort()
    sorted_dict = {i: dictionary[i] for i in myKeys}
    times = list(sorted_dict.keys())
    counts = list(sorted_dict.values())
    fig = plt.figure()
    plt.plot(times, counts)
    plt.xlabel("Time")
    plt.ylabel("Floes Present")
    title_string = "Floe count over Time" + str(ratio) + " Type = " + str(type_init)
    subtitle_string = "Ratio = " + str(ratio) + " Type=" + str(type_init)
    plt.suptitle(title_string, y=1.05, fontsize=18)
    plt.title(subtitle_string, fontsize=10)
    x = str(ratio).replace(".", "_")
    fname = str(x) + "_floe_count_type" + str(type_init)
    plt.savefig(fname + ".jpg")
    plt.close(fig)


    
# choose a random event to occur, 0 = nothing, 1 = fracture, 2 = weld
def random_event(num, rfrac, rweld):
    sampleList = [0, 1, 2]
    rnone = 1 - (rfrac + rweld)
    randomList = random.choices(
      sampleList, weights=(rnone, rfrac, rweld), k=num)
    return(randomList)

# pick  a random floe out of the available floes, chooses out of a list of the available floe sizes, 
# weighted by the amount of floes of that size
def pick_floe(fsd):
    randomPick = random.choices(
      list(fsd.keys()), weights=(list(fsd.values())), k=1)
    return randomPick[0]


# the funcitons below are the initial condition functions running all the different init types
def one_big(events, rfrac, rweld):  
    fsd_dict2 = {20000:1}
# this value is for the weld loop
    opt_out = 0
    # chooses the given input number of events to happen
    events = random_event(events, rfrac, rweld)
    time_events = {}
    count = 0
    
    # goes through the events one by one and decides to nothing/split/weld based on the value 0,1,2
    for val in events:
        count +=1
        # define all the possible sizes
        keys = list(fsd_dict2.keys())
        sizes =[]
        time_events[count] = sum(fsd_dict2.values())
        for key in keys:
            if fsd_dict2[key] > 0:
                sizes.append(key)
        
        if val == 0:
            continue
        elif val == 1:   # Fracture occurs
            # choose a place to break 
            # Randomly chose a place to have a fracture
            # and Randomly choose how many it will break in to (4, 16?)

            choice = float(pick_floe(fsd_dict2))
            # small floe condition of 5 (10/2)
            if choice >= 10:
                new_size = choice/2
                
        # remove 1 from the bigger value and add 4 to the broken value
                fsd_dict2[choice] -= 1
            
                if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 4
                else:
                    fsd_dict2[new_size] = 4
            else:
                continue
                

        elif val == 2:   # Weld occurs
            # choose a place to weld
            choice = float(pick_floe(fsd_dict2))
            
            if fsd_dict2[choice] >= 4:
                new_size = choice*2
                fsd_dict2[choice] -= 4
                
                if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 1
                else:
                    fsd_dict2[new_size] = 1
            
            # if there are not 4 available floes to weld, we skip
            elif fsd_dict2[choice] < 4:
                continue
#                 # check and see how many there are in our choice
#                 choice_total = fsd_dict2[choice]
            
#                 # see how many floes we need
#                 needed_floes = (4 - choice_total)
            
#                 for i in range(1000):
#                     if opt_out == 1:
#                         continue
                
#                 # check if a sligtly larger floe is available to weld 
#                     elif (choice + i) in fsd_dict2 and fsd_dict2[(choice + i)] > 0:
#                         if fsd_dict2[choice + i] >= needed_floes:
#                             fsd_dict2[choice + i] -= needed_floes
#                             fsd_dict2[choice] = 0
#                             opt_out = 1
                    
#                     # change the vals in the dictionary
#                             if needed_floes == 3:
#                                 new_size = (choice + i)*2
#                                 if new_size in fsd_dict2:
#                                     fsd_dict2[new_size] += 1

#                                 else:
#                                     fsd_dict2[new_size] = 1
#                             else: 
#                                 new_size = (choice + i) + choice
#                                 if new_size in fsd_dict2:
#                                     fsd_dict2[new_size] += 1

#                                 else:
#                                     fsd_dict2[new_size] = 1
    return fsd_dict2, time_events


# normal distribution of mean = 3400, sd = 900, n = 1000
def big_normal(events, rfrac, rweld):
    fsd_dict2 = {}
    data = normal(loc=3400, scale=900, size=1000)
    fsd = data.tolist()
    time_events = {}
    count = 0
    for item in fsd:
        if item not in fsd_dict2:
            fsd_dict2[item] = 1
        else:
            fsd_dict2[item] += 1
            
# this value is for the weld loop
    opt_out = 0
    events = random_event(events, rfrac, rweld)
    for val in events:
        count += 1
        keys = list(fsd_dict2.keys())
        sizes =[]
        time_events[count] = sum(fsd_dict2.values())
        for key in keys:
            if fsd_dict2[key] > 0:
                sizes.append(key)
    
        if val == 0:
            continue
            
        elif val == 1:   # Fracture occurs
            choice = float(pick_floe(fsd_dict2))
            # small floe condition of 5 (10/2)
            if choice >= 10:
                new_size = choice/2
                fsd_dict2[choice] -= 1
                if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 4
                else:
                    fsd_dict2[new_size] = 4
                    
            else:
                continue
                

        elif val == 2:   # Weld occurs
            # choose a place to weld
            choice = float(pick_floe(fsd_dict2))
            
            if fsd_dict2[choice] >= 4:
                new_size = choice*2
                fsd_dict2[choice] -= 4
                
                if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 1
                else:
                    fsd_dict2[new_size] = 1
                

            elif fsd_dict2[choice] < 4:
                continue
#                 choice_total = fsd_dict2[choice]
#                 needed_floes = (4 - choice_total)
            
#                 for i in range(1000):
#                     if opt_out == 1:
#                         continue
                
#                 # check if a sligtly larger floe is available to weld 
#                     elif (choice + i) in fsd_dict2 and fsd_dict2[(choice + i)] > 0:
#                         if fsd_dict2[choice + i] >= needed_floes:
#                             fsd_dict2[choice + i] -= needed_floes
#                             fsd_dict2[choice] = 0
#                             opt_out = 1
                    
#                     # change the vals in the dictionary
#                             if needed_floes == 3:
#                                 new_size = (choice + i)*2
#                                 if new_size in fsd_dict2:
#                                     fsd_dict2[new_size] += 1

#                                 else:
#                                     fsd_dict2[new_size] = 1
#                             else: 
#                                 new_size = (choice + i) + choice
#                                 if new_size in fsd_dict2:
#                                     fsd_dict2[new_size] += 1

#                                 else:
#                                     fsd_dict2[new_size] = 1
    return fsd_dict2, time_events


# small normal distribution with mean = 1000, sd = 100, n = 500
def small_normal(events, rfrac, rweld):
    fsd_dict2 = {}
    data = normal(loc=1000, scale=100, size=500)
    fsd = data.tolist()
    time_events = {}
    count = 0
    
    for item in fsd:
        if item not in fsd_dict2:
            fsd_dict2[item] = 1
        else:
            fsd_dict2[item] += 1
        
# this value is for the weld loop
    opt_out = 0
    events = random_event(events, rfrac, rweld)
    for val in events:
        count += 1
        keys = list(fsd_dict2.keys())
        sizes =[]
        time_events[count] = sum(fsd_dict2.values())

        for key in keys:
            if fsd_dict2[key] > 0:
                sizes.append(key)
    
        if val == 0:
            continue
            
        elif val == 1:   # Fracture occurs
            choice = float(pick_floe(fsd_dict2))
            # small floe condition of 5 (10/2)
            if choice >= 10:
                new_size = choice/2
                fsd_dict2[choice] -= 1
                if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 4
                else:
                    fsd_dict2[new_size] = 4
                    
            else:
                continue
                

        elif val == 2:   # Weld occurs
            # choose a place to weld
            choice = float(pick_floe(fsd_dict2))
            
            if fsd_dict2[choice] >= 4:
                new_size = choice*2
                fsd_dict2[choice] -= 4
                
                if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 1
                else:
                    fsd_dict2[new_size] = 1
                    
            elif fsd_dict2[choice] < 4:
                continue
#                 choice_total = fsd_dict2[choice]
#                 needed_floes = (4 - choice_total)
            
#                 for i in range(1000):
#                     if opt_out == 1:
#                         continue
                
#                 # check if a sligtly larger floe is available to weld 
#                     elif (choice + i) in fsd_dict2 and fsd_dict2[(choice + i)] > 0:
#                         if fsd_dict2[choice + i] >= needed_floes:
#                             fsd_dict2[choice + i] -= needed_floes
#                             fsd_dict2[choice] = 0
#                             opt_out = 1
                    
#                     # change the vals in the dictionary
#                             if needed_floes == 3:
#                                 new_size = (choice + i)*2
#                                 if new_size in fsd_dict2:
#                                     fsd_dict2[new_size] += 1

#                                 else:
#                                     fsd_dict2[new_size] = 1
#                             else: 
#                                 new_size = (choice + i) + choice
#                                 if new_size in fsd_dict2:
#                                     fsd_dict2[new_size] += 1

#                                 else:
#                                     fsd_dict2[new_size] = 1
    return fsd_dict2, time_events


def one_big2(events, rfrac, rweld):  
    fsd_dict2 = {400000000:1}
# this value is for the weld loop
# this function defines area not width
    opt_out = 0
    events = random_event(events, rfrac, rweld)
    time_events = {}
    count = 0
    for val in events:
        # define all the possible sizes
        count+=1
        keys = list(fsd_dict2.keys())
        sizes =[]
        time_events[count] = sum(fsd_dict2.values())

        for key in keys:
            if fsd_dict2[key] > 0:
                sizes.append(key)
    
        if val == 0:
            continue
        elif val == 1:   # Fracture occurs
            # choose a place to break 
            # Randomly chose a place to have a fracture
            # and Randomly choose how many it will break in to (4, 16?)

            choice = float(pick_floe(fsd_dict2))
            # small floe condition of 25 (50/2)
            if choice >= 50:
                new_size = choice/2
                fsd_dict2[choice] -= 1
            
                if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 2
                else:
                    fsd_dict2[new_size] = 2
                    
            else:
                continue
                

        elif val == 2:   # Weld occurs
            # choose a place to weld
            choice = float(pick_floe(fsd_dict2))
            
            if fsd_dict2[choice] >= 2:
                new_size = choice*2
                fsd_dict2[choice] -= 2
                
                if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 1
                else:
                    fsd_dict2[new_size] = 1
            
            elif fsd_dict2[choice] < 2:
                continue
                # check and see how many there are in our choice
#                 choice_total = fsd_dict2[choice]
            
#                 # see how many floes we need
#                 needed_floes = (2 - choice_total)
            
#                 for i in range(1000):
#                     if opt_out == 1:
#                         continue
                
#                 # check if a sligtly larger floe is available to weld 
#                     elif (choice + i) in fsd_dict2 and fsd_dict2[(choice + i)] > 0:
#                         if fsd_dict2[choice + i] >= needed_floes:
#                             fsd_dict2[choice + i] -= needed_floes
#                             fsd_dict2[choice] = 0
#                             opt_out = 1
                    
#                     # change the vals in the dictionary
#                             if needed_floes == 3:
#                                 new_size = (choice + i)*2
#                                 if new_size in fsd_dict2:
#                                     fsd_dict2[new_size] += 1

#                                 else:
#                                     fsd_dict2[new_size] = 1
#                             else: 
#                                 new_size = (choice + i) + choice
#                                 if new_size in fsd_dict2:
#                                     fsd_dict2[new_size] += 1

#                                 else:
#                                     fsd_dict2[new_size] = 1
    return fsd_dict2, time_events

def one_big_area(events, rfrac, rweld):  
    fsd_dict2 = {400000000:1}
# this value is for the weld loop
    opt_out = 0
    events = random_event(events, rfrac, rweld)
    time_events = {}
    count = 0
    for val in events:
        # define all the possible sizes
        count+= 1
        keys = list(fsd_dict2.keys())
        sizes =[]
        time_events[count] = sum(fsd_dict2.values())

        for key in keys:
            if fsd_dict2[key] > 0:
                sizes.append(key)
    
        if val == 0:
            continue
        elif val == 1:   # Fracture occurs
            # choose a place to break 
            # Randomly chose a place to have a fracture
            # and Randomly choose how many it will break in to (4, 16?)

            choice = float(pick_floe(fsd_dict2))
            # small floe condition of 400 (800/2)
            if choice >= 50:
                new_size = choice/2
                
        # remove 1 from the bigger value and add 4 to the broken value
                fsd_dict2[choice] -= 1
            
                if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 4
                else:
                    fsd_dict2[new_size] = 4
            
            else:
                continue
                
        elif val == 2:   # Weld occurs
            # choose a place to weld
            choice = float(pick_floe(fsd_dict2))
           
            if fsd_dict2[choice] >= 4:
                new_size = choice*2
                fsd_dict2[choice] -= 4
                
                if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 1
                else:
                    fsd_dict2[new_size] = 1
            
            elif fsd_dict2[choice] < 4:
                continue
                # check and see how many there are in our choice
#                 choice_total = fsd_dict2[choice]
            
#                 # see how many floes we need
#                 needed_floes = (4 - choice_total)
            
#                 for i in range(1000):
#                     if opt_out == 1:
#                         continue
                
#                 # check if a sligtly larger floe is available to weld 
#                     elif (choice + i) in fsd_dict2 and fsd_dict2[(choice + i)] > 0:
#                         if fsd_dict2[choice + i] >= needed_floes:
#                             fsd_dict2[choice + i] -= needed_floes
#                             fsd_dict2[choice] = 0
#                             opt_out = 1
                    
#                     # change the vals in the dictionary
#                             if needed_floes == 3:
#                                 new_size = (choice + i)*2
#                                 if new_size in fsd_dict2:
#                                     fsd_dict2[new_size] += 1

#                                 else:
#                                     fsd_dict2[new_size] = 1
#                             else: 
#                                 new_size = (choice + i) + choice
#                                 if new_size in fsd_dict2:
#                                     fsd_dict2[new_size] += 1

#                                 else:
#                                     fsd_dict2[new_size] = 1
    return fsd_dict2, time_events

def power_law(events, rfrac, rweld):
    fsd_dict2 = {}
    for i in range(100): 
        if i != 0:
            fsd_dict2[i] = 10000 * (i **(-2))
    opt_out = 0
    events = random_event(events, rfrac, rweld)
    time_events = {}
    count = 0
    for val in events:
        count +=1
        # define all the possible sizes
        keys = list(fsd_dict2.keys())
        sizes =[]
        time_events[count] = sum(fsd_dict2.values())
        for key in keys:
            if fsd_dict2[key] > 0:
                sizes.append(key)
        
        if val == 0:
            continue
        elif val == 1:   # Fracture occurs
            # choose a place to break 
            # Randomly chose a place to have a fracture
            
            choice = float(pick_floe(fsd_dict2))
            # small floe condition of 5 (10/2)
            if choice >= 10:
                new_size = choice/2
            
        # remove 1 from the bigger value and add 4 to the broken value
                fsd_dict2[choice] -= 1
            
                if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 4
                else:
                    fsd_dict2[new_size] = 4
                    
            else:
                continue
         

        elif val == 2:   # Weld occurs
            # choose a place to weld
            choice = float(pick_floe(fsd_dict2))
            
            if fsd_dict2[choice] >= 4:
                new_size = choice*2
                fsd_dict2[choice] -= 4
                
                if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 1
                else:
                    fsd_dict2[new_size] = 1
            
            elif fsd_dict2[choice] < 4:
                continue
#                 # check and see how many there are in our choice
#                 choice_total = fsd_dict2[choice]
            
#                 # see how many floes we need
#                 needed_floes = (4 - choice_total)
            
#                 for i in range(1000):
#                     if opt_out == 1:
#                         continue
                
#                 # check if a sligtly larger floe is available to weld 
#                     elif (choice + i) in fsd_dict2 and fsd_dict2[(choice + i)] > 0:
#                         if fsd_dict2[choice + i] >= needed_floes:
#                             fsd_dict2[choice + i] -= needed_floes
#                             fsd_dict2[choice] = 0
#                             opt_out = 1
                    
#                     # change the vals in the dictionary
#                             if needed_floes == 3:
#                                 new_size = (choice + i)*2
#                                 if new_size in fsd_dict2:
#                                     fsd_dict2[new_size] += 1

#                                 else:
#                                     fsd_dict2[new_size] = 1
#                             else: 
#                                 new_size = (choice + i) + choice
#                                 if new_size in fsd_dict2:
#                                     fsd_dict2[new_size] += 1

#                                 else:
#                                     fsd_dict2[new_size] = 1
    return fsd_dict2, time_events

    

if __name__ == "__main__":
    main(init_type = sys.argv[1], 
         trial_amount = sys.argv[2], 
         binsize = sys.argv[3], 
         rfrac = sys.argv[4], 
         rweld = sys.argv[5], 
         events = sys.argv[6])
