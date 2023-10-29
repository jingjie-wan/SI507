import requests
import json
#The cache contains three dictionary items: random points, census, and income. Each value is a dictionary containing each district.
#step 1
response = requests.get("https://dsl.richmond.edu/panorama/redlining/static/downloads/geojson/MIDetroit1939.geojson")
json_str = response.text
json_dict = json.loads(json_str)
RedliningData = json_dict['features'] #a list
#step 2
class DetroitDistrict:
    color = {'A': 'darkgreen', 'B': 'cornflowerblue', 'C': 'gold', 'D': 'maroon'}
    def __init__(self, district, name):
        self.Coordinates = district['geometry']['coordinates'][0][0]
        self.HolcGrade = district['properties']['holc_grade']
        self.HolcColor = DetroitDistrict.color[self.HolcGrade]
        self.name = name #index
        self.Qualitative_Description = district['properties']['area_description_data']['8']
        self.RandomLat = None
        self.RandomLong = None
        self.Median_Income = None
        self.CensusTract = None
Districts = [DetroitDistrict(RedliningData[i], i) for i in range(len(RedliningData))]
#step 3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
fig, ax = plt.subplots()
for district in Districts: # what kind of for loop makes sense?
    ax.add_patch(plt.Polygon(district.Coordinates, facecolor=district.HolcColor, edgecolor = 'black')) # add arguments here
    ax.autoscale()
    plt.rcParams["figure.figsize"] = (15,15)
plt.show()
#step 7
CACHE_FILENAME = "cache.json"

def open_cache():
    ''' opens the cache file if it exists and loads the JSON into
    a dictionary, which it then returns.
    if the cache file doesn't exist, creates a new cache dictionary
    Parameters
    ----------
    None
    Returns
    -------
    The opened cache
    '''
    try:
        cache_file = open(CACHE_FILENAME, 'r')
        cache_contents = cache_file.read()
        cache_dict = json.loads(cache_contents)
        cache_file.close()
    except:
        cache_dict = {'random':{}, 'census':{}, 'income':{}}
    return cache_dict

def save_cache(cache_dict):
    ''' saves the current state of the cache to disk
    Parameters
    ----------
    cache_dict: dict
        The dictionary to save
    Returns
    -------
    None
    '''
    dumped_json_cache = json.dumps(cache_dict)
    fw = open(CACHE_FILENAME,"w")
    fw.write(dumped_json_cache)
    fw.close() 
    
FIB_CACHE = open_cache() ###

#step4
import random as random
from matplotlib.path import Path
import numpy as np
random.seed(17)

xgrid = np.arange(-83.5, -82.8, .004)
ygrid = np.arange(42.1, 42.6, .004)
xmesh, ymesh = np.meshgrid(xgrid, ygrid) #combine xgrid and y grid into an array of two elements

points = np.vstack((xmesh.flatten(), ymesh.flatten())).T #transpose the array into an array of points

for j in Districts:
    name = str(j.name)
    if name in FIB_CACHE['random']:
        point = FIB_CACHE['random'][name]
    else:
        p = Path(j.Coordinates)
        grid = p.contains_points(points) #return an array of boolean values
        print(j, " : ", points[random.choice(np.where(grid)[0])]) #the first one in coordinates that contains points
        point = list(points[random.choice(np.where(grid)[0])])
        FIB_CACHE['random'][name] = point
        save_cache(FIB_CACHE)
        point = FIB_CACHE['random'][name]
        
    j.RandomLong = point[0]
    j.RandomLat = point[1]
    
    
#step5
for district in Districts:
    name = str(district.name)
    if name in FIB_CACHE['census']:
        census_tract = FIB_CACHE['census'][name]
    else:
        lat = str(district.RandomLat)
        lon = str(district.RandomLong)
        census = requests.get("https://geo.fcc.gov/api/census/area?lat=" + lat + "&lon=" + lon + "&censusYear=2010&format=json")
        census_str = census.text
        census_dict = json.loads(census_str)
        census_tract = census_dict['results'][0]['block_fips'][5:11]
        FIB_CACHE['census'][name] = census_tract
        save_cache(FIB_CACHE)
        census_tract = FIB_CACHE['census'][name]
    district.CensusTract = census_tract
    
