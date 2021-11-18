import sentencepiece as spm
import MeCab
import pandas as pd

def korean_token_src(datatxt, _mecab=False):
    m = MeCab.Tagger()
    delete_tag = ['BOS/EOS', 'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JX', 'JC']

    def del_post_pos(sentence):
        tokens = sentence.split()

        dict_list = []

        for token in tokens:
            m.parse('')
            node = m.parseToNode(token)
            word_list = []
            morph_list = []

            while node:
                morphs = node.feature.split(',')
                word_list.append(node.surface)
                morph_list.append(morphs[0])
                node = node.next

            dict_list.append(dict(zip(word_list, morph_list)))

        for dic in dict_list:
            for key in list(dic.keys()):
                if dic[key] in delete_tag:
                    del dic[key]

        combine_word = [''.join(list(dic.keys())) for dic in dict_list]
        result = ' '.join(combine_word)

        return result

    data = open(datatxt,'r', encoding='utf-8')

    with open("data/kor_src.txt", "w", encoding='utf-8') as f:
        for row in data:
            if _mecab:
                # delete tag
                f.write(del_post_pos(row))
            else:
                # only sentencepicec
                f.write(row)
            f.write('\n')

    spm.SentencePieceTrainer.Train(
        '--input=data/kor_src.txt \
        --model_prefix=data/korean_tok_src \
        --vocab_size=100000 \
        --hard_vocab_limit=false'
    )
        
def korean_token_tgt(datatxt, _mecab=False):
    m = MeCab.Tagger()
    delete_tag = ['BOS/EOS', 'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JX', 'JC']

    def del_post_pos(sentence):
        tokens = sentence.split()

        dict_list = []

        for token in tokens:
            m.parse('')
            node = m.parseToNode(token)
            word_list = []
            morph_list = []

            while node:
                morphs = node.feature.split(',')
                word_list.append(node.surface)
                morph_list.append(morphs[0])
                node = node.next

            dict_list.append(dict(zip(word_list, morph_list)))

        for dic in dict_list:
            for key in list(dic.keys()):
                if dic[key] in delete_tag:
                    del dic[key]

        combine_word = [''.join(list(dic.keys())) for dic in dict_list]
        result = ' '.join(combine_word)

        return result

    data = open(datatxt,'r', encoding='utf-8')

    with open("data/kor_tgt.txt", "w", encoding='utf-8') as f:
        for row in data:
            if _mecab:
                # delete tag
                f.write(del_post_pos(row))
            else:
                # only sentencepicec
                f.write(row)
            f.write('\n')

    spm.SentencePieceTrainer.Train(
        '--input=data/kor_tgt.txt \
        --model_prefix=data/korean_tok_tgt \
        --vocab_size=100000 \
        --hard_vocab_limit=false'
    )