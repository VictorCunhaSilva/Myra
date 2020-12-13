from itemadapter import ItemAdapter
import pandas as pd
from pandas import DataFrame
from datetime import datetime

class MyratestPipeline:
    def process_item(self, item, spider):
        
        saved_as = self.save_text(str(item['text']))
        
        item_dictionary = {'Author': [str(item['author'])],
        'Tags': [str(item['tag'])],
        'Page': [str(item['page'])],
        'Rule': [str(item['rule'])],
        'TextFile': [saved_as]
        }
        df = pd.DataFrame.from_dict(item_dictionary, orient='columns')
        df.to_csv("data.csv",sep=';',encoding='utf-8-sig',mode='a',header=False)
        #df = DataFrame(item_dictionary, columns= ['Author', 'Tags', 'Page', 'Rule', 'TextFile'])
        return item

        
    def save_text(self,text):
        #Salva texto em .txt
        file_name = 'crawl' + str(datetime.now()) + '.txt'
        f = open(file_name, "w")
        f.write(text)
        f.close()
        return file_name