#step6
if FIB_CACHE['income'] != {}:
    for district in Districts:
        name = str(district.name)
        medium_income = FIB_CACHE['income'][name]
        district.Median_Income = medium_income
else:  
    income = requests.get("https://api.census.gov/data/2018/acs/acs5?get=B19013_001E&for=tract:*&in=state:26&key=44011c132f4e6c44649f0c0f92114f7ae5ba1393")
    income_str = income.text
    income_dict = json.loads(income_str)
    for district in Districts:
        census = district.CensusTract
        name = str(district.name)
        for lst in income_dict[1:]:
            if census == lst[3]: 
                medium_income = lst[0]
                FIB_CACHE['income'][name] = medium_income
                save_cache(FIB_CACHE)
                medium_income = FIB_CACHE['income'][name]
                district.Median_Income = medium_income
                break
#step 8
income_A = []
income_B = []
income_C = []
income_D = []
for district in Districts:
    grade = district.HolcGrade
    if grade == 'A': income_A.append(int(district.Median_Income))
    elif grade == 'B': income_B.append(int(district.Median_Income))
    elif grade == 'C': income_C.append(int(district.Median_Income))
    elif grade == 'D': income_D.append(int(district.Median_Income))
A_mean_income = np.mean(income_A)
A_median_income = np.median(income_A)
B_mean_income = np.mean(income_B)
B_median_income = np.median(income_B)
C_mean_income = np.mean(income_C)
C_median_income = np.median(income_C)
D_mean_income = np.mean(income_D)
D_median_income = np.median(income_D)
print('A_mean_income: ', A_mean_income)
print('A_median_income: ', A_median_income)
print('B_mean_income: ', B_mean_income)
print('B_median_income: ', B_median_income)
print('C_mean_income: ', C_mean_income)
print('C_median_income: ', C_median_income)
print('D_mean_income: ', D_mean_income)
print('D_median_income: ', D_median_income)
#step 9
stopwords = {'&',
 "'d",
 "'ll",
 "'m",
 "'re",
 "'s",
 "'ve",
 '*See',
 '-',
 'A',
 'All',
 'Area',
 'Descriptions.',
 'On',
 'The',
 'There',
 'This',
 'a',
 'about',
 'above',
 'across',
 'after',
 'afterwards',
 'again',
 'against',
 'all',
 'almost',
 'alone',
 'along',
 'already',
 'also',
 'although',
 'always',
 'am',
 'among',
 'amongst',
 'amount',
 'an',
 'and',
 'another',
 'any',
 'anyhow',
 'anyone',
 'anything',
 'anyway',
 'anywhere',
 'are',
 'area',
 'area.',
 'around',
 'as',
 'at',
 'back',
 'be',
 'became',
 'because',
 'become',
 'becomes',
 'becoming',
 'been',
 'before',
 'beforehand',
 'behind',
 'being',
 'below',
 'beside',
 'besides',
 'between',
 'beyond',
 'both',
 'bottom',
 'but',
 'by',
 'ca',
 'call',
 'can',
 'cannot',
 'could',
 'did',
 'do',
 'does',
 'doing',
 'done',
 'down',
 'due',
 'during',
 'each',
 'eight',
 'either',
 'eleven',
 'else',
 'elsewhere',
 'empty',
 'enough',
 'even',
 'ever',
 'every',
 'everyone',
 'everything',
 'everywhere',
 'except',
 'explanation',
 'few',
 'fifteen',
 'fifty',
 'first',
 'five',
 'for',
 'former',
 'formerly',
 'forty',
 'four',
 'from',
 'front',
 'full',
 'further',
 'get',
 'give',
 'go',
 'grade.',
 'had',
 'has',
 'have',
 'he',
 'hence',
 'her',
 'here',
 'hereafter',
 'hereby',
 'herein',
 'hereupon',
 'hers',
 'herself',
 'him',
 'himself',
 'his',
 'houses',
 'how',
 'however',
 'hundred',
 'i',
 'if',
 'in',
 'indeed',
 'into',
 'is',
 'it',
 'its',
 'itself',
 'just',
 'keep',
 'last',
 'latter',
 'latterly',
 'least',
 'less',
 'made',
 'make',
 'many',
 'may',
 'me',
 'meanwhile',
 'might',
 'mine',
 'more',
 'moreover',
 'most',
 'mostly',
 'move',
 'much',
 'must',
 'my',
 'myself',
 "n't",
 'name',
 'namely',
 'neighborhood',
 'neither',
 'never',
 'nevertheless',
 'next',
 'nine',
 'no',
 'nobody',
 'none',
 'noone',
 'nor',
 'not',
 'nothing',
 'now',
 'nowhere',
 'n‘t',
 'n’t',
 'of',
 'off',
 'often',
 'on',
 'once',
 'one',
 'only',
 'onto',
 'or',
 'other',
 'others',
 'otherwise',
 'our',
 'ours',
 'ourselves',
 'out',
 'over',
 'own',
 'part',
 'per',
 'perhaps',
 'please',
 'put',
 'quite',
 'rather',
 're',
 'really',
 'regarding',
 'same',
 'say',
 'section',
 'see',
 'seem',
 'seemed',
 'seeming',
 'seems',
 'serious',
 'several',
 'she',
 'sheet',
 'should',
 'show',
 'side',
 'since',
 'six',
 'sixty',
 'so',
 'some',
 'somehow',
 'someone',
 'something',
 'sometime',
 'sometimes',
 'somewhere',
 'still',
 'such',
 'take',
 'ten',
 'than',
 'that',
 'the',
 'their',
 'them',
 'themselves',
 'then',
 'thence',
 'there',
 'thereafter',
 'thereby',
 'therefore',
 'therein',
 'thereupon',
 'these',
 'they',
 'third',
 'this',
 'those',
 'though',
 'three',
 'through',
 'throughout',
 'thru',
 'thus',
 'to',
 'together',
 'too',
 'top',
 'toward',
 'towards',
 'twelve',
 'twenty',
 'two',
 'under',
 'unless',
 'until',
 'up',
 'upon',
 'us',
 'used',
 'using',
 'various',
 'very',
 'via',
 'was',
 'we',
 'well',
 'were',
 'what',
 'whatever',
 'when',
 'whence',
 'whenever',
 'where',
 'whereafter',
 'whereas',
 'whereby',
 'wherein',
 'whereupon',
 'wherever',
 'whether',
 'which',
 'while',
 'whither',
 'who',
 'whoever',
 'whole',
 'whom',
 'whose',
 'why',
 'will',
 'with',
 'within',
 'without',
 'would',
 'yet',
 'you',
 'your',
 'yours',
 'yourself',
 'yourselves',
 '‘d',
 '‘ll',
 '‘m',
 '‘re',
 '‘s',
 '‘ve',
 '’d',
 '’ll',
 '’m',
 '’re',
 '’s',
 '’ve'}
string_A = []
string_B = []
string_C = []
string_D = []
for district in Districts:
    grade = district.HolcGrade
    word_list = [word for word in district.Qualitative_Description.split() if not word in stopwords]
    if grade == 'A': string_A += word_list
    elif grade == 'B': string_B += word_list
    elif grade == 'C': string_C += word_list
    elif grade == 'D': string_D += word_list

from collections import Counter
collection_A = Counter(string_A)
collection_B = Counter(string_B)
collection_C = Counter(string_C)
collection_D = Counter(string_D)
A_10_Most_Common = [word for word, cnt in collection_A.most_common(10)]
B_10_Most_Common = [word for word, cnt in collection_B.most_common(10)]
C_10_Most_Common = [word for word, cnt in collection_C.most_common(10)]
D_10_Most_Common = [word for word, cnt in collection_D.most_common(10)]
print(A_10_Most_Common)
print(B_10_Most_Common)
print(C_10_Most_Common)
print(D_10_Most_Common)