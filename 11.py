

#Problem-11: Write a program to solve the following 0/1
# Knapsack using dynamic programming approach 
# profits 𝑃 = (15,25,13,23), weight 𝑊 = (2,6,12,9), 
# Knapsack 𝐶 = 20, and the number of items n=4
def Knapsack (numitems, capacity, weight, value):

    # No item can be put in the sack of capacity 0 so maximum value for sack of capcacity 0 is 0
    if (capacity == 0):
        return 0

    # If 0 items are put in the sack, then maximum value for sack is 0
    if (numitems == 0):
        return 0

    # Note : Here the number of item is limited (unlike coin change / integer partition problem)
    # hence the numitems -> (numitems - 1) when the item is included in the knapsack
    if (capacity >= weight[numitems-1]):
        return max ( Knapsack (numitems-1, capacity, weight, value), # Item is not included.
                     Knapsack (numitems-1, capacity-weight[numitems-1], weight, value) + value[numitems-1] )# Item included.
    else:
        return Knapsack (numitems-1, capacity, weight, value)

# DP approach to 0-1 Knapsack problem
def DPKnapsack (capacity, weight, value):

    numitems = len(weight)
    maxval = [0] * (numitems+1)

    for r in range (numitems+1) :
        maxval[r] = [0] * (capacity+1)

    # If 0 items are put in the sack of capacity 'cap' then maximum value for each sack is 0
    for cap in range (capacity+1) :
        maxval[0][cap] = 0

    # No item can be put in the sack of capacity 0 so maximum value for sack of capcacity 0 is 0
    for item in range (numitems+1) :
        maxval[item][0] = 0

    # Note : Here the number of item is limited (unlike coin change / integer partition problem)
    # hence the numitems -> (numitems - 1) when the item is included in the knapsack
    for item in range (1, numitems+1) :
        for cap in range (1, capacity+1) :
            if (cap >= weight[item-1]) :
                maxval[item][cap] = max (maxval[item-1][cap], maxval[item-1][cap-weight[item-1]] + value[item-1])
            else:
                maxval[item][cap] = maxval[item-1][cap]

    return maxval[numitems][capacity]

weight = [2,6,12,9]
value =  [15,25,13,23,]
capacity = 20
print("Maximum value of 0-1 Knapsack using DP : " + str( DPKnapsack (capacity, weight, value)))