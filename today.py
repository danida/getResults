from selenium import webdriver
driver = webdriver.Firefox()
import re
from datetime import datetime
from xlutils.copy import copy
import xlrd
from match import match1

def append_df_to_excel(filename, darray):
    rb = xlrd.open_workbook(filename, formatting_info=True)
    r_sheet = rb.sheet_by_index(0)
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    print()
    i=0
    maxrow = len(sheet._Worksheet__rows)
    for col in darray:
        print(col)
        j=0
        for row in col:
               sheet.write(maxrow+j, i, row)
               j+=1
        i+=1

    wb.save(filename)



def hasClass(element, classsearched):
    parent = element.find_element_by_xpath('.')
    classes = parent.get_attribute('class')
    classes = classes.split()
    for class1 in classes:
        if class1 == classsearched:
            return True
    return False

def getScheduledMatches(code,url):
    driver.get(url)
    tbody = driver.find_element_by_css_selector('.sportName')
    matches = tbody.find_elements_by_xpath('*')
    A = []
    B = []
    C = []
    F = []
    G = []
    H = []
    I = []
    D = []
    E = []
    roundmatches = {}
    matches = matches[0:20]
    for match in matches:
        if hasClass(match, 'event_round'):
            break
        if len(match.find_elements_by_css_selector('.event__participant--home'))!=0:
            home = match.find_element_by_css_selector('.event__participant--home')
            away = match.find_element_by_css_selector('.event__participant--away')
            hometeamname = re.findall("\w+", home.get_attribute('innerText'))
            awayteamname = re.findall("\w+", away.get_attribute('innerText'))
            hometeamname = (' '.join(hometeamname))
            awayteamname = (' '.join(awayteamname))
            score = match.find_element_by_css_selector('.event__scores')


            time = match.find_element_by_css_selector('.event__time')
            print(2020)
            time = datetime.strptime(time.get_attribute('innerHTML') + ' ' + str(2020), '%d.%m. %H:%M %Y')

            time = datetime(2020, time.month, time.day, time.hour, time.minute)

            F.append(hometeamname)
            G.append(awayteamname)
            H.append(-1)
            I.append(-1)

            E.append(datetime.time(time))
            D.append(datetime.date(time))
            B.append("")
            A.append("")
            C.append(2020)

    print (str(datetime.time(time))+'\t'+hometeamname+"\t"+awayteamname)
    darray = []
    darray.append(A)
    darray.append(B)
    darray.append(C)
    darray.append(D)
    darray.append(E)
    darray.append(F)
    darray.append(G)
    darray.append(H)
    darray.append(I)

    print (darray)



    append_df_to_excel('C:\\Users\\danida\\Desktop\\excels2\\' + code + '.xls',darray )

countries = {}
#countries["CRO1_"]="https://www.flashscore.com/football/croatia/1-hnl/fixtures/"
#countries["MEX"] = "https://www.flashscore.com/football/mexico/primera-division/fixtures/"
#countries["COL"]="https://www.flashscore.com/football/colombia/liga-aguila/fixtures/"
#countries["EGYPT"]="https://www.flashscore.com/football/egypt/premier-league/fixtures/"
countries["ENG"]="https://www.flashscore.com/football/england/premier-league/fixtures/"
countries["Championship"]="https://www.flashscore.com/football/england/championship/fixtures/"
#countries["FRA"]="https://www.flashscore.com/football/france/ligue-1/fixtures/"
#countries["IRAN"]="https://www.flashscore.com/football/iran/persian-gulf-pro-league/fixtures/"
#countries["ITA"]="https://www.flashscore.com/football/italy/serie-a/fixtures/"
#countries["NED"]="https://www.flashscore.com/football/netherlands/eredivisie/fixtures/"
countries["SCO"]="https://www.flashscore.com/football/scotland/premiership/fixtures/"
#countries["SPA"]="https://www.flashscore.com/football/spain/laliga/fixtures/"
countries["USARAB"]="https://www.flashscore.com/football/united-arab-emirates/uae-league/fixtures/"
#countries["IRAK"]="https://www.flashscore.com/football/iraq/super-league/fixtures/"
countries["SAUD"]="https://www.flashscore.com/football/saudi-arabia/saudi-professional-league/fixtures/"
#countries["FRA2_"] = "https://www.flashscore.com/football/france/ligue-2/fixtures/"
#countries["FRA3_"] = "https://www.flashscore.com/football/france/national/fixtures/"
#countries["GER"] ="https://www.flashscore.com/football/germany/bundesliga/fixtures/"
#countries["NED2_"] ="https://www.flashscore.com/football/netherlands/eerste-divisie/fixtures/"
#countries["POR"] = "https://www.flashscore.com/football/portugal/primeira-liga/fixtures/"
#countries["SPA2_"] = "https://www.flashscore.com/football/spain/laliga2/fixtures/"
countries["TUR"] = "https://www.flashscore.com/football/turkey/super-lig/fixtures/"
#countries["GRE"] = "https://www.flashscore.com/football/greece/super-league/fixtures/"
#countries["IRL2019"] = "https://www.flashscore.com/football/ireland/premier-division/fixtures/"
countries["MAROC"] = "https://www.flashscore.com/football/morocco/botola-pro/fixtures/"
#countries["FIN2019"] = "https://www.flashscore.com/football/finland/veikkausliiga/fixtures/"

#countries["MAROC"] = "https://www.flashscore.com/football/morocco/botola-pro/fixtures/"

for key, value in countries.items():
    print(key+"\n")
    getScheduledMatches(key,value)

driver.close()
