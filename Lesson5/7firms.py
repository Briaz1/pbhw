from statistics import mean
from json import dump

analytics = [{}, {}]
with open('firms.txt.txt', 'r', encoding='utf-8') as firms:
    for firm in firms:
        analytics[0][firm.split()[0]] = int(firm.split()[2]) - int(firm.split()[3])
    analytics[1]['Average profit'] = mean([el for el in analytics[0].values() if el > 0])
print(analytics)
with open('firms_json.json', 'w', encoding='utf-8') as firms_json:
    dump(analytics, firms_json, indent=2, ensure_ascii=False)
