def matchedChar(str1,str2):
    temp1=set(str1.lower())
    temp2=set(str2.lower())
    return len(temp1 & temp2)

    # count=0
    # for i in range(len(temp1)):
    #     ch1=temp1[i]
    #     if not (ch1 in temp1[:i]):
    #         for ch2 in temp2:
    #             if ch1 == ch2:
    #                 count+=1
    # return count


str1=input("Enter String 1:")
str2=input("Enter String 2:")
print("Number of Matched Charecters ",matchedChar(str1,str2))

