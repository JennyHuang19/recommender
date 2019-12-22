'''
@author: Yijian Jenny Huang (yjh3)
'''
#We strongly suggest that you write the functions in this order.  This means you should be sure to write, test, debug, and submit to Gradescope for each one before starting the next one.

#items, a list of strings
#ratings, a dictionary of raters/users to a list of integer ratings
#name, the name of a rater/user that's a key in the dictionary ratings
#ratings["Melanie"][2]is 3, meaning that 3 is the rating Melanie gives "IlForno", the eatery in items[2]. 


def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    #ratDict = item, [rating1, rating2]
    rateDict = {}
    for i in range(len(items)):
        if i not in rateDict:
            rateDict[items[i]] = []
        for name in ratings:
            if ratings[name][i] == 0:
                continue
            rateDict[items[i]].append(ratings[name][i]) #ratings[name][i] is a rater's rating for that particular movie.
    #avgDct = key, sum(ratings)/len(list)
    avgDict = {}
    for i in rateDict:
        if len(rateDict[i]) == 0:
            avgDict[i] = 0.0 #when the length of ratings is 0.
        else:
            avgDict[i] = sum(rateDict[i])/len(rateDict[i]) #only when len != 0.
    #conditional. if value in ratDict is empty, the average should be 0.
    #do not count raters who give a value of 0 in rateDict.
    #return avgDict
    sortAlphabet = sorted(avgDict.items())
    sortedRate = sorted(sortAlphabet, key = lambda i:i[1], reverse = True)
    return sortedRate



def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    #similarity score is the dot product of that name's ratings to another name's ratings.
    simDict = {} #name, simRating
    for n in ratings:
        if n == name:
            continue
        dotprod = 0
        #index iteration of the list in the value in the dictionary.
        for i in range(len(ratings[n])):
            dotprod += ratings[n][i]*ratings[name][i] 
            if n not in simDict: #name or n
                #add the name and simRating to the dictionary
                simDict[n] = dotprod
    #sort by simRating and break ties by alphabetical order.
    simDictA = sorted(simDict.items())
    return sorted(simDictA, key = lambda x: x[1], reverse = True)     

 
def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''
    #multiply each value in the ratings list by the dotprod of that name (output x[1] of similarities)
    newRatings = {}
    dotprod = similarities(name, ratings) 
    ImpRaters = dotprod[:numUsers]
    ImpNames = [x[0] for x in ImpRaters]
    #Only use weighted ratings for the first numUsers raters in the list returned by similarities.
    for specname in ratings:
        if specname in ImpNames:
            #retrieve the dot product (similarity rating) from the list ImpRaters.
            specDotProd = [x[1] for x in ImpRaters if x[0] == specname][0]
            #multiply each item in list by the dot product.
            newratingLst = [num*specDotProd for num in ratings[specname]]
            #for num in ratings[name]: #the list of ratings for each person. 
            #weightednum = num*dotprod
            #CORRECT. newRatings = {} #nameofrater: their new ratings according to the weight outputted in similarities.
            newRatings[specname] = newratingLst
            #print(newRatings)
    #take the average of each item's rating across all the people in newRatings.
    avgTup = averages(items, newRatings) #[('FarmStead', 81.33), ('DivinityCafe', 1.33), ('LoopPizzaGrill', -75.0)]
    sortedA = sorted(avgTup)
    sortedB = sorted(sortedA, key = lambda x:x[1], reverse = True)
    return sortedB
        

if __name__ == '__main__':
    name = "me"
    items = ["DivinityCafe", "FarmStead", "LoopPizzaGrill"]
    ratings = {"me":
   [5, 3,-5], 
          "rater1":
   [1, 5,-3], 
 "rater2":
   [5,-3, 5], 
 "rater3":
   [1, 3, 0]}
    numUsers = 2
    print(recommendations(name, items, ratings, numUsers))
    
    pass