def TowerOfHanoi(num , source, destination, auxiliary):
    if num==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(num-1, source, auxiliary, destination)
    print ("Move disk",num,"from source",source,"to destination",destination)
    TowerOfHanoi(num-1, auxiliary, destination, source)
         
num = 4
TowerOfHanoi(num,'A','B','C')
