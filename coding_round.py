def sum_count(list_array):
    count_value=0
    user_entered_sum_value=int(input("Enter the sum value"))
    for i in range(0,len(list_array)):
        for j in range(1,len(list_array)-1):
            sum1=list_array[i]+list_array[j]
            if user_entered_sum_value==sum1:
                count_value=count_value+1
                print("pairs{},{}".format(list_array[i],list_array[j]))
    print(count_value)
sum_count([1,5,7,-1,5])

def pair_color(s):
    list_conversion=list(s)
    removing_duplicate=set(list_conversion)
    if len(removing_duplicate)==0:
        return "True"
    else:
        return "False"

pair_color("RBBR")
