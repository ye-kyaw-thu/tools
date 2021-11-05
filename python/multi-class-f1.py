"""
 F1-Score calculation for multi-class classification
 written by Ye Kyaw Thu, LST, NECTEC, Thailand
 last updated date: 26 Oct 2021

"""

from sklearn.metrics import f1_score
import random
from random import randint

computer_roll = [random.randint(1,6) for x in range(100)]
print("Dice roll by a model: ", computer_roll)

player1_roll = [random.randint(1,6) for x in range(100)]
print("Dice roll by player1: ", player1_roll)

player2_roll = [random.randint(1,6) for x in range(100)]
print("Dice roll by player2: ", player2_roll)

#calculate multi-class F1 scores
# important: we need to set the average parameter to "None" to output the per class F1 score.
# အင်္ဂလိပ်လိုလည်း ရေးထားသလိုပါပဲ multi-class F1 score ကိုတွက်ပေးတာလည်း sklearn.metrics ရဲ့ f1_score function ပါပဲ
# အရေးကြီးတာက average=None ဆိုတဲ့ parameter ကို ထည့်ပေးရပါမယ်။ မဟုတ်ရင် error ပေးပါလိမ့်မယ်။
player1_score=f1_score(computer_roll, player1_roll, average=None)
print("F1-score for player1: ", player1_score)
player2_score=f1_score(computer_roll, player2_roll, average=None)
print("F1-score for player2: ", player2_score)

