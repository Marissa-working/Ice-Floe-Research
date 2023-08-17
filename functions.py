import pandas as pd
import matplotlib.pyplot as plt
import random
import time
from numpy.random import normal
import numpy as np
from sklearn.linear_model import LinearRegression
import math

# bin the dictionary based 
def log_binning(dictionary, binsize):
    binned = {}
    bins = {}
    sizes = []
    for i in range(5000):
        if i != 0:
            sizes.append((binsize)**i)
            #sizes.append((i*binsize)**2)
    for size in sizes:
        binned[size] = 0
        
    for value in dictionary:
        if value > 0:   #change to 40, any val
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

def graphing(dictionary):
    myKeys = list(dictionary.keys())
    myKeys.sort()
    sorted_dict = {i: dictionary[i] for i in myKeys}
    sizes = list(sorted_dict.keys())
    counts = list(sorted_dict.values())
    total_count = sum(counts)
    plt.scatter(sizes, counts)
    plt.plot(sizes, counts)
    plt.xlabel("Width (m)")
    plt.ylabel("Count")
    plt.title("Model For FSD")
    plt.yscale("log")
    plt.xscale("log")
    m, b = log_coeff(sizes, counts)
    print("Exponent Value: ", m)
    print(sorted_dict)

def floes_at_time(dictionary):
    myKeys = list(dictionary.keys())
    myKeys.sort()
    sorted_dict = {i: dictionary[i] for i in myKeys}
    times = list(sorted_dict.keys())
    counts = list(sorted_dict.values())
    plt.plot(times, counts)
    plt.xlabel("Time")
    plt.ylabel("Floes Present")
    plt.title("Floes over Time")
    
# choose a random event to occur
def random_event(num, rfrac, rweld):
    sampleList = [0, 1, 2]
    rnone = 1 - (rfrac + rweld)
    randomList = random.choices(
      sampleList, weights=(rnone, rfrac, rweld), k=num)
    return(randomList)

# pick  a random floe out of the available floes
def pick_floe(fsd):
    randomPick = random.choices(
      list(fsd.keys()), weights=(list(fsd.values())), k=1)
    return randomPick[0]



# run a specific amount of trials with type, number of trials, binsize, rfrac, rweld, events
def fsd_trials(init_type, trial_amount, binsize, rfrac, rweld, events):
    averages = {}
    total = {}
    for i in range(trial_amount):
        if init_type == "one_big":
        # calls fsd function to get a dict for that init_type
            result = one_big(events, rfrac, rweld)
            fsd = result[0]
            for value in fsd:
                if value in averages:
                    averages[value].append(fsd[value])
                else:
                    averages[value] = []
                    averages[value].append(fsd[value])
        
        elif init_type == "big_normal":
        # calls fsd function to get a dict for that init_type
            fsd = big_normal(events, rfrac, rweld)
            for value in fsd:
                if value in averages:
                    averages[value].append(fsd[value])
                else:
                    averages[value] = []
                    averages[value].append(fsd[value])
                    
        elif init_type == "small_normal":
        # calls fsd function to get a dict for that init_type
            fsd = small_normal(events, rfrac, rweld)
            for value in fsd:
                if value in averages:
                    averages[value].append(fsd[value])
                else:
                    averages[value] = []
                    averages[value].append(fsd[value])
        elif init_type == "one_big2":
        # calls fsd function to get a dict for that init_type
            fsd = one_big2(events, rfrac, rweld)
            for value in fsd:
                if value in averages:
                    averages[value].append(fsd[value])
                else:
                    averages[value] = []
                    averages[value].append(fsd[value])
        elif init_type == "one_big_area":
        # calls fsd function to get a dict for that init_type
            fsd = one_big_area(events, rfrac, rweld)
            for value in fsd:
                if value in averages:
                    averages[value].append(fsd[value])
                else:
                    averages[value] = []
                    averages[value].append(fsd[value])
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
    
    # binning the trials with binning function
        bin_dict = log_binning(averages, binsize)
        return bin_dict, result[1]


def one_big(events, rfrac, rweld):  
    fsd_dict2 = {20000:1}
