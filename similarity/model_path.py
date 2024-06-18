MODEL_PATH = {
    #"PhraseBERT": "whaleloops/phrase-bert",
    # "DensePhrases": "princeton-nlp/densephrases-multi-query-multi",
    #"BERT": "bert-base-uncased",
    #"SpanBERT-base": "SpanBERT/spanbert-base-cased",
    #"SpanBERT-large": "SpanBERT/spanbert-large-cased",
    #"SentenceBERT": "bert-base-nli-stsb-mean-tokens",
    #"SimCSE": "princeton-nlp/sup-simcse-bert-base-uncased",
    #"E5": "intfloat/e5-base-v2"
    #"EMistral": "intfloat/e5-mistral-7b-instruct"  #not working
    #"Mistral": "mistralai/Mistral-7B-v0.1" #same issue as the previous one
    #"Xlnet": "xlnet/xlnet-base-cased" #OverflowError: can't convert negative int to unsigned
    #"Albert": "albert/albert-base-v2" #many many phrases are not found! accuracy is really low
    #"T511B": "google-t5/t5-11b" #too large
    #"Distilbert": "distilbert/distilbert-base-uncased"  #GOOD
    #"DistilbertFinetuned": "distilbert/distilbert-base-uncased-finetuned-sst-2-english" #62 accuracy
    #"DistilRoberta": "distilbert/distilroberta-base"
    #"DistilbertQA": "distilbert/distilbert-base-cased-distilled-squad"
    #"LLM": "meta-llama/Meta-Llama-3-8B" #too big
    #"Roberta": "FacebookAI/roberta-base" #too many phrase not found
    #"XLMRoberta": "FacebookAI/xlm-roberta-base" #too many phrase not found bt still gives 58
    #"RobertaEnglish": "FacebookAI/xlm-roberta-large-finetuned-conll03-english" #too many
}


