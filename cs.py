from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"

browser_driver = Service('/usr/bin/chromedriver')

page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/login/index.php")
    time.sleep(1)

    page_to_scrape.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/section/div/div[2]/div/div/div/div/div/div[2]/div[3]/div/a").click()
    time.sleep(1)

    mail = page_to_scrape.find_element(By.XPATH, '//*[@id="i0116"]')
    mail.send_keys(os.environ['mail'])  
    page_to_scrape.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    time.sleep(1)   

    password = page_to_scrape.find_element(By.XPATH, '//*[@id="i0118"]')
    password.send_keys(os.environ['password'])  
    page_to_scrape.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    time.sleep(1)

    page_to_scrape.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()
    time.sleep(1)

    # I godina
    # uur

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=2&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(1)
    
    uurT = page_to_scrape.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/section/div/article[1]/div')
    uur_markdown = uurT.text
    uurT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

    with open("uur.md", "w") as uur_file:
        uur_file.write(uur_markdown)

    heightUUR = uurT.size['height']
    widthUUR = uurT.size['width']
    desired_widthUUR = max(widthUUR, 1200)  
    desired_heightUUR = min(heightUUR, 1000)
    page_to_scrape.set_window_size(desired_widthUUR, desired_heightUUR)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", uurT)
    uurT.screenshot('uur.png')

    # aip

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=3&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(1)
    
    aipT = page_to_scrape.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/section/div/article[1]/div')
    aip_markdown = aipT.text
    aipT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

    with open("aip.md", "w") as aip_file:
        aip_file.write(aip_markdown)

    heightAIP = aipT.size['height']
    widthAIP = aipT.size['width']
    desired_widthAIP = max(widthAIP, 1200)  
    desired_heightAIP = min(heightAIP, 1000)
    page_to_scrape.set_window_size(desired_widthAIP, desired_heightAIP)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", aipT)
    aipT.screenshot('aip.png')

    # II godina
    # bp

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=4&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(1)
    
    bpT = page_to_scrape.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/section/div/article[1]/div')
    bp_markdown = bpT.text
    bpT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

    with open("bp.md", "w") as bp_file:
        bp_file.write(bp_markdown)

    heightBP = bpT.size['height']
    widthBP = bpT.size['width']
    desired_widthBP = max(widthBP, 1200)  
    desired_heightBP = min(heightBP, 1000)
    page_to_scrape.set_window_size(desired_widthBP, desired_heightBP)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", bpT)
    bpT.screenshot('bp.png')

    # dmat

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=97&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(1)
    
    dmatT = page_to_scrape.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/section/div/article[1]/div')
    dmat_markdown = dmatT.text
    dmatT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

    with open("dmat.md", "w") as dmat_file:
        dmat_file.write(dmat_markdown)

    heightDMAT = dmatT.size['height']
    widthDMAT = dmatT.size['width']
    desired_widthDMAT = max(widthDMAT, 1200)  
    desired_heightDMAT = min(heightDMAT, 1000)
    page_to_scrape.set_window_size(desired_widthDMAT, desired_heightDMAT)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", dmatT)
    dmatT.screenshot('dmat.png')

    # oop

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=45&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(1)
    
    oopT = page_to_scrape.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/section/div/article[1]/div')
    oop_markdown = oopT.text
    oopT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

    with open("oop.md", "w") as oop_file:
        oop_file.write(oop_markdown)

    heightOOP = oopT.size['height']
    widthOOP = oopT.size['width']
    desired_widthOOP = max(widthOOP, 1200)  
    desired_heightOOP = min(heightOOP, 1000)
    page_to_scrape.set_window_size(desired_widthOOP, desired_heightOOP)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", oopT)
    oopT.screenshot('oop.png')


    # lp

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=41&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(1)
    
    lpT = page_to_scrape.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/section/div/article[1]/div')
    lp_markdown = lpT.text
    lpT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

    with open("lp.md", "w") as lp_file:
        lp_file.write(lp_markdown)

    heightLP = lpT.size['height']
    widthLP = lpT.size['width']
    desired_widthLP = max(widthLP, 1200)  
    desired_heightLP = min(heightLP, 1000)
    page_to_scrape.set_window_size(desired_widthLP, desired_heightLP)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", lpT)
    lpT.screenshot('lp.png')




    # oopj

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=62&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(1)
    
    oopjT = page_to_scrape.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/section/div/article[1]/div')
    oopj_markdown = oopjT.text
    oopjT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

    with open("oopj.md", "w") as oopj_file:
        oopj_file.write(oopj_markdown)

    heightOOPJ = oopjT.size['height']
    widthOOPJ = oopjT.size['width']
    desired_widthOOPJ = max(widthOOPJ, 1200)  
    desired_heightOOPJ = min(heightOOPJ, 1000)
    page_to_scrape.set_window_size(desired_widthOOPJ, desired_heightOOPJ)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", oopjT)
    oopjT.screenshot('oopj.png')



    # sp

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=9&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(1)
    
    spT = page_to_scrape.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/section/div/article[1]/div')
    sp_markdown = spT.text
    spT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

    with open("sp.md", "w") as sp_file:
        sp_file.write(sp_markdown)

    heightSP = spT.size['height']
    widthSP = spT.size['width']
    desired_widthSP = max(widthSP, 1200)  
    desired_heightSP = min(heightSP, 1000)
    page_to_scrape.set_window_size(desired_widthSP, desired_heightSP)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", spT)
    spT.screenshot('sp.png')


    # pj

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=11&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(1)
    
    pjT = page_to_scrape.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/section/div/article[1]/div')
    pj_markdown = pjT.text
    pjT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

    with open("pj.md", "w") as pj_file:
        pj_file.write(pj_markdown)

    heightPJ = pjT.size['height']
    widthPJ = pjT.size['width']
    desired_widthPJ = max(widthPJ, 1200)  
    desired_heightPJ = min(heightPJ, 1000)
    page_to_scrape.set_window_size(desired_widthPJ, desired_heightPJ)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", pjT)
    pjT.screenshot('pj.png')

    # III godina
    # os

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=55&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(1)
    
    osT = page_to_scrape.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/section/div/article[1]/div')
    os_markdown = osT.text
    osT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

    with open("os.md", "w") as os_file:
        os_file.write(os_markdown)

    heightOS = osT.size['height']
    widthOS = osT.size['width']
    desired_widthOS = max(widthOS, 1200)  
    desired_heightOS = min(heightOS, 1000)
    page_to_scrape.set_window_size(desired_widthOS, desired_heightOS)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", osT)
    osT.screenshot('os.png')


    # rm

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=49&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(1)
    
    rmT = page_to_scrape.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/section/div/article[1]/div')
    rm_markdown = rmT.text
    rmT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

    with open("rm.md", "w") as rm_file:
        rm_file.write(rm_markdown)

    heightRM = rmT.size['height']
    widthRM = rmT.size['width']
    desired_widthRM = max(widthRM, 1200)  
    desired_heightRM = min(heightRM, 1000)
    page_to_scrape.set_window_size(desired_widthRM, desired_heightRM)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", rmT)
    rmT.screenshot('rm.png')

    # ti

    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=110&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2000&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    time.sleep(1)
    
    tiT = page_to_scrape.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/section/div/article[1]/div')
    ti_markdown = tiT.text
    tiT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

    with open("ti.md", "w") as ti_file:
        ti_file.write(ti_markdown)

    heightTI = tiT.size['height']
    widthTI = tiT.size['width']
    desired_widthTI = max(widthTI, 1200)  
    desired_heightTI = min(heightTI, 1000)
    page_to_scrape.set_window_size(desired_widthTI, desired_heightTI)    
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", tiT)
    tiT.screenshot('ti.png')




finally:
    
    page_to_scrape.quit()
