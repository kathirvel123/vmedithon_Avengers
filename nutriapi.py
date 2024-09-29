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
