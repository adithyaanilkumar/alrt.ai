import requests
import urllib.parse as urlparse
from urllib.parse import urlencode

params = {
    "id": "32423",
    "company_name": "Bharat Petroleum Corporation Limited",
    "common_name": "Bharat Petroleum",
    "public": True,
    "ticker": "BPCL",
    "source": ["google_news", "gdelt"],
    "date_from": "2018-12-25T05:37:07Z",
    "date_to": "2019-12-25T05:37:07Z",
    "storage_bucket": "alrt-ai-ps"
}


def clean(header):
    if "(" in header:
        return header.split(" (")[0]
    elif "llc" in header.lower():
        return header.split(" llc")[0]
    elif "ltd" in header.lower():
        return header.split(" ltd")[0]
    elif "co" in header.lower():
        return header.split(" co")[0]
    return header


def create_url(url, params):
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)

    url_parts[4] = urlencode(query)

    url = urlparse.urlunparse(url_parts)
    return url


response = requests.get("http://34.93.8.218:5000/api/company")


url = "http://34.93.177.185:56733/aggregate/"

response = [
    {
        "name": "Abdullah A Al Barrak and Sons Co",
        "id": 2
    },
    {
        "name": "Baas International Group",
        "id": 3
    },
    {
        "name": "Fugro Suhaimi",
        "id": 4
    },
    {
        "name": "Global Suhaimi Company",
        "id": 5
    },
    {
        "name": "Gulf Farabi Petrochemical Company",
        "id": 6
    },
    {
        "name": "Jacko Gases Company",
        "id": 7
    },
    {
        "name": "JAL International",
        "id": 8
    },
    {
        "name": "Kaefer Saudi Arabia",
        "id": 9
    },
    {
        "name": "SMH Industrial Services",
        "id": 10
    },
    {
        "name": "Vallourec",
        "id": 11
    },
    {
        "name": "Abdulla Fouad Holding",
        "id": 12
    },
    {
        "name": "Sunbelt Supply Co",
        "id": 13
    },
    {
        "name": "Abunayyan Holding",
        "id": 14
    },
    {
        "name": "Arabian Drilling Company",
        "id": 15
    },
    {
        "name": "Saudi Aramco Mobil Refinery Co",
        "id": 16
    },
    {
        "name": "Petro Rabigh",
        "id": 17
    },
    {
        "name": "Oman Oil Company (OOC)",
        "id": 18
    },
    {
        "name": "National Oil Corporation, Libya (NOC)",
        "id": 19
    },
    {
        "name": "Sonatrach",
        "id": 20
    },
    {
        "name": "Abu Dhabi National Oil Company (ADNOC)",
        "id": 21
    },
    {
        "name": "Qatar Petroleum",
        "id": 22
    },
    {
        "name": "National Iranian Oil Company (NIOC)",
        "id": 23
    },
    {
        "name": "Abu Dhabi Oil Refining Company (TAKREER)",
        "id": 24
    },
    {
        "name": "Adyard ABU Dhabi LLC",
        "id": 25
    },
    {
        "name": "Analytical Instrumentation & Maintenance Systems",
        "id": 26
    },
    {
        "name": "Bilfinger Deutsche Babcock Middle East",
        "id": 27
    },
    {
        "name": "Cameron",
        "id": 28
    },
    {
        "name": "China Petroleum Engineering & Construction Corporation",
        "id": 29
    },
    {
        "name": "Emdad Services LLC",
        "id": 30
    },
    {
        "name": "Emirates Industrial Laboratory",
        "id": 31
    },
    {
        "name": "Emirates Lube Oil Company Limited",
        "id": 32
    },
    {
        "name": "Eversendai Offshore RMC FZE",
        "id": 33
    },
    {
        "name": "Frames Abu Dhabi",
        "id": 34
    },
    {
        "name": "Abu Dhabi Gas Industries Limited",
        "id": 35
    },
    {
        "name": "Ghazanfar Group",
        "id": 36
    },
    {
        "name": "Global Trust Enterprises",
        "id": 37
    },
    {
        "name": "Hexa Oil and Gas",
        "id": 38
    },
    {
        "name": "J P Kenny Engineering Limited",
        "id": 39
    },
    {
        "name": "Lootah BC GAS",
        "id": 40
    },
    {
        "name": "Mubarraz Oilfield Installation LLC",
        "id": 41
    },
    {
        "name": "MUC Oil & Gas Engineering Consultancy",
        "id": 42
    },
    {
        "name": "Multiline Employees Provision Services",
        "id": 43
    },
    {
        "name": "National Holding & Al",
        "id": 44
    },
    {
        "name": "National Petroleum Construction Company (NPCC)",
        "id": 45
    },
    {
        "name": "N services JLT",
        "id": 46
    },
    {
        "name": "Petrofac Facilities Management International Ltd.",
        "id": 47
    },
    {
        "name": "Petrofac International",
        "id": 48
    },
    {
        "name": "Quebec Energy LLC",
        "id": 49
    },
    {
        "name": "Raven General Petroleum LLC",
        "id": 50
    },
    {
        "name": "Safwan Petroleum",
        "id": 51
    },
    {
        "name": "Sharafco Group Of Companies",
        "id": 52
    },
    {
        "name": "Sunrise Petroleum Fzc",
        "id": 53
    },
    {
        "name": "Technip",
        "id": 54
    },
    {
        "name": "The MGT Group",
        "id": 55
    },
    {
        "name": "Weir OIl & Gas Services",
        "id": 56
    },
    {
        "name": "YAS Oilfield Services",
        "id": 57
    },
    {
        "name": "Alderley FZE",
        "id": 58
    },
    {
        "name": "Cape Regional Services Dmcc",
        "id": 59
    },
    {
        "name": "Consilium Middle East",
        "id": 60
    },
    {
        "name": "Gulf Petrochem",
        "id": 61
    },
    {
        "name": "Halo Engineering Services LLC",
        "id": 62
    },
    {
        "name": "Loops Automation",
        "id": 63
    },
    {
        "name": "Emirates National Oil Company (ENOC)",
        "id": 64
    },
    {
        "name": "Zakum Development Company (ZADCO)",
        "id": 65
    },
    {
        "name": "ESNAAD",
        "id": 66
    },
    {
        "name": "Dana Gas",
        "id": 67
    },
    {
        "name": "Abu Dhabi Marine Operating Company (ADMA",
        "id": 68
    },
    {
        "name": "TAQA",
        "id": 69
    },
    {
        "name": "Partex Oil and Gas Group",
        "id": 70
    },
    {
        "name": "AlMansoori Specialized Engineering",
        "id": 71
    },
    {
        "name": "John Zink Hamworthy Combustion",
        "id": 72
    },
    {
        "name": "Craig International",
        "id": 73
    },
    {
        "name": "Doha Petroleum Construction Co Ltd",
        "id": 74
    },
    {
        "name": "Petrofac Qatar",
        "id": 75
    },
    {
        "name": "Petrotec Group",
        "id": 76
    },
    {
        "name": "Supreme Supply Services",
        "id": 77
    },
    {
        "name": "Qatar General Petroleum Company",
        "id": 78
    },
    {
        "name": "Qatargas",
        "id": 79
    },
    {
        "name": "Dolphin Energy",
        "id": 80
    },
    {
        "name": "Aban Offshore",
        "id": 81
    },
    {
        "name": "Bharat Petroleum",
        "id": 82
    },
    {
        "name": "Bongaigaon Refinery and Petrochemicals",
        "id": 83
    },
    {
        "name": "Cairn India",
        "id": 84
    },
    {
        "name": "Castrol India",
        "id": 85
    },
    {
        "name": "Chennai Petroleum Corporation",
        "id": 86
    },
    {
        "name": "GAIL",
        "id": 87
    },
    {
        "name": "Great Eastern Energy",
        "id": 88
    },
    {
        "name": "Gujarat Gas",
        "id": 89
    },
    {
        "name": "Gujarat State Petroleum Corporation",
        "id": 90
    },
    {
        "name": "Haldia Petrochemicals",
        "id": 91
    },
    {
        "name": "Hindustan Petroleum",
        "id": 92
    },
    {
        "name": "Indane (LPG)",
        "id": 93
    },
    {
        "name": "Indian Oil Corporation",
        "id": 94
    },
    {
        "name": "Indraprastha Gas",
        "id": 95
    },
    {
        "name": "Mahanagar Gas",
        "id": 96
    },
    {
        "name": "Mangalore Refinery and Petrochemicals Limited",
        "id": 97
    },
    {
        "name": "Nayara Energy",
        "id": 98
    },
    {
        "name": "Oil and Natural Gas Corporation",
        "id": 99
    },
    {
        "name": "Oil India",
        "id": 100
    },
    {
        "name": "Petronet LNG",
        "id": 101
    },
    {
        "name": "Projects and Development India Limited",
        "id": 102
    },
    {
        "name": "Ratnagiri Gas and Power",
        "id": 103
    },
    {
        "name": "Reliance Industries Limited",
        "id": 104
    },
    {
        "name": "Reliance Natural Resources Limited",
        "id": 105
    },
    {
        "name": "Reliance Petroleum",
        "id": 106
    },
    {
        "name": "Savita Oil Technologies Limited",
        "id": 107
    },
    {
        "name": "Bhatia Brothers FZE",
        "id": 108
    },
    {
        "name": "Dash Inspectorate Inspection Services",
        "id": 109
    },
    {
        "name": "Deltachem Middle East LLC",
        "id": 110
    },
    {
        "name": "Parker Drilling",
        "id": 111
    },
    {
        "name": "Halliburton",
        "id": 112
    },
    {
        "name": "Emarat",
        "id": 113
    },
    {
        "name": "Borr Drilling",
        "id": 114
    },
    {
        "name": "Kerui Petroleum",
        "id": 115
    },
    {
        "name": "Seaharvest Group",
        "id": 116
    },
    {
        "name": "Technical Solutions To Industry",
        "id": 117
    },
    {
        "name": "Weatherford International Oil Field Services",
        "id": 118
    },
    {
        "name": "Oceaneering",
        "id": 119
    },
    {
        "name": "National Iranian Gas Company (NIGC)",
        "id": 120
    },
    {
        "name": "National Petrochemical Company (NPC)",
        "id": 121
    },
    {
        "name": "Al Baraka Oilfield Services Saoc",
        "id": 122
    },
    {
        "name": "Al Ghalbi International Engineering Contracting",
        "id": 123
    },
    {
        "name": "Arabian Industries LLC",
        "id": 124
    },
    {
        "name": "Grand Drilling Petroleum Service",
        "id": 125
    },
    {
        "name": "Mohammed Bin Jama Bin Esmail Trading",
        "id": 126
    },
    {
        "name": "Pipeline Supply Company",
        "id": 127
    },
    {
        "name": "W J Towell and Co",
        "id": 128
    },
    {
        "name": "IFluids Engineering",
        "id": 129
    },
    {
        "name": "SPETCO",
        "id": 130
    },
    {
        "name": "United Oil Projects Co K S C",
        "id": 131
    }
]

# for company in response.json()["data"][1:]:

for company in response:

    params = {
        "id": company["id"],
        "company_name": company["name"],
        "common_name": clean(company["name"]),
        "public": False,
        "ticker": "none",
        "source": ["google_news", "gdelt"],
        "date_from": "2019-12-26T05:37:07Z",
        "date_to": "2019-12-27T05:37:07Z",
        "storage_bucket": "alrt-ai-ps"
    }

    temp = create_url(url, params)
    response = requests.get(temp)
    print(response.content)
