from bs4 import BeautifulSoup
import requests

def search_indeed():
    website_url = "https://www.indeed.com/jobs?q=software%20developer%20%24115%2C000&l=Frisco%2C%20TX&jt=fulltime&explvl=entry_level&vjk=e324c2afeff9c5ae"
    html_text = requests.get(website_url).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_ = 'slider_container css-11g4k3a eu4oa1w0')

    for job in jobs:
        job_company_name = job.find('span', class_ = 'companyName').text
        job_name = job.find('div', class_ = 'heading4 color-text-primary singleLineTitle tapItem-gutter').text.replace("new", "")
        job_location = job.find('div', class_ = 'companyLocation').text
        
        # workaround because not all jobs have salary listed
        try:
            job_salary = job.find('div', class_ = 'metadata salary-snippet-container').text
        except:
            job_salary = "Unknown salary"
            
        print(f"{job_company_name}")
        print(f"{job_name}")
        print(f"{job_salary}")
        print(f"{job_location}")
        print("")
        
search_indeed()