# this value is for the weld loop
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
            # and Randomly choose how many it will break in to (4, 16?)

            choice = float(pick_floe(fsd_dict2))
            new_size = choice/2
            
        # remove 1 from the bigger value and add 4 to the broken value
            fsd_dict2[choice] -= 1
            
            if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 4
            else:
                fsd_dict2[new_size] = 4
                

        elif val == 2:   # Weld occurs
            # choose a place to weld
            choice = float(pick_floe(fsd_dict2))

            
            if fsd_dict2[choice] < 4:
                # check and see how many there are in our choice
                choice_total = fsd_dict2[choice]
            
                # see how many floes we need
                needed_floes = (4 - choice_total)
            
                for i in range(1000):
                    if opt_out == 1:
                        continue
                
                # check if a sligtly larger floe is available to weld 
                    elif (choice + i) in fsd_dict2 and fsd_dict2[(choice + i)] > 0:
                        if fsd_dict2[choice + i] >= needed_floes:
                            fsd_dict2[choice + i] -= needed_floes
                            fsd_dict2[choice] = 0
                            opt_out = 1
                    
                    # change the vals in the dictionary
                            if needed_floes == 3:
                                new_size = (choice + i)*2
                                if new_size in fsd_dict2:
                                    fsd_dict2[new_size] += 1

                                else:
                                    fsd_dict2[new_size] = 1
                            else: 
                                new_size = (choice + i) + choice
                                if new_size in fsd_dict2:
                                    fsd_dict2[new_size] += 1

                                else:
                                    fsd_dict2[new_size] = 1
    return fsd_dict2, time_events


# normal distribution of mean = 3400, sd = 900, n = 1000
def big_normal(events, rfrac, rweld):
    fsd_dict2 = {}
    data = normal(loc=3400, scale=900, size=1000)
    fsd = data.tolist()
    for item in fsd:
        if item not in fsd_dict2:
            fsd_dict2[item] = 1
        else:
            fsd_dict2[item] += 1
        
# this value is for the weld loop
    opt_out = 0
    events = random_event(events, rfrac, rweld)
    for val in events:
        keys = list(fsd_dict2.keys())
        sizes =[]
        
        for key in keys:
            if fsd_dict2[key] > 0:
                sizes.append(key)
    
        if val == 0:
            continue
            
        elif val == 1:   # Fracture occurs
            choice = float(pick_floe(fsd_dict2))
            new_size = choice/2
            fsd_dict2[choice] -= 1
            if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 4
            else:
                fsd_dict2[new_size] = 4
                

        elif val == 2:   # Weld occurs
            # choose a place to weld
            choice = float(pick_floe(fsd_dict2))

            if fsd_dict2[choice] < 4:
                choice_total = fsd_dict2[choice]
                needed_floes = (4 - choice_total)
            
                for i in range(1000):
                    if opt_out == 1:
                        continue
                
                # check if a sligtly larger floe is available to weld 
                    elif (choice + i) in fsd_dict2 and fsd_dict2[(choice + i)] > 0:
                        if fsd_dict2[choice + i] >= needed_floes:
                            fsd_dict2[choice + i] -= needed_floes
                            fsd_dict2[choice] = 0
                            opt_out = 1
                    
                    # change the vals in the dictionary
                            if needed_floes == 3:
                                new_size = (choice + i)*2
                                if new_size in fsd_dict2:
                                    fsd_dict2[new_size] += 1

                                else:
                                    fsd_dict2[new_size] = 1
                            else: 
                                new_size = (choice + i) + choice
                                if new_size in fsd_dict2:
                                    fsd_dict2[new_size] += 1

                                else:
                                    fsd_dict2[new_size] = 1
    return fsd_dict2


# small normal distribution with mean = 1000, sd = 100, n = 500
def small_normal(events, rfrac, rweld):
    fsd_dict2 = {}
    data = normal(loc=1000, scale=100, size=500)
    fsd = data.tolist()
    for item in fsd:
        if item not in fsd_dict2:
            fsd_dict2[item] = 1
        else:
            fsd_dict2[item] += 1
        
