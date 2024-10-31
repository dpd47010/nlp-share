# detect lexical overlap threshold
import json
from collections import Counter
from string import punctuation

def convertToExcel(fstr, foutstr):
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
            threshold = 0
            if(((Counter(premise_list) & Counter(hypothesis_list)).total()) / (Counter(hypothesis_list).total())
                >= threshold):
                lexical = True

            s = "{}\n".format(lexical)
            fout.write(s)
           
    fout.close()

#fbreak = './jsonl/eval_predictions_break.jsonl'
#fbreakout = './tsv/breakdetect.tsv'
fdev = './jsonl/eval_predictions_dev.jsonl'
fdevout = './tsv/devdetectthreshold.25.tsv'
#fmcc = './jsonl/eval_predictions_mccoy.jsonl'
#fmccout = './tsv/mccoy.tsv'

#convertToExcel(fbreak, fbreakout)
convertToExcel(fdev, fdevout)
#convertToExcel(fmcc, fmccout)


