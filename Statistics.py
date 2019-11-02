'''Created class that Calculates mean and standard deviation'''
class statistics:
    
    def __init__(self, num_list):
        #Instantiate and create list
        self.values = num_list                      

    def append(self, num):   
        #Append values to list                         
        self.values.append(num)

    def get_values(self):
        #Access list of values                            
        return self.values
          
    def mean(self):   
        #Calculate mean                               
        self.mean = sum(self.values)/len(self.values)
        return self.mean

    def variance(self):
        #Calculate variance
        distance_squared = [(n-self.mean)**2 for n in self.values]
        self.variance = sum(distance_squared)/(len(self.values) - 1)
        return self.variance

nums = statistics([1, 3, 5])
print(nums.values)
nums.append(7)
print(nums.values)
values = nums.get_values()
print(values)
mean = nums.mean()
print(mean)
nums.get_values()
print(nums.variance())