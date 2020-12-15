import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# plotting Myanmar unicode characters with matplotlib
# Note: plotting syllables are not working with this program
# written by Ye Kyaw Thu, Visiting Professor, LST, NECTEC, Thailand
# ref: https://jdhao.github.io/2018/04/08/matplotlib-unicode-character/
# ref: https://stackoverflow.com/questions/3899980/how-to-change-the-font-size-on-a-matplotlib-plot
# how to run: python plot-unicode-char.py

fontPath = '/home/ye/.local/share/fonts/myanmar3.ttf'
prop = fm.FontProperties(fname=fontPath, size=60)

# အောက်ပါ parameter တွေကလည်း သိထားသင့်တယ်
#plt.rcParams['font.family'] = 'sans-serif'
#plt.rcParams['font.sans-serif'] = ['Myanmar3']
#matplotlib.rcParams.update({'font.size': 50})

plt.text(0.2, 0.2, "က", fontproperties=prop)
plt.text(0.4, 0.4, "ခ", fontproperties=prop, size=45)
plt.text(0.6, 0.6, "ဂ", fontproperties=prop, size=35)
plt.text(0.8, 0.8, "ဃ", fontproperties=prop, size=25)
plt.text(0.9, 0.9, "င", fontproperties=prop, size=15)

plt.savefig('plot-unicode-char.png')
plt.show()

