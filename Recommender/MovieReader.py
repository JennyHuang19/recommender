'''
@author: Yijian Jenny Huang (yjh3)
'''

def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    f = open("data/movies.txt")
    items = [] #list of movies
    d = {}
    datalist = []
    for line in f:
        data = line.strip().split(',') 
        datalist.append(data) #a list of lists [[student,movie,strRanking],[student,movie,strRanking]..]
    #sort the lines by (alphabetical) movies
    sortedLines = sorted(datalist, key = lambda x: x[1])
    
    #print(sortedLines)
    #print(len(sortedLines))
    
    #creating movie list
    for line in sortedLines:
        student = line[0]
        movie = line[1]
        strRanking = line[2]
        if movie not in items:
            items.append(movie)
            
    #creating blank dictionary values
    for line in sortedLines:
        student = line[0]
        movie = line[1]
        strRanking = line[2]
        if student not in d:
            d[student] = [0 for _ in range(len(items))]
            #if student in d, code goes on to the next student
    #iterate through sorted lines to fill in the rankings.
    for line in sortedLines: #fill the all zeros list with values using strRanking
        student = line[0]
        movie = line[1]
        strRanking = line[2]
        #retrieve index of movie in items
        dex = items.index(movie)
        #mutate the dexth value inside the [0,0,0] to the ranking
        d[student][dex] = int(strRanking)
        
    #print(d)

    f.close()

    return (items, d)

if __name__ == '__main__':
    print(getdata())