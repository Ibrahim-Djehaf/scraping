def scrap_my_job_application_indeed(mail,pwd):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    browser = webdriver.Chrome('/usr/bin/chromedriver')
    #browser.get('https://www.indeed.fr/emplois?l=%C3%8Ele-de-France')
    browser.get('https://www.indeed.fr/myjobs?from=nextsteps_myjobs_desktop&tk=1dhlhpbfo15i4000#applied')
    email = browser.find_element_by_xpath('//*[@id="login-email-input"]')
    email.send_keys(mail)
    time.sleep(3)
    pwd = browser.find_element_by_xpath('//*[@id="login-password-input"]')
    pwd.send_keys(password)
    time.sleep(3)
    pwd.send_keys(Keys.ENTER)
    browser.find_element_by_xpath('//*[@id="views"]/div/span[2]/a').click()
    cdt = []
    nb_cdt = 17
    for i in range(100):
        candi = browser.find_element_by_xpath('//*[@id="jobs"]')
        cdt.append(candi.text)
    l = [i.split('\n') for i in cdt[:1]]
    flat_list = [item for sublist in l for item in sublist]
    n = 4
    # using list comprehension
    final = [flat_list[i * n:(i + 1) * n] for i in range((len(flat_list) + n - 1) // n )]
    #print (final)

    import pandas as pd
    df = pd.DataFrame(final,columns=['Poste','Entreprise','Quand','question'])
    df.to_csv('Candidature.csv',index=False)
scrap_my_job_application_indeed(mail, password)
