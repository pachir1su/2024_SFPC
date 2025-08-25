# Pre_E0
def can_get_apples() :
    stickers_chungcheong = {1, 3, 5, 7, 9, 10}
    stickers_chungnami = {1, 2, 4, 6, 8, 10}

    combined_stickers = stickers_chungcheong | stickers_chungnami

    all_required = set(range(1, 11))
    
    if combined_stickers == all_required:
        print("YES")
    else:
        print("NO")

can_get_apples()