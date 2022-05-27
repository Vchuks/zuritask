# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open('Reading-Text-Files\story.txt',"r") as f:
        file=f.read()
        print(file)
        return file
        
    


def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    count = dict()
    txt = str(text)
    words = txt.split()
    for a in words:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    
    print(count) 
count_words()