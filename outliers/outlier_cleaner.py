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

    ### your code goes here
    errors = [abs(i-j) for i,j in zip(predictions, net_worths)]
    index = -int(len(ages)*.10)
    threshold = sorted(errors)[index]

    for p,a,n in zip(predictions, ages, net_worths):
        e = abs(p-n)
        if e >= threshold:
            continue
        cleaned_data.append((a,n,e))

    return cleaned_data
