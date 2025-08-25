# Do_E0
def chili_amount_for_family_49() :
    chili = [0] * 49
    chili[0] = 2
    chili[1] = 2
    
    for i in range(2, 49) :
        amount = chili[i-1] + chili[i-2]
        if amount >= 30 :
            chili[i] = 1
        else:
            chili[i] = amount
    
    return chili[48]

if __name__ == "__main__" :
    result = chili_amount_for_family_49()
    print(result)