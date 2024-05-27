def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print(plate)
    else:
        print("InValid")

    

def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        if s.isalpha() :
            return True
        else:
            flag = False
            for i in s:
                if i.isdigit():
                    if flag==False:
                        if i == "0":
                            return False
                        else:
                            flag = True
                    if flag == True:
                        pass
                if i.isalpha():
                    if flag == True:
                        return False
                    if flag == False:
                        pass
            return True
        
            
    else:
        return False
if __name__ == "__main__":
    main()

                    
        