from run_server_phraseSearch import app

if __name__ == "__main__":
    logger = CreateLogger()

    datasets = load_datasets()

    model_bert, _ = load_model('BERT:bert-base-uncased')
    model_phrasebert, _ = load_model('PhraseBERT:phrase-bert-qa')
    model_longformer, tokenizer = load_model('Longformer:allenai/longformer-base-4096')

    sent_tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')    
    app.run()