# this value is for the weld loop
    opt_out = 0
    events = random_event(events, rfrac, rweld)
    for val in events:
        keys = list(fsd_dict2.keys())
        sizes =[]
        
        for key in keys:
            if fsd_dict2[key] > 0:
                sizes.append(key)
    
        if val == 0:
            continue
            
        elif val == 1:   # Fracture occurs
            choice = float(pick_floe(fsd_dict2))
            new_size = choice/2
            fsd_dict2[choice] -= 1
            if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 4
            else:
                fsd_dict2[new_size] = 4
                

        elif val == 2:   # Weld occurs
            # choose a place to weld
            choice = float(pick_floe(fsd_dict2))

            if fsd_dict2[choice] < 4:
                choice_total = fsd_dict2[choice]
                needed_floes = (4 - choice_total)
            
                for i in range(1000):
                    if opt_out == 1:
                        continue
                
                # check if a sligtly larger floe is available to weld 
                    elif (choice + i) in fsd_dict2 and fsd_dict2[(choice + i)] > 0:
                        if fsd_dict2[choice + i] >= needed_floes:
                            fsd_dict2[choice + i] -= needed_floes
                            fsd_dict2[choice] = 0
                            opt_out = 1
                    
                    # change the vals in the dictionary
                            if needed_floes == 3:
                                new_size = (choice + i)*2
                                if new_size in fsd_dict2:
                                    fsd_dict2[new_size] += 1

                                else:
                                    fsd_dict2[new_size] = 1
                            else: 
                                new_size = (choice + i) + choice
                                if new_size in fsd_dict2:
                                    fsd_dict2[new_size] += 1

                                else:
                                    fsd_dict2[new_size] = 1
    return fsd_dict2


def one_big2(events, rfrac, rweld):  
    fsd_dict2 = {400000000:1}
# this value is for the weld loop
# this function defines area not width
    opt_out = 0
    events = random_event(events, rfrac, rweld)
    for val in events:
        # define all the possible sizes
        keys = list(fsd_dict2.keys())
        sizes =[]
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
            new_size = choice/2
            
        # remove 1 from the bigger value and add 4 to the broken value
            fsd_dict2[choice] -= 1
            
            if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 2
            else:
                fsd_dict2[new_size] = 2
                

        elif val == 2:   # Weld occurs
            # choose a place to weld
            choice = float(pick_floe(fsd_dict2))

            
            if fsd_dict2[choice] < 2:
                # check and see how many there are in our choice
                choice_total = fsd_dict2[choice]
            
                # see how many floes we need
                needed_floes = (2 - choice_total)
            
                for i in range(1000):
                    if opt_out == 1:
                        continue
                
                # check if a sligtly larger floe is available to weld 
                    elif (choice + i) in fsd_dict2 and fsd_dict2[(choice + i)] > 0:
                        if fsd_dict2[choice + i] >= needed_floes:
                            fsd_dict2[choice + i] -= needed_floes
                            fsd_dict2[choice] = 0
                            opt_out = 1
                    
                    # change the vals in the dictionary
                            if needed_floes == 3:
                                new_size = (choice + i)*2
                                if new_size in fsd_dict2:
                                    fsd_dict2[new_size] += 1

                                else:
                                    fsd_dict2[new_size] = 1
                            else: 
                                new_size = (choice + i) + choice
                                if new_size in fsd_dict2:
                                    fsd_dict2[new_size] += 1

                                else:
                                    fsd_dict2[new_size] = 1
    return fsd_dict2

def one_big_area(events, rfrac, rweld):  
    fsd_dict2 = {400000000:1}
# this value is for the weld loop
    opt_out = 0
    events = random_event(events, rfrac, rweld)
    for val in events:
        # define all the possible sizes
        keys = list(fsd_dict2.keys())
        sizes =[]
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
            new_size = choice/2
            
        # remove 1 from the bigger value and add 4 to the broken value
            fsd_dict2[choice] -= 1
            
            if new_size in fsd_dict2:
                    fsd_dict2[new_size] += 4
            else:
                fsd_dict2[new_size] = 4
                

        elif val == 2:   # Weld occurs
            # choose a place to weld
            choice = float(pick_floe(fsd_dict2))

            
            if fsd_dict2[choice] < 4:
                # check and see how many there are in our choice
                choice_total = fsd_dict2[choice]
            
                # see how many floes we need
                needed_floes = (4 - choice_total)
            
                for i in range(1000):
                    if opt_out == 1:
                        continue
                
                # check if a sligtly larger floe is available to weld 
                    elif (choice + i) in fsd_dict2 and fsd_dict2[(choice + i)] > 0:
                        if fsd_dict2[choice + i] >= needed_floes:
                            fsd_dict2[choice + i] -= needed_floes
                            fsd_dict2[choice] = 0
                            opt_out = 1
                    
                    # change the vals in the dictionary
                            if needed_floes == 3:
                                new_size = (choice + i)*2
                                if new_size in fsd_dict2:
                                    fsd_dict2[new_size] += 1

                                else:
                                    fsd_dict2[new_size] = 1
                            else: 
                                new_size = (choice + i) + choice
                                if new_size in fsd_dict2:
                                    fsd_dict2[new_size] += 1

                                else:
                                    fsd_dict2[new_size] = 1
    return fsd_dict2

