def main():
    plist = []
    
    firstN = int(input("Value Greater than 1: "))
    secN = int(input("Value Greater than the one before: "))
    
    if firstN <= 1 or secN <= 1 or firstN > secN:
        print(" Try again")
    else:
        for num in range(firstN, secN +1 ):
            is_prime = True
            if num>1:
                for i in range (2,num):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    plist.append(num)
        print(plist)
                    
                
    ##################################################
    # Comlete your code here
    ##################################################

    return plist


if __name__ == '__main__':
    main()
