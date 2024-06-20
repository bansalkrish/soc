from bs4 import BeautifulSoup
import requests
import pandas as pd

socdata = {"name":[], "link":[], "mentorname":[], "menteenumber":[]}

html_text = requests.get('https://shiveshcodes.github.io/wncc-soc.github.io/soc/').text
soup = BeautifulSoup(html_text, 'lxml')
projects = soup.find_all('span', class_ = 'rounded')
plinks = soup.find_all('div', class_ = 'rounded hover-wrapper pr-3 pl-3 pt-3 pb-3 bg-white')

for project in projects:
    projectname = project.find('p', class_ = 'lead text-center font-weight-bold text-dark').text
    # print(projectname)
    socdata["name"].append(projectname)
for plink in plinks:
    projectlink = plink.a['href']
    projectlinkfinal = "https://shiveshcodes.github.io" + projectlink
    # print(projectlinkfinal)
    socdata["link"].append(projectlinkfinal)

    m_name_dict = {"m_name_list":[]}
    temporary = {"mname":[]}

    html_text2 = requests.get(projectlinkfinal).text
    soup2 = BeautifulSoup(html_text2, 'lxml')
    mentorname = soup2.find('div', class_ = 'col-sm-10 col-md-8')
    names = mentorname.find_all('p', class_ = 'lead')
    for name in names:
        mentornames = name.text
        # print(mentornames)
        m_name_dict["m_name_list"].append(mentornames)


    
    number = m_name_dict['m_name_list'].pop()
    socdata['menteenumber'].append(number)
    temporary['mname'] = m_name_dict['m_name_list']
    socdata['mentorname'].append(temporary['mname'])
print(socdata['mentorname'])
    
     
df = pd.DataFrame.from_dict(socdata)
df.to_csv("socdata.csv", index = False)


