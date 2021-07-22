from scipy import spatial
import pickle
import numpy as np
import math
import pandas as pd


def load(path_reps):
    with open(path_reps, 'rb') as h:
        df = pickle.load(h)
    return df.set_index('id').to_dict('index')



class Recommend():
    def __init__(self, n, w_downloads=0.6, w_avg_rating=0.1, w_total_rating=0.3, fixed=True):
        self.n = n
        self.data = load('api/app/representations/relevant_with_emebeddings.pkl')
        self.similarity = lambda x,y: 1 - spatial.distance.cosine(x, y)
        self.w_downloads = w_downloads
        self.w_avg_rating = w_avg_rating
        self.w_total_rating = w_total_rating
        self.fixed = fixed
        
    def __call__(self, current_app):
        
        results = {appid: 0 for appid in self.data if appid != current_app}
        
        app_name_rep = self.data[current_app]['NameEmbeddingsRoBERTa']
        app_desc_rep = self.data[current_app]['DescEmbeddingsRoBERTa']
        
        for app in results:
            results[app] = self.similarity(app_name_rep, self.data[app]['NameEmbeddingsRoBERTa']) + self.similarity(app_desc_rep, self.data[app]['DescEmbeddingsRoBERTa'])
        
        most_similar = sorted(results.items(), key=lambda pair: pair[1], reverse=True)[:30]
        
        relevant_ids = [ms[0] for ms in most_similar]
        
        prob = self.get_relevancy_judgements(relevant_ids)
        
      
        recomendations = np.random.choice(relevant_ids, size=self.n, replace=False, p=prob)
        
        result = []

        if not self.fixed:
            for app_id in recomendations:
                result.append(self.data[app_id]['title'])
                #print(app_to_prob_map[app_id])
                
        else:
            highest_probability = [(app, prob[idx]) for idx, app in enumerate(relevant_ids)]
            highest_probability = sorted(highest_probability, key=lambda pair: pair[1], reverse=True)[:self.n]
            for pair in highest_probability:
                result.append(self.data[pair[0]]['title'])

        return result


    

    def get_relevancy_judgements(self, ids):
        judgements = []
        max_downloads = math.log10(383534142)
        min_downloads = math.log10(1010)
        max_ratings = 50863
        min_ratings = 0
        
        for app_id in ids:
            rating_score = self.data[app_id]['avg_rating']/5
            total_rating_score = (self.data[app_id]['total_ratings'] - min_ratings)/(max_ratings-min_ratings)
            downloads_score = (math.log10(self.data[app_id]['downloads']) - min_downloads)/(max_downloads-min_downloads)
            
            final_score = self.w_avg_rating * rating_score + self.w_total_rating * total_rating_score + self.w_downloads * downloads_score
            
            judgements.append(final_score)
            

        probs = np.array(judgements)
        probs = np.square(probs)
        probs =  probs / probs.sum()
        
        return probs
            
recommender = Recommend(n = 7, w_downloads = 0.6, w_avg_rating = 0.1, w_total_rating = 0.3, fixed=True)

            