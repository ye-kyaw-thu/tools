# Example usages of perl programs

## clean-space.pl

```bash
lar@lar-air:~/tool/perl$ cat ./tst-input 
This is  a car.
  This is       a cat.


cat is a cat.     

Blue

B l     u           e    


lar@lar-air:~/tool/perl$ perl ./clean-space.pl ./tst-input 
This is a car.
This is a cat.
cat is a cat.
Blue
B l u e
lar@lar-air:~/tool/perl$
```

## rmEnglishSentences.pl

```bash
lar@lar-air:~/tool/perl$ cat tst-input2
မြန်မာစာ နဲ့ English
မြန်မာစာ နဲ့ အင်္ဂလိပ်စာ
ကခဂ နဲ့ abc
ကခဂ နဲ့ အေဘီစီ
Do you speak English?
အင်္ဂလိပ်စကား ပြောနိုင်လား။

ဘာလုပ်နေတာလဲ။ thinking လုပ်နေတာလား။
က a ခ b ဂ c
a b c d e f g
lar@lar-air:~/tool/perl$ perl ./rm-EnglishSentences.pl ./tst-input2 
မြန်မာစာ နဲ့ အင်္ဂလိပ်စာ
ကခဂ နဲ့ အေဘီစီ
အင်္ဂလိပ်စကား ပြောနိုင်လား။
```
