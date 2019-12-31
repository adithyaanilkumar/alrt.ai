import json

"""
https://github.com/OpenDemocracyManitoba/winnipegelection/wiki/Google-News-RSS-Scraping
https://stackoverflow.com/questions/57792590/google-news-xml-api-use-country-language-parameters
https://www.andiamo.co.uk/resources/iso-language-codes/
https://sites.google.com/site/tomihasa/google-language-codes
"""
with open("labels.json", "r") as fp:
    labels = json.load(fp)["parameters"]

hl = {'af': 'Afrikaans', 'ak': 'Akan', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', 'hy': 'Armenian', 'az': 'Azerbaijani', 'eu': 'Basque', 'be': 'Belarusian', 'bem': 'Bemba', 'bn': 'Bengali', 'bh': 'Bihari', 'xx-bork': 'bork!', 'bs': 'Bosnian', 'br': 'Breton', 'bg': 'Bulgarian', 'km': 'Cambodian', 'ca': 'Catalan', 'chr': 'Cherokee', 'ny': 'Chichewa', 'zh-CN': 'Simplified Chinese', 'zh-TW': 'Traditional Chinese', 'co': 'Corsican', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'xx-elmer': 'Fudd', 'en': 'English', 'eo': 'Esperanto', 'et': 'Estonian', 'ee': 'Ewe', 'fo': 'Faroese', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'fy': 'Frisian', 'gaa': 'Ga', 'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek', 'gn': 'Guarani', 'gu': 'Gujarati', 'xx-hacker': 'Hacker', 'ht': 'Creole', 'ha': 'Hausa', 'haw': 'Hawaiian', 'iw': 'Hebrew', 'hi': 'Hindi', 'hu': 'Hungarian', 'is': 'Icelandic', 'ig': 'Igbo', 'id': 'Indonesian', 'ia': 'Interlingua', 'ga': 'Irish', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese', 'kn': 'Kannada', 'kk': 'Kazakh', 'rw': 'Kinyarwanda', 'rn': 'Kirundi', 'xx-klingon': 'Klingon', 'kg': 'Kongo', 'ko': 'Korean', 'kri': 'Leone', 'ku': 'Kurdish', 'ckb': 'Soranî', 'ky': 'Kyrgyz', 'lo': 'Laothian', 'la': 'Latin', 'lv': 'Latvian', 'ln': 'Lingala',
            'lt': 'Lithuanian', 'loz': 'Lozi', 'zh-HK':'Chinese Hong Kong SAR','lg': 'Luganda', 'ach': 'Luo', 'mk': 'Macedonian', 'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Marathi', 'mfe': 'Creole', 'mo': 'Moldavian', 'mn': 'Mongolian', 'sr-ME': 'Montenegrin', 'ne': 'Nepali', 'pcm': 'Pidgin', 'nso': 'Sotho', 'no': 'Norwegian', 'nn': 'Nynorsk', 'oc': 'Occitan', 'or': 'Oriya', 'om': 'Oromo', 'ps': 'Pashto', 'fa': 'Persian', 'xx-pirate': 'Pirate', 'pl': 'Polish', 'pt-BR': 'Brazil', 'pt-PT': 'Portugal', 'pa': 'Punjabi', 'qu': 'Quechua', 'ro': 'Romanian', 'rm': 'Romansh', 'nyn': 'Runyakitara', 'ru': 'Russian', 'gd': 'Gaelic', 'sr': 'Serbian', 'sh': 'Serbo-Croatian', 'st': 'Sesotho', 'tn': 'Setswana', 'crs': 'Creole', 'sn': 'Shona', 'sd': 'Sindhi', 'si': 'Sinhalese', 'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali', 'es': 'Spanish', 'es-419': 'American)', 'su': 'Sundanese', 'sw': 'Swahili', 'sv': 'Swedish', 'tg': 'Tajik', 'ta': 'Tamil', 'tt': 'Tatar', 'te': 'Telugu', 'th': 'Thai', 'ti': 'Tigrinya', 'to': 'Tonga', 'lua': 'Tshiluba', 'tum': 'Tumbuka', 'tr': 'Turkish', 'tk': 'Turkmen', 'tw': 'Twi', 'ug': 'Uighur', 'uk': 'Ukrainian', 'ur': 'Urdu', 'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'wo': 'Wolof', 'xh': 'Xhosa', 'yi': 'Yiddish', 'yo': 'Yoruba', 'zu': 'Zulu','en-AU':'English Australian','en-IN':'English India','en-NZ':'English Newzeland','en-GB':'English United Kingdom','en-CA':'English Canada'}

gl = {'af': 'Afrikaans', 'ae': 'U.A.E.', 'bh': 'Bahrain', 'dz': 'Algeria', 'eg': 'Egypt', 'iq': 'Iraq', 'jo': 'Jordan', 'kw': 'Kuwait', 'lb': 'Lebanon', 'ly': 'Libya', 'ma': 'Morocco', 'om': 'Oman', 'qa': 'Qatar', 'sa': 'Saudi Arabia', 'sy': 'Syria', 'tn': 'Tunisia', 'ye': 'Yemen', 'be': 'Belarusian', 'bg': 'Bulgarian', 'ca': 'Catalan', 'cs': 'Czech', 'cy': 'Welsh', 'da': 'Danish', 'de': 'Germany', 'at': 'Austria', 'ch': 'Switzerland', 'li': 'Liechtenstein', 'lu': 'German Luxembourg', 'el': 'Greek', 'en': 'English', 'au': 'Australia', 'bz': 'Belize', 'ca': 'Canada', 'gb': 'United Kingdom', 'ie': 'Ireland', 'jm': 'Jamaica', 'nz': 'New Zealand', 'tt': 'Trinidad', 'us': 'United States', 'za': 'South Africa', 'es': 'Spain', 'ar': 'Argentina', 'bo': 'Bolivia', 'cl': 'Chile', 'co': 'Colombia', 'cr': 'Costa Rica', 'do': 'Dominican Republic', 'ec': 'Ecuador', 'gt': 'Guatemala', 'hn': 'Honduras', 'mx': 'Mexico', 'ni': 'Nicaragua', 'pa': 'Panama', 'pe': 'Peru', 'pr': 'Puerto Rico',
      'py': 'Paraguay', 'sv': 'El Salvador', 'uy': 'Uruguay', 've': 'Venezuela', 'et': 'Estonian', 'eu': 'Basque', 'fa': 'Farsi', 'fi': 'Finnish', 'fo': 'Faeroese', 'fr': 'Standard', 'be': 'Belgium', 'ca': 'Canada', 'ch': 'Switzerland', 'lu': 'Luxembourg', 'ga': 'Irish', 'gd': 'Scotland', 'he': 'Hebrew', 'hi': 'Hindi', 'hr': 'Croatian', 'hu': 'Hungarian', 'id': 'Indonesian', 'is': 'Icelandic', 'it': 'Italy', 'ch': 'Switzerland', 'ja': 'Japanese', 'ji': 'Yiddish', 'ko': 'Johab', 'ku': 'Kurdish', 'lt': 'Lithuanian', 'lv': 'Latvian', 'mk': 'Macedonian ', 'ml': 'Malayalam', 'ms': 'Malaysian', 'mt': 'Maltese', 'nb': 'Norwegian', 'nl': 'Dutch', 'be': 'Belgium', 'nn': 'Nynorsk', 'no': 'Norwegian', 'pa': 'Punjab', 'pl': 'Polish', 'pt': 'Portugal', 'br': 'Brazil', 'rm': 'Rhaeto-Romanic', 'ro': 'Romanian', 'md': 'Republic of Moldova', 'ru': 'Russian', 'md': 'Republic of Moldova', 'sb': 'Sorbian', 'sk': 'Slovak', 'sl': 'Slovenian', 'sq': 'Albanian', 'sr': 'Serbian', 'sv': 'Swedish', 'fi': 'Finland', 'th': 'Thai', 'tn': 'Tswana', 'tr': 'Turkish', 'ts': 'Tsonga', 'uk': 'Ukrainian', 'ur': 'Urdu', 've': 'Venda', 'vi': 'Vietnamese', 'xh': 'Xhosa', 'cn': 'PRC', 'hk': 'Hong Kong', 'sg': 'Singapore', 'tw': 'Taiwan', 'zu': 'Zulu', 'us': 'United States','me':'Montengero','bd':'Bangladesh','in':'India','il':'Israel','jp':'Japan','my':'Malaysia','pk':'Pakistan','ph':'Philippines','kr':'Korea','vn':'Vietnam','bw':'Botswana','cz':'Czech Republic','ee':'Estonia','gr':'Greece','ke':'Kenya','ng':'Nigeria','sn':'Senegal','rs':'Serbia','si':'Slovenia','se':'Sweden','ua':'Ukraine','uz':'Uzbekistan','zw':'Zimbabwe','ug':'Uighur','na':'Nauru','cu':'Slavonic'}

mod_labels = {
    "hl": {},
    "gl": {},
}

hl_none_exist= list()
gl_none_exist=list()

for label in labels:
    if label["hl"] in hl:
        mod_labels["hl"][label["hl"]] = hl[label["hl"]]
    else:
        hl_none_exist.append(label["hl"])

    if label["gl"].lower() in gl:
        mod_labels["gl"][label["gl"].lower()] = gl[label["gl"].lower()]
    else:
        gl_none_exist.append(label["gl"].lower())


print("total no of labels: {}".format(len(labels)))

print("no of hl: {}".format(len(mod_labels['hl'])))
print("no of gl: {}".format(len(mod_labels['gl'])))
print(hl_none_exist)#the names which are not in hl
print(gl_none_exist)#the names which are not in gl

with open("final.json", "w") as fp:
   json.dump(mod_labels, fp)
