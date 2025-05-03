


def rev_str(input_str:str):
    input_str = list(input_str)
    left,right =0 , len(input_str)-1
    while(left < right):
        temp = input_str[left]
        input_str[left]=input_str[right]
        input_str[right]=temp
        left+=1
        right-=1
    return "".join(input_str)

input_str="hello"
result = rev_str(input_str)
print(result)


