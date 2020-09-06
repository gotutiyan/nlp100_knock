def program_30():
    sentences = []
    with open('neko.txt.mecab') as fp:
        sentence = []
        for line in fp:
            morph_dic = morph_to_dict(line)
            sentence.append(morph_dic)
            if line[0]=='。':
                sentences.append(sentence)
                sentence = []
        return sentences
            
            
def morph_to_dict(morph):
    dic = {}
    morph = morph.split('\t')
    dic['surface'] = morph[0]
    if len(morph) >= 2:
        if len(morph[1].split(',')) >=6:
            dic['base'] = morph[1].split(',')[6]
        dic['pos'] = morph[1].split(',')[0]
        dic['pos1'] = morph[1].split(',')[1]
    return dic

# Number 30
sentences = program_30()

# Number 32
base_set = set()
for sentence in sentences:
    for morph in sentence:
        if morph['pos'] == '動詞':
            base_set.add(morph['base'])

print(base_set)
"""
{'嵌る', '描き出す', '取り払う',
.... '近寄る', '擦り付ける', '愛する', '舞い戻る'}
"""




    

