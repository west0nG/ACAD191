'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Lab 5
'''

def loadFile(fileName, dataDictionary):
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                parts = line.split(',')
                if len(parts) >= 2:
                    subreddit = parts[0].strip()
                    count = parts[1].strip() 
                    dataDictionary[subreddit] = count
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        return False

def main():
    dataDictionary = {}  
    while True:
        fileName = input("Tallies file: ")
            
        if loadFile(fileName, dataDictionary):
            print("Loading data...")
            break
        else:
            print(f'Could not open the file "{fileName}"')
    
    while True:
        subreddit = input("Subreddit: ")
        
        if not subreddit:
            print("Goodbye!")
            break
            
        if subreddit in dataDictionary:
            print(f"{subreddit} --> {dataDictionary[subreddit]}")
        else:
            print(f'"{subreddit}" is an unknown subreddit')
    
if __name__ == "__main__":
    main()
