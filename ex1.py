def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    #create compliments
    compliments = {}
    #create array = 

    for index in range(length):
        zeroth = 0
        first = 0
        difference = limit - weights[index]
        if difference in compliments:
            compliment_number = compliments[difference]
            if index > compliment_number:
                match_number = (index, compliment_number)
            else:
                match_number = (compliment_number, index)
            return match_number
        else:
            compliments[weights[index]] = index 
    return None
