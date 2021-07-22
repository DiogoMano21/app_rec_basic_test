from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from rec import Recommend


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

recommender = Recommend(n = 7, w_downloads = 0.6, w_avg_rating = 0.1, w_total_rating = 0.3, fixed=True)

##############
# ENDPOINTS
##############

@app.route('/recommend')
@cross_origin()
def recommend():
    app_id = request.args.get('app_id', type = int)

    recommended_apps = recommender(app_id)

    return jsonify({'status': 'ok', 'data': recommended_apps})


##############
# START
##############

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")



##############
# EXAMPLE IDS
##############

## RELEVANT APPLICATIONS

#facebook = 56965434
#twitter = 56490993
#netflix = 43216914
#free_fire = 56681891
#pokemon_go = 56860539
#dropbox = 56960002
#spotify = 56825681
#outlook = 56290023
#hbo = 56956360
#mi_fit = 56732830
#shazam = 56576893
#candy_crush = 56972423
#samsung_galery = 50320431
#avast = 55053460
#facebook_lite = 56965397

## NOT SO RELEVANT APPLICATIONS

#lang = 56659061 # "learn 33 languages free - mondly"
#chat = 56609880 # chat application
#screen_mirror = 53354567 # "apowermirror - screen mirroring for pc/tv/phone"