votingData = [{"county" :'Arapahoe', "registered voters" : 422829}, 
            {"county" : 'Denver' , "registered voters" : 463353}, 
            {"county" : 'Jefferson' , "registered voters" : 432438}]

countyDic = {"Arapahoe" : 422829, "Denver" : 413229, "Jefferson" : 390222}

for c , v in countyDic.items():
    print(f'{c} county has {v : ,} registered voters.')

print("Doing it a Different way")
print("")
print("")
print("")

for counties in range(len(votingData)):
    print(f'{votingData[counties]["county"]} county has {votingData[counties]["registered voters"] : ,} registered voters.')