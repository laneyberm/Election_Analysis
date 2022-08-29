""" print("Hello World") """
counties = ["Arapahoe","Denver","Jefferson"]
""" if counties[1] == 'Denver':
    print(counties[1]) """
""" if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else: 
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county) """

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
""" 
    print(county)   
for voters in counties_dict.values():
    print(voters) """

""" the following two does the same function as the above to get the amount of voters """
""" for county in counties_dict:
    print(counties_dict[county]) """
""" for county in counties_dict:
    print(counties_dict.get(county))  """   
""" for county, voters in counties_dict.items():
    print(county , voters)
    print() """
    
""" voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}] """
""" for county_dict in voting_data:
    print(county_dict) """
""" for i in range(len(voting_data)):
    print(voting_data[i]['county']) """
""" for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
#print(counties_dict["Denver"])
for county_dict in voting_data:
    print(county_dict['county'])
for county_dict in voting_data:
    print(county_dict['registered_voters']) """
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")
#How to use an f string to make the same output as the for statement above
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")
""" counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.") """
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]
for d in voting_data:
    print(f"{d['county']} county has {d['registered_voters']} registered voters.")


