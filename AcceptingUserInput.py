def display(row1,row2,row3):
    position_index1 = int(input("Enter Your position: "))
    row1[position_index1] = 'x'
    row2[position_index1] = 'x'
    row3[position_index1] = 'x'
    print(row1)
    print(row2)
    print(row3)
  
input_row1 = ['','','']
input_row2 = ['','','']
input_row3 = ['','','']
result = display(input_row1,input_row2,input_row3)