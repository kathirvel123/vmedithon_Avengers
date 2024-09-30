import requests
def foodcabs(x):
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(x)
    response = requests.get(api_url, headers={'X-Api-Key': '8XXHwIQiSyfYjszangWRiA==7aNqe2hm24lZ43xN'})
    if response.status_code == requests.codes.ok:
        li=eval(response.text)
        for i in li:
            return i
    else:
        return {}
def heartrate(rate):
    return rate-72
def estimated_blood_sugar(carbohydrate,rate,exer,previousblood):
    return previousblood+(carbohydrate*2)-(heartrate(rate)*0.5)-(exer*2)
def insulin_needed(cur,tar,isf):
    return (cur-tar)/isf
