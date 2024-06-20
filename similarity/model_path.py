MODEL_PATH = {
    #"PhraseBERT": "whaleloops/phrase-bert",
    # "DensePhrases": "princeton-nlp/densephrases-multi-query-multi",
    #"BERT": "bert-base-uncased",
    #"SpanBERT-base": "SpanBERT/spanbert-base-cased",
    #"SpanBERT-large": "SpanBERT/spanbert-large-cased",
    #"SentenceBERT": "bert-base-nli-stsb-mean-tokens",
    #"SimCSE": "princeton-nlp/sup-simcse-bert-base-uncased",
    #"E5": "intfloat/e5-base-v2"
    #"E5Large": "intfloat/e5-large-v2" #accuracy 62
    #"E5LargeMultilingual": "intfloat/multilingual-e5-large-instruct" #tooo many, still 61
    #"EMistral": "intfloat/e5-mistral-7b-instruct"  #not working
    #"Mistral": "mistralai/Mistral-7B-v0.1" #same issue as the previous one
    #"Xlnet": "xlnet/xlnet-base-cased" #OverflowError: can't convert negative int to unsigned
    #"Albert": "albert/albert-base-v2" #many many phrases are not found! accuracy is really low
    #"T511B": "google-t5/t5-11b" #too large
    #"Distilbert": "distilbert/distilbert-base-uncased"  #GOOD
    #"DistilbertFinetuned": "distilbert/distilbert-base-uncased-finetuned-sst-2-english" #62 accuracy
    #"DistilRoberta": "distilbert/distilroberta-base"
    #"DistilbertQA": "distilbert/distilbert-base-cased-distilled-squad"
    #"DistilbertGPT": "google-t5/t5-large" #error not enough values to unpack
    #"LLM": "meta-llama/Meta-Llama-3-8B" #too big
    #"Roberta": "FacebookAI/roberta-base" #too many phrase not found
    #"XLMRoberta": "FacebookAI/xlm-roberta-base" #too many phrase not found bt still gives 58
    #"RobertaEnglish": "FacebookAI/xlm-roberta-large-finetuned-conll03-english" #too many phrase not found
    #"StructBert": "bayartsogt/structbert-large" #59 accuracy
    #"Canine": "google/canine-c" #50 accuracy
    #"BigBird": "google/bigbird-roberta-base" #61 accuracy too many phrases not found
    #"BigBirdLarge": "google/bigbird-roberta-large" #59 too too too many phrases
    #"Longformer": "allenai/longformer-base-4096" #too too too too too too too too
    #"Electra": "google/electra-base-discriminator" #61 accuracy
    #"T5": "google-t5/t5-large" #tooo many, error dise last e (not many values to unpack)
    #"SentenceSimilarity": "annakotarba/sentence-similarity" #too many, 55 accuracy
    #"Luke": "studio-ousia/luke-base" #too many, 55
    #"sbert": "l3cube-pune/indic-sentence-similarity-sbert" #58 accuracy
    #"miniLM": "sentence-transformers/all-MiniLM-L6-v2" #58 accuracy
    #"Mpnet": "sentence-transformers/all-mpnet-base-v2" #64
    #"MpnetV1": "sentence-transformers/all-mpnet-base-v1" #65
    #"EmbedMistral": "Linq-AI-Research/Linq-Embed-Mistral" #run hoy nay
    "Labse": "sentence-transformers/LaBSE"

}
