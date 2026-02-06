placeholder = input("")
second_placeholder = placeholder.split(" ")
third_placeholder = map(int, second_placeholder)
n,k = third_placeholder
scores = input("")
scores_list_str = scores.split(" ")
placeholder_list_2 = map(int, scores_list_str)
scores_list = list(placeholder_list_2)
placeholder_list = []
if len(scores_list) == n:
    for value in scores_list:
        if value>0 and value >= scores_list[k-1]:
            placeholder_list.append(value)
print(len(placeholder_list))