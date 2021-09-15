import glob

with open("data.txt", "w") as file:
    
    path = "C:"
    
    while True:
        
        path += "/*"
        f = glob.glob(path)
        
        try:
            for fil in f:
                print(fil)
                fil = fil.replace('\\', "/")
                file.write(f"{fil}\n")
        except: print("\n\nERREUR\n\n")
