def cigar_party(cigar,is_weekend):
    if ((40 < cigar < 60) and not is_weekend):
        return True
    elif (cigar > 40 and is_weekend):
        return True
    else:
        return False
    
print(cigar_party(30,False))
print(cigar_party(50,False))
print(cigar_party(70,True))
