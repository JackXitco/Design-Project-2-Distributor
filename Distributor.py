import random
def main():
    loadList = ["701", "712", "713", "714", "718", 
                "720", "722", "724", "725", "727",
                "728", "729", "730", "731", "732",
                "733", "734", "735", "736", "737",
                "738", "740", "741", "742", "744"] #Buses in the IEEE 37 bus systems that have loads
    distributions = [0,0,0,0,0,
                    0,0,0,0,0,
                    0,0,0,0,0,
                    0,0,0,0,0,
                    0,0,0,0,0] #Blank distribution
    numBuses = len(loadList) #25 buses have loads
    numDistributions = 100 #Change this number for more or less iterations
    totalKW = 0 #Counter for number kW added in total
    for i in range (numDistributions + 1):
        j = random.randint(0, numBuses-1) #Picking a random bus to distribute to
        kw = random.randint(10, 32) #Randomly generate #kW to add
        distributions[j] += kw #Add kW to the randomly selected bus
        totalKW += kw #Keep track of total kW added
    for k in range(numBuses):
        print("{" + loadList[k] + ": +" + str(distributions[k]) + "kW}")
    print("Total kW added to system: " + str(totalKW) + "kW")
    return 0
main()