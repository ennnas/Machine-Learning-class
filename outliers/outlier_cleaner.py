#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    error_function = []
    ### your code goes here
    for pred_y,true_y in zip(predictions,net_worths):
        error_function.append( (pred_y-true_y)**2)
    #return the indexes of the ten highest errors
    remove = sorted(range(len(error_function)), key=lambda x: error_function[x])[-9:]
    for i,(eta,target,error) in enumerate(zip(ages,net_worths,error_function)):
        if i in remove:
            continue
        cleaned_data.append([eta,target,error])
    return cleaned_data



