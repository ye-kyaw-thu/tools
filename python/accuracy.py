"""
Function to calculate accuracy
written by Ye Kyaw Thu, LST, NECTEC, Thailand
last updated date: 27 Oct 2021
reference: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
"""

# accuracy တွက်ဖို့အတွက်က
# ကိုယ့်ဖာသာကိုယ် function ဆောက်ပြီး တွက်မယ် ဆိုရင်လည်း လွယ်ပါတယ်
def calc_accuracy(ref, pred):
   correct_count = 0
   for y_true, y_pred in zip(ref, pred):
      if y_true == y_pred:
         correct_count += 1
   return correct_count / len(ref)

# ဒီနေရာမှာ reference ဆိုတာက accuracy တွက်တဲ့အခါမှာ နှိုင်းယှဉ်ဖို့ အတွက် ကြိုတင်ပြင်ဆင်ထားတဲ့ ရလဒ်အမှန်
# prediction ဆိုတဲ့ list variable ကတော့ algorithm သို့မဟုတ် model တစ်ခုခုကနေ ထွက်လာတဲ့ output ရလဒ်ပါ
reference = [1,1,0,1,0,0,1,1,0,1]
prediction = [1,0,1,1,0,1,1,0,1,1]

accuracy = calc_accuracy(reference, prediction)
print("Accuracy calculation with calc_accuracy(ref, pred): ", accuracy)

# တကယ်က sklearn python library package ကို သုံးပြီး တွက်မယ် ဆိုရင်လည်း ရပါတယ်
from sklearn import metrics

# metrics.accuracy_score(y_true, y_pred, *, normalize=True, sample_weight=None)
# default parameter setting အတိုင်းပဲ ထား တွက်ကြည့်ရအောင်
accuracy=metrics.accuracy_score(reference, prediction)
print("Accuracy calculation with sklearn package's metrics.accuracy_score() with default parameters:", accuracy)

# ဒီနေရာမှာ normalize ဆိုတာက default က True ဆိုတဲ့ setting ပါ
# False ထားထားရင်တော့ classification လုပ်ထားတဲ့ output မှာ ဘယ်နှစ်ခု မှန်တယ် (the number of correctly classified samples) ဆိုတဲ့ အရေအတွက်ကို 
# အတိအကျ return လုပ်လိမ့်မယ်
# True နဲ့ ဆိုရင်တော့ ဘယ်လောက် classification မှန်တယ်ဆိုတဲ့ အချိုးတန်ဖိုး (the fraction of correctly classified samples) ကို return ပြန်ပေးပါလိမ့်မယ်။
accuracy=metrics.accuracy_score(reference, prediction, normalize=False)
print("Accuracy calculation with sklearn package\'s metrics.accuracy_score() with parameter \"normalize=False\":", accuracy)

