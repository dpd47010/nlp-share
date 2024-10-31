
import json
'''
Instructions from run.py
# You need to format the dataset appropriately. For SNLI, you can prepare a file with each line containing one
# example as follows:
# {"premise": "Two women are embracing.", "hypothesis": "The sisters are hugging.", "label": 1}
# contra = 2
# net = 1
# entail = 0
'''

'''
From https://github.com/BIU-NLP/Breaking_NLI
sentence1: The premise sentence.

sentence2: The hypothesis sentence, which is the same as the premise except for one word/phrase that was replaced.

annotator_labels: These are all of the individual labels from the three annotators. 

gold_label: This is the label chosen by the majority of annotators. 

pairID: A unique identifier for each sentence1--sentence2 pair.

category: This category sematically groups the replaced words.
'''
def convertToExcelBreak(fstr, foutstr):
    fout = open(foutstr, 'w')
    with open(fstr) as jsonFile:
        jsonList = list(jsonFile)
        for line in jsonList:
            lineDict = json.loads(line)
            s = "{}\n".format(lineDict['category'])
            fout.write(s)
    fout.close()

def convertToExcelMccoy(fstr, foutstr):
    fout = open(foutstr, 'w')
    with open(fstr) as jsonFile:
        jsonList = list(jsonFile)
        for line in jsonList:
            lineDict = json.loads(line)
            s = "{}\t{}\n".format(lineDict['heuristic'], lineDict['subcase'])
            fout.write(s)
    fout.close()

fbreak = './Breaking_NLI-master/data/dataset.jsonl'
fbreakout = './tsv/morebreak.tsv'
fmcc = './hans-master/heuristics_evaluation_set.jsonl'
fmccout = './tsv/moremccoy.tsv'

convertToExcelBreak(fbreak, fbreakout)
convertToExcelMccoy(fmcc, fmccout)


