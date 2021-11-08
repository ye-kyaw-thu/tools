"""
 for teaching list usages of Python
 Written by Ye Kyaw Thu, NECTEC, Thailand
 Last updated: 8 Nov 2021
# Reference: 
# an article of towards data science entitled "6 Amazing Things You Can Do With Python Lists " by Pranjal Saxena
"""

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('list1: ', list1)

# slice operation
# လိုချင်တဲ့ အပိုင်းကိုပဲ ဖြတ်ယူတာ
elements = slice(4 , 10 , 1)
list2 = list1[elements]

print('after slicing with slice(4, 10, 1): ', list2)

# apply similar operation on each element of the list
# operation တစ်ခုခုကို list ထဲက element အကုန်ကို apply လုပ်တာမျိုး

def multi(x):
    return 10*x
    
print('apply "10*x" to every element of the list1 with "map": ', list(map(multi, list1)))

# reversing a list
str="ဒီညတော့ ဂျူးပဲပုပ်ကြော် နဲ့ ညစာ စားမယ်"
print('original string: ', str)
print('after reversing a list: ', str[::-1])


myanmar = ["မူလတန်း", "အလယ်တန်း", "အထက်တန်း"]
english = ["primary school", "middle school", "high school"]
years = [5,3,2]

# list တစ်ခုထက်မက ကို iteration လုပ်တဲ့ ပုံစံ
# f-string formatting ကိုလည်း သုံးပြထားပါတယ်
for my, eng, yrs in zip(myanmar, english, years):
    print(f'{my}, In English "{eng}", {yrs} years course.')

# joining "list values" of key-value pairs in a dictionary
# dictionary ထဲမှာ ရှိနေတဲ့ list ကို ပေါင်းတဲ့ ပုံစံ
even_odd_dict = {"odd": [1, 3, 5, 7, 9], "even":[2, 4, 6, 8, 10]}
print('even_odd_dict: ', even_odd_dict)
all_numbers = sum(even_odd_dict.values(), [])
print('After joining all list values: ', all_numbers)

# merging two lists to form a dictionary
# list နှစ်ခုကို ပေါင်းပြီးတော့ dictionary အသစ်ဆောက်သွားတဲ့ ပုံစံ
drinks = ["Cafe Latte", "American Coffee", "Matcha Latte", "Cappuccino", "Lemon Tea"]
price = [60 , 45, 70, 60, 55]
menu_dictionary = dict(zip(drinks, price))
print('after merging two lists: ', menu_dictionary)


