import os

languages = ["en_US","en_GB","de_DE","es_ES","es_MX","fr_FR","fr_CA","it_IT","ja_JP","ko_KR","pt_BR","pt_PT","ru_RU","zh_CN","zh_TW","nl_NL","bg_BG","cs_CZ","da_DK","el_GR","fi_FI","hu_HU","id_ID","nb_NO","pl_PL","sk_SK","sv_SE","tr_TR","uk_UA"]

for i in range(len(languages)):
    fileName = 'texts/'
    fileName += languages[i]
    fileName += '.lang'
    with open('en_US.lang','r') as enUS, open(fileName,'w') as other:
        for line in enUS:
                 other.write(line)

langJson = open('texts\languages.json', 'w')
langJson.write('[\n\t"en_US",\n\t"en_GB",\n\t"de_DE",\n\t"es_ES",\n\t"es_MX",\n\t"fr_FR",\n\t"fr_CA",\n\t"it_IT",\n\t"ja_JP",\n\t"ko_KR",\n\t"pt_BR",\n\t"pt_PT",\n\t"ru_RU",\n\t"zh_CN",\n\t"zh_TW",\n\t"nl_NL",\n\t"bg_BG",\n\t"cs_CZ",\n\t"da_DK",\n\t"el_GR",\n\t"fi_FI",\n\t"hu_HU",\n\t"id_ID",\n\t"nb_NO",\n\t"pl_PL",\n\t"sk_SK",\n\t"sv_SE",\n\t"tr_TR",\n\t"uk_UA"\n]')
langJson.close()

os.remove('en_US.lang')
