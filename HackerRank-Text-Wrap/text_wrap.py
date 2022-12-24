import textwrap

def wrap(string, max_width):
    modified_string = ''
    
    for i in range(len(string)):
        if i!=0 and i%max_width==0:
            modified_string+='\n'+string[i]
        else:
            modified_string+=string[i]
    return modified_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
