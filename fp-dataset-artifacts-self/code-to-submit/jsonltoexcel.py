
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

def convertToExcel(fstr, foutstr):
    fout = open(foutstr, 'w')
    with open(fstr) as jsonFile:
        jsonList = list(jsonFile)
        for line in jsonList:
            lineDict = json.loads(line)
            p0 = lineDict['predicted_scores'][0]
            p1 = lineDict['predicted_scores'][1]
            p2 = lineDict['predicted_scores'][2]
            s = "{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(lineDict['premise'], lineDict['hypothesis'], p0, p1, p2, lineDict['label'], lineDict['predicted_label'])
            fout.write(s)
    fout.close()


'''
original set
fbreak = './jsonl/eval_predictions_break.jsonl'
fbreakout = './tsv/break.tsv'
fdev = './jsonl/eval_predictions_dev.jsonl'
fdevout = './tsv/dev.tsv'
fmcc = './jsonl/eval_predictions_mccoy.jsonl'
fmccout = './tsv/mccoy.tsv'

convertToExcel(fbreak, fbreakout)
convertToExcel(fdev, fdevout)
convertToExcel(fmcc, fmccout)
'''

'''
# tatf 5k set
fbreak = './jsonl/eval_predictions_break_tatf5k.jsonl'
fbreakout = './tsv/break_tatf5k.tsv'
fdev = './jsonl/eval_predictions_dev_tatf5k.jsonl'
fdevout = './tsv/dev_tatf5k.tsv'
fmcc = './jsonl/eval_predictions_mccoy_tatf5k.jsonl'
fmccout = './tsv/mccoy_tatf5k.tsv'

convertToExcel(fbreak, fbreakout)
convertToExcel(fdev, fdevout)
convertToExcel(fmcc, fmccout)
'''

'''
# tatf 50k set
fbreak = './jsonl/eval_predictions_break_tatf50k.jsonl'
fbreakout = './tsv/break_tatf50k.tsv'
fdev = './jsonl/eval_predictions_dev_tatf50k.jsonl'
fdevout = './tsv/dev_tatf50k.tsv'
fmcc = './jsonl/eval_predictions_mccoy_tatf50k.jsonl'
fmccout = './tsv/mccoy_tatf50k.tsv'
'''

'''
# combined set
fbreak = './trained_model_combined_try2/eval_output_break_combined/eval_predictions.jsonl'
fbreakout = './tsv/break_combined.tsv'
fdev = './trained_model_combined_try2/eval_output_snli_combined/eval_predictions.jsonl'
fdevout = './tsv/dev_combined.tsv'
fmcc = './trained_model_combined_try2/eval_output_mccoylimited_combined/eval_predictions.jsonl'
fmccout = './tsv/mccoylimited_combined.tsv'
'''

# baseline on 40% cut of mccoy
f40 = './eval_output_baseline_on_40mccoy/eval_predictions.jsonl'
f40out = './tsv/baseline_40.tsv'
convertToExcel(f40, f40out)

'''
convertToExcel(fbreak, fbreakout)
convertToExcel(fdev, fdevout)
convertToExcel(fmcc, fmccout)
'''