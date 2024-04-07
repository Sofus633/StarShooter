def check_collition(object1, object2):
    # [[x, y], [w, h]]
    obj1_upc = object1[0]
    obj1_downc = [object1[0][0] + object1[1][0], object1[0][1] + object1[1][1]]
    
    obj2_upc = object2[0]
    obj2_downc = [object2[0][0] + object2[1][0], object2[0][1] + object2[1][1]]
    
    if obj1_upc[0] < obj2_upc[0] and obj2_upc[0] < obj1_downc[0] and obj1_upc[1] < obj2_upc[1] and obj2_upc[1] < obj1_downc[1]:
        return True
    else:
        return False