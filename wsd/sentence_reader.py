
import json


class WSDFileReader:

    def __init__(self, json_file, preprocessor):
        self.preprocessor = preprocessor
        self.filename = json_file
        self.words_dict = dict()

        wsd_list = json.load(open(json_file))['wsd_list']

        for wsd in wsd_list:
            word = preprocessor.preprocess_word(wsd['word'])
            self.words_dict[word] = list()
            for sentence_obj in wsd['sentences']:
                bag_of_words = preprocessor.preprocess_sentence(sentence_obj['sentence'])
                self.words_dict[word].append((sentence_obj['sentence'], bag_of_words))
