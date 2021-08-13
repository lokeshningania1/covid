
from django.http import HttpResponse
from django.shortcuts import render
import requests

def homes(request):
    return HttpResponse("hii")



def home(request):
        r = requests.get('https://api.covid19india.org/v4/min/data.min.json')
        result = r.json()
        print(result.keys())
        stateabbs = {'AN':'Andaman and Nicobar Islands', 'AP':'Andhra Pradesh', 'AR':'Arunachal Pradesh', 'AS':'Assam', 'BR':'Bihar', 'CH':'Chandigarh', 'CT':'Chattisgarh', 'DL':'Delhi', 'DN':'Daman & Diu', 'GA':'Goa', 'GJ':'Gujarat', 'HP':'Himachal Pradesh', 'HR':'Haryana', 'JH':'Jharkhand', 'JK':'Jammu and Kashmir', 'KA':'Karnataka', 'KL':'Kerala', 'LA':'Ladakh', 'LD':'Lakshadweep', 'MH':'Maharashtra', 'ML':'Meghalaya', 'MN':'Manipur', 'MP':'Madhya Pradesh', 'MZ':'Mizoram', 'NL':'Nagaland', 'OR':'Orissa', 'PB':'Punjab', 'PY':'Pondicherry', 'RJ':'Rajasthan', 'SK':'Sikkim', 'TG':'Telangana', 'TN':'Tamil Nadu', 'TR':'Tripura', 'TT':'India', 'UP':'Uttar Pradesh', 'UT':'Uttarakhand', 'WB':'West Bengal'}
        states = []
        for state in result:
            newdict = result[state]['total']
            newdict["name"] = stateabbs[state]
            newdict["nameabb"] = state
            if state=='':
                newdict["name"]= 'India'
            states.append(newdict)
        params={'states':states}
        return render(request,'home.html',params)

def districts(request , sname):
        r = requests.get('https://api.covid19india.org/v4/min/data.min.json')
        result = r.json()
        districtsdata = []
        dists = result[sname]['districts']
        for district in dists:
            districtdict = result[sname]['districts'][district]['total']
            districtdict['name']=district
            districtsdata.append(districtdict)
        params = {'districts':districtsdata}
        return render(request,'district.html',params)
    

