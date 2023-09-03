# function to read input
def get_width_input(): 
    w = float(input("key in width: "))
    return w

def get_length_input(): 
    l = float(input("key in length: "))
    return l
    
# function to calculate the area of circle
def calculate(w, l):
    W = get_width_input()
    L = get_length_input()
    area = W * L
    return area

# main
def main():
    x = get_width_input()
    y = get_length_input()
    area = calculate(x, y)
    print(f"Area: {area}")

if __name__ == "__main__":
    main() # call main()

