Dictionary1={'Project':"Lab1",'Course':"Python",'TeamMember1':"Srinivas",'TeamMember2':"Shiva",'TeamMember3':"vamshi"}
Dictionary2={'ClassID1':"16",'ClassID2':"17",'ClassID3':"26",'University':"UMKC",'Country':"UnitedStates"}
Dictionary1.update(Dictionary2)
print(Dictionary1)
Sorted_Dictionary= sorted(Dictionary1.items(), key=lambda x: x[1])    
print(Sorted_Dictionary)