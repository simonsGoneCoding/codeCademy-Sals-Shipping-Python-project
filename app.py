# In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

weight = 8.4; 

#Ground Shipping: 

if weight <= 2:
  cost_ground = weight * 1.5 + 20.00; 
elif weight > 2 and weight <= 6: 
  cost_ground = weight * 3.00 + 20.00; 
elif weight > 6 and weight <= 10: 
  cost_ground = weight * 4.00 + 20.00; 
elif weight > 10 
  cost_ground = weight * 4.75 + 20.00; 

const_ground_premium = 125; 
 
print("Ground Shipping Premimium $", cost_ground_premium)
print(cost_ground)    #returns 53.60


# Drone shipping: 

if weight <= 2:
  cost_drone = weight * 4.5;
elif weight > 2 and weight <= 6: 
  cost_drone = weight * 9.00; 
elif weight > 6 and weight <= 10: 
  cost_drone = weight * 12.00; 
elif weight > 10 
  cost_drone = weight * 14.25; 


