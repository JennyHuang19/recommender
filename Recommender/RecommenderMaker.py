'''
@author: Yijian Jenny Huang (yjh3)
'''
import RecommenderEngine

def makerecs(name, items, ratings, numUsers, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists. 
    The first list is the top items rated by the rater called name (string).
    The second list is the top items not seen/rated by name (string)
    '''
    #[('A Beautiful Mind', 335.0), ('Black Swan', 335.0), ('Anchorman: The Legend of Ron Burgundy', 247.5)]
    avgTups = RecommenderEngine.recommendations(name, items, ratings, numUsers)
    #Correct. the movies the person has rated.
    hasRated = [] 
    #get the movies the person has rated.
    for i in range(len(items)):
        if ratings[name][i]!= 0: #check to see the movie has been rated
            hasRated.append(items[i]) #append that movie into hasRated.

    #pick out the top hasRated values to put in favorites.
    favorites = [] #Correct. [('Anchorman: The Legend of Ron Burgundy', 247.5), ('Avatar', 215.5), ('The Godfather', 201.0)]
    #the (movie, avgrating) for movies the person rated.
    for tuple in avgTups:
        if tuple[0] in hasRated: #the movie has been rated
            favorites.append(tuple)
    #print(favorites)
    topfavs = favorites[:top]       
    #print(topfavs) 
    
    #pick out the top notRated values to put in recLst.
    recLst = []#notRate[:top] [('A Beautiful Mind', 335.0), ('Black Swan', 335.0), ('A Nightmare on Elm Street', 96.0)]
    for tuple in avgTups:
        if tuple[0] not in hasRated: #pick out movies that have not been rated.
            recLst.append(tuple)
    #print(recLst)
    toprec = recLst[:top]
    
    return (topfavs, toprec)


if __name__ == '__main__':
    name = 'student1367'
    items = ['127 Hours', 'The Godfather', '50 First Dates', 'A Beautiful Mind', 'A Nightmare on Elm Street', 'Alice in Wonderland', 'Anchorman: The Legend of Ron Burgundy', 'Austin Powers in Goldmember', 'Avatar', 'Black Swan']
    ratings = {'student1367': [ 0, 3,-5, 0, 0, 1, 5, 1, 3, 0], 
    'student1046': [ 0, 0, 0, 3, 0, 0, 0, 0, 3, 5], 
    'student1206': [-5, 0, 1, 0, 3, 0, 5, 3, 3, 0], 
    'student1103': [-3, 3,-3, 5, 0, 0, 5, 3, 5, 5]}
    numUsers = 2
    top = 3

    print(makerecs(name, items, ratings, numUsers, top))
             



