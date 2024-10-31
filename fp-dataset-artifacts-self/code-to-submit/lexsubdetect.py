# detect subsequence and lexical overlap
import json
from collections import Counter
from string import punctuation

def convertToExcel(fstr, foutstr, writePairs=False):
    fout = open(foutstr, 'w')
    with open(fstr) as jsonFile:
        jsonList = list(jsonFile)
        for line in jsonList:
            lexical = False
            subsequence = False

            lineDict = json.loads(line)
            premise = lineDict['premise']
            hypothesis = lineDict['hypothesis']

            # try to find lexical overlap
            premise_list = premise.lower().translate(str.maketrans('','',punctuation)).split()
            hypothesis_list = hypothesis.lower().translate(str.maketrans('','',punctuation)).split()
            if((Counter(premise_list) & Counter(hypothesis_list)).total() == Counter(hypothesis_list).total()):
                lexical = True

                # try to find subsequence (ordered)
                if (hypothesis in premise):
                    subsequence = True

            if(writePairs == True):
                s = "{}\t{}\t{}\t{}\t{}\n".format(premise, hypothesis, lineDict['label'], lexical, subsequence)
            else:
                s = "{}\t{}\n".format(lexical, subsequence)

            fout.write(s)
           
    fout.close()

#fbreak = './jsonl/eval_predictions_break.jsonl'
#fbreakout = './tsv/breakdetect.tsv'
#fdev = './jsonl/eval_predictions_dev.jsonl'
#fdevout = './tsv/devdetect.tsv'
#fmcc = './jsonl/eval_predictions_mccoy.jsonl'
#fmccout = './tsv/mccoy.tsv'
fsnlitrain = './jsonl/snli_only_train.jsonl'
fsnlitrainout = './tsv/snli_only_train_lexsubs.tsv'

convertToExcel(fsnlitrain, fsnlitrainout, True) # also write premise and hypoth to file
#convertToExcel(fbreak, fbreakout)
#convertToExcel(fdev, fdevout)
#convertToExcel(fmcc, fmccout)


