
import json

def getdata():
    
    st = open("data/food.json").read() #{"Sarah Lee": [3, 3, 3, 3, 0, -3, 5, 0, -3], "Melanie":[5, 0, 3, 0, 1, 3, 3, 3, 1]}
    ratings = json.loads(st)  
    st = open("data/eateries.txt").read() #["DivinityCafe", "FarmStead", "IlForno", "LoopPizzaGrill", "McDonalds", "PandaExpress", "Tandoor", "TheCommons", "TheSkillet"]
    places = json.loads(st)
    
    return (places,ratings)


if __name__ == '__main__':
    items, ratings = getdata()
    print(items)
    print(ratings)