"""
 F1-score calculation example for single 
written by Ye Kyaw Thu, LST, NECTEC, Thailand
Date: 26 Oct 2021

# Reference:
https://datascience.stackexchange.com/questions/15989/micro-average-vs-macro-average-performance-in-a-multiclass-classification-settin
http://rushdishams.blogspot.com/2011/08/micro-and-macro-average-of-precision.html
"""

# micro-average နဲ့ macro-average က တွက်ပုံက အနည်းငယ်ကွဲပြားတယ်။ အဲဒါကြောင့် အဖြေကလည်း တထပ်တည်း တူမှာမဟုတ်ဘူး။
# micro-average ကတော့ class အမျိုးအစားကွဲ ရှိသလောက် ကိုအားလုံးစုပေါင်းပြီးမှ average တွက်တဲ့ ပုံစံပါ။
# အသေးစိတ်ပြောရရင် true-positive တွေ အားလုံးပေါင်း၊ false-positive တွေ အားလုံးပေါင်း၊ false-negative တွေ အားလုံးကိုလည်း ပေါင်းပြီးမှ
# တွက်သွားတဲ့ ပုံစံပါ။ အောက်ပါအတိုင်းပါ...  
# P = TP/(TP+FP), R = TP/TP+FN
# အဲဒါကြောင့် micro-average က multi-class classification အတွက် ပိုသင့်တော်ပါတယ်။
# အထူးသဖြင့် ဒေတာထဲမှာ class အမျိုးအစား ပါဝင်မှု အရေအတွက်က မညီမျှနိုင်တဲ့မျိုးအခြေအနေမျိုးမှာပါ။
# ဥပမာ class အမျိုးအစား တစ်ခုမှာ အရေအတွက်က အရမ်းကြီးများနေတဲ့ case မျိုးမှာ...  

# macro-average က class တစ်ခုချင်းစီအတွက် သပ်သပ်စီ တွက်ပြီးမှ average ယူတယ်။ class အားလုံးကို ညီတူညီမျှပဲ ထားပြီး စဉ်းစားတယ်။
# macro-average တွက်တဲ့ ပုံစံက 
# macro-average-precision = P1+P2/2 (true, false class နှစ်မျိုးပဲ ရှိလို့)
# macro-average-recall = R1 + R2/2
# system တစ်ခု အနေနဲ့ သို့မဟုတ် model တစ်ခုရဲ့ dataset ပေါ်မှာ ရလာတဲ့ performance ကို ကြည့်ဖို့အတွက် အသုံးဝင်တယ်
# NLP သမားတွေ၊ ML သမားတွေ ပြောနေကြတဲ့ precision, recall, F1-socre တွေက default က macro ပါ

# module, package loading
from sklearn.metrics import confusion_matrix, classification_report, precision_score, recall_score, f1_score
import random


# prepare reference data
# ture, false တွေကို အကြိမ် ၁၀၀ ကျပန်း ယူလိုက်ပြီး reference အနေနဲ့ ထားလိုက်တာ
reference = [random.choice([True, False])  for x in range(100)]
print("Reference: ", reference)

# simulation of model prediction
# model တစ်ခုခုက ခန့်မှန်းပြီး ထွက်လာတဲ့ အဖြေကိုလည်း အထက်ကလိုပါပဲ အကြိမ် ၁၀၀ ကျပန်း ယူလိုက်ပြီး list တစ်ခု ဆောက်လိုက်တာပါ
prediction = [random.choice([True, False])  for x in range(100)]
print("\nModel Output: ", prediction)

# confusion matrix
print("\nConfusion matrix:")
print(confusion_matrix(reference, prediction, labels=[True, False]))

#calculate F1 score
precision=precision_score(reference, prediction)
print("\nParameter: average=micro")
print("Precision: ", precision)
recall=recall_score(reference, prediction)
print("Recall: ", recall)
score=f1_score(reference, prediction)
print("F1 Score: ", score)

precision=precision_score(reference, prediction, average='macro')
print("\nParameter: average=macro")
print("Precision: ", precision)
recall=recall_score(reference, prediction, average='macro')
print("Recall: ", recall)
score=f1_score(reference, prediction, average='macro')
print("F1 Score: ", score)

# using classification_report()
print("\nClassification_report():")
print(classification_report(reference, prediction, labels=[True, False]))
