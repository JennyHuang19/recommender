'''
@author: Yijian Jenny Huang (yjh3)
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    #The first element is a list of the book titles rated. The second element is ratings, a dictionary of user/raters to lists of ratings.
    f = open("data/books.txt")
    items = [] #list of books
    d = {}
    datalist = []
    for line in f:
        data = line.strip().split(',')
        for i in range(len(data)):
            if i%2 == 1 and data[i] not in items:
                items.append(data[i])
                #all of the books are located on odd indices. No repeats
        datalist.append(data) #a list of lists [[student,movie,strRanking],[student,movie,strRanking]..]
#     print(items)
#     print(len(items))
    for line in datalist:
        student = line[0]
        d[student] = [int(line[i]) for i in range(1, len(line)) if i%2 == 0] #index iteration of the elements in 1 line.
#     print(d)
#     print(len(d["student1001"]))
    f.close()
    #Return value: (["book1","book2"],{"student1": [2,4], "student2": [3,5]})
    return (items, d)

if __name__ == '__main__':
    print(getdata())