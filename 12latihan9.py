list1 = [5,6,7]
list2 = ["lima", "enam", "tujuh"]
for i, (input_text, target_text) in enumerate(zip(list1, list2)):
    print(i, input_text, target_text)