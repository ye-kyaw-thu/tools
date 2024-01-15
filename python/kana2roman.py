"""
for Kana to Romaji conversion.
Written by Ye Kyaw Thu, LU Lab., Myanmar.
Last updated: 15 Jan 2024

Reference:
https://en.wikipedia.org/wiki/Romanization_of_Japanese
https://github.com/emsk/romajify
https://j-talk.com/convert
https://ja.wikipedia.org/wiki/%E3%87%BE

How to run:
python ./kana2roman.py --help

python ./kana2roman.py --input ./test1.txt --method hepburn --output hepburn.txt
python ./kana2roman.py --input ./test1.txt --method nihon --output nihon.txt
python ./kana2roman.py --input ./test1.txt --method kunrei --output kunrei.txt

"""


import argparse

class Converter:
    MONOGRAPHS = {
        'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
        'ア': 'a', 'イ': 'i', 'ウ': 'u', 'エ': 'e', 'オ': 'o',
        'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
        'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko',

        'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
        'ガ': 'ga', 'ギ': 'gi', 'グ': 'gu', 'ゲ': 'ge', 'ゴ': 'go',

        'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
        'サ': 'sa', 'シ': 'shi', 'ス': 'su', 'セ': 'se', 'ソ': 'so',

        'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
        'ザ': 'za', 'ジ': 'ji', 'ズ': 'zu', 'ゼ': 'ze', 'ゾ': 'zo',

        'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
        'タ': 'ta', 'チ': 'chi', 'ツ': 'tsu', 'テ': 'te', 'ト': 'to',

        'だ': 'da', 'ぢ': 'ji', 'づ': 'zu', 'で': 'de', 'ど': 'do',
        'ダ': 'da', 'ヂ': 'ji', 'ヅ': 'zu', 'デ': 'de', 'ド': 'do',

        'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
        'ナ': 'na', 'ニ': 'ni', 'ヌ': 'nu', 'ネ': 'ne', 'ノ': 'no',

        'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
        'ハ': 'ha', 'ヒ': 'hi', 'フ': 'fu', 'ヘ': 'he', 'ホ': 'ho',

        'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
        'バ': 'ba', 'ビ': 'bi', 'ブ': 'bu', 'ベ': 'be', 'ボ': 'bo',

        'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po',
        'パ': 'pa', 'ピ': 'pi', 'プ': 'pu', 'ペ': 'pe', 'ポ': 'po',

        'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
        'マ': 'ma', 'ミ': 'mi', 'ム': 'mu', 'メ': 'me', 'モ': 'mo',

        'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
        'ヤ': 'ya', 'ユ': 'yu', 'ヨ': 'yo',

        'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
        'ラ': 'ra', 'リ': 'ri', 'ル': 'ru', 'レ': 're', 'ロ': 'ro',

        'わ': 'wa', 'ゐ': 'i', 'ゑ': 'e', 'を': 'o', 'ん': 'n',
        'ワ': 'wa', 'ヰ': 'i', 'ヱ': 'e', 'ヲ': 'o', 'ン': 'n',

        'ぁ': 'a', 'ぃ': 'i', 'ぅ': 'u', 'ぇ': 'e', 'ぉ': 'o',
        'ァ': 'a', 'ィ': 'i', 'ゥ': 'u', 'ェ': 'e', 'ォ': 'o',
        'ゃ': 'ya', 'ゅ': 'yu', 'ょ': 'yo',
        'ャ': 'ya', 'ュ': 'yu', 'ョ': 'yo',
        'ゔ': 'bu', 'ヴ': 'bu', 'ー': '', '＿': '_', '、': ',', '。': '.'
   }

    DIGRAPHS = {
        'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo',
        'キャ': 'kya', 'キュ': 'kyu', 'キョ': 'kyo',

        'しゃ': 'sha', 'しゅ': 'shu', 'しょ': 'sho',
        'シャ': 'sha', 'シュ': 'shu', 'ショ': 'sho',

        'じゃ': 'ja', 'じゅ': 'ju', 'じょ': 'jo',
        'ジャ': 'ja', 'ジュ': 'ju', 'ジョ': 'jo',

        'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho',
        'チャ': 'cha', 'チュ': 'chu', 'チョ': 'cho',

        'ぢゃ': 'ja', 'ぢゅ': 'ju', 'ぢょ': 'jo',
        'ヂャ': 'ja', 'ヂュ': 'ju', 'ヂョ': 'jo',

        'にゃ': 'nya', 'にゅ': 'nyu', 'にょ': 'nyo',
        'ニャ': 'nya', 'ニュ': 'nyu', 'ニョ': 'nyo',

        'ひゃ': 'hya', 'ひゅ': 'hyu', 'ひょ': 'hyo',
        'ヒャ': 'hya', 'ヒュ': 'hyu', 'ヒョ': 'hyo',

        'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo',
        'ビャ': 'bya', 'ビュ': 'byu', 'ビョ': 'byo',

        'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo',
        'ピャ': 'pya', 'ピュ': 'pyu', 'ピョ': 'pyo',

        'みゃ': 'mya', 'みゅ': 'myu', 'みょ': 'myo',
        'ミャ': 'mya', 'ミュ': 'myu', 'ミョ': 'myo',

        'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo',
        'リャ': 'rya', 'リュ': 'ryu', 'リョ': 'ryo'

    }
    NIHON_MONOGRAPHS = {
        'し': 'si', 'ち': 'ti', 'つ': 'tu', 'ふ': 'hu', 'じ': 'zi', 'ぢ': 'di', 'づ': 'du',
    'シ': 'si', 'チ': 'ti', 'ツ': 'tu', 'フ': 'hu', 'ジ': 'zi', 'ヂ': 'di', 'ヅ': 'du',

    'ゐ': 'wi', 'ゑ': 'we', 'を': 'wo',
    'ヰ': 'wi', 'ヱ': 'we', 'ヲ': 'wo'
    }

    NIHON_DIGRAPHS = {
        'しゃ': 'sya', 'しゅ': 'syu', 'しょ': 'syo',
        'シャ': 'sya', 'シュ': 'syu', 'ショ': 'syo',

        'じゃ': 'zya', 'じゅ': 'zyu', 'じょ': 'zyo',
        'ジャ': 'zya', 'ジュ': 'zyu', 'ジョ': 'zyo',

        'ちゃ': 'tya', 'ちゅ': 'tyu', 'ちょ': 'tyo',
        'チャ': 'tya', 'チュ': 'tyu', 'チョ': 'tyo',

        'ぢゃ': 'dya', 'ぢゅ': 'dyu', 'ぢょ': 'dyo',
        'ヂャ': 'dya', 'ヂュ': 'dyu', 'ヂョ': 'dyo'
    }

    KUNREI_MONOGRAPHS = {
        'し': 'si', 'ち': 'ti', 'つ': 'tu', 'ふ': 'hu', 'じ': 'zi', 'ぢ': 'zi',
        'シ': 'si', 'チ': 'ti', 'ツ': 'tu', 'フ': 'hu', 'ジ': 'zi', 'ヂ': 'zi'
    }

    KUNREI_DIGRAPHS = {
        'しゃ': 'sya', 'しゅ': 'syu', 'しょ': 'syo',
        'シャ': 'sya', 'シュ': 'syu', 'ショ': 'syo',

        'じゃ': 'zya', 'じゅ': 'zyu', 'じょ': 'zyo',
        'ジャ': 'zya','ジュ': 'zyu', 'ジョ': 'zyo',

        'ちゃ': 'tya', 'ちゅ': 'tyu', 'ちょ': 'tyo',
        'チャ': 'tya', 'チュ': 'tyu', 'チョ': 'tyo',

        'ぢゃ': 'zya', 'ぢゅ': 'zyu', 'ぢょ': 'zyo',
        'ヂャ': 'zya', 'ヂュ': 'zyu', 'ヂョ': 'zyo'
    }


    @staticmethod
    def hepburn(text, upcase=False, traditional=False):
        result_text = Converter.romanize(text, Converter.DIGRAPHS)
        result_text = Converter.romanize(result_text, Converter.MONOGRAPHS)

        # Double consonants: 促音
        result_text = result_text.replace('っc', 'tc').replace('ッc', 'tc')
        result_text = Converter.handle_double_consonants(result_text)

        # Syllabic n: 撥音
        if traditional:
            result_text = result_text.replace('n', 'm', 1)

        # Long vowels: 長音
        result_text = result_text.replace('oo', 'o').replace('ou', 'o').replace('uu', 'u')

        if upcase:
            result_text = result_text.upper()

        return result_text

    @staticmethod
    def nihon(text, upcase=False):
        # Ensure specific mappings for 'nihon' take precedence
        combined_mappings = {**Converter.MONOGRAPHS, **Converter.DIGRAPHS, **Converter.NIHON_MONOGRAPHS, **Converter.NIHON_DIGRAPHS}
        result_text = Converter.romanize(text, combined_mappings)
        result_text = Converter.handle_double_consonants(result_text)
        result_text = result_text.replace('oo', 'o').replace('ou', 'o').replace('uu', 'u')

        if upcase:
            result_text = result_text.upper()

        return result_text

    @staticmethod
    def kunrei(text, upcase=False):
        # Ensure specific mappings for 'kunrei' take precedence
        combined_mappings = {**Converter.MONOGRAPHS, **Converter.DIGRAPHS, **Converter.KUNREI_MONOGRAPHS, **Converter.KUNREI_DIGRAPHS}
        result_text = Converter.romanize(text, combined_mappings)
        result_text = Converter.handle_double_consonants(result_text)
        result_text = result_text.replace('oo', 'o').replace('ou', 'o').replace('uu', 'u')

        if upcase:
            result_text = result_text.upper()

        return result_text


    @staticmethod
    def romanize(text, chars):
        result_text = text
        for kana, romaji in chars.items():
            result_text = result_text.replace(kana, romaji)
        return result_text

    @staticmethod
    def handle_double_consonants(text):
        result_text = ''
        i = 0
        while i < len(text):
            if i + 1 < len(text) and text[i] in ['っ', 'ッ']:
                next_char = text[i + 1]
                if next_char in 'bcdfghjklmnpqrstvwxyz':  # Ensure the next character is a consonant
                    result_text += next_char * 2
                    i += 2  # Skip the small tsu and the next character that's been doubled
                    continue
            result_text += text[i]
            i += 1
        return result_text


def main():
    parser = argparse.ArgumentParser(description='Japanese Romanization')
    parser.add_argument('--input', type=str, help='Input file containing Kana text')
    parser.add_argument('--output', type=str, help='Output file for Romaji text')
    parser.add_argument('--method', type=str, choices=['hepburn', 'nihon', 'kunrei'], default='hepburn', help='Choose the romanization method: "hepburn", "nihon", or "kunrei"')
    parser.add_argument('--upcase', action='store_true', help='Return text in upper case')
    parser.add_argument('--traditional', action='store_true', help='Use traditional Hepburn rules')

    args = parser.parse_args()

    input_text = ''
    if args.input:
        with open(args.input, 'r', encoding='utf-8') as file:
            input_text = file.read()
    else:
        input_text = input()

    if args.method == 'hepburn':
        output_text = Converter.hepburn(input_text, args.upcase, args.traditional)
    elif args.method == 'nihon':
        output_text = Converter.nihon(input_text, args.upcase)
    elif args.method == 'kunrei':
        output_text = Converter.kunrei(input_text, args.upcase)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as file:
            file.write(output_text)
    else:
        print(output_text)


if __name__ == "__main__":
    main()
