#Writing a function for paint area calaculator
import math
def paint_calc(height, width, cover):
    number_of_cans = math.ceil((test_h*test_w)/coverage) 
    print("Number of cans required will be ", number_of_cans)

test_h = int(input("Height"))
test_w = int(input("Width"))
coverage =5     
paint_calc(height=test_h, width =test_w, cover = coverage)