from selenium import webdriver 										
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC 	#Selenium imports
import time 	#for time.sleep
import csv		#necessary to write to csv file

driver = webdriver.Firefox()
driver.get("http://www.gelbeseiten.de/essen-auf-raedern/s1/relevanz/branche-23551")
links = []
button = []
i = 1
endpage = 6 #Last page to visit
while(i < endpage + 1): 
	time.sleep(4) #necessary to be sure dom is loaded

	#Saving all Websites in Xpath to list rawlinks unformatted
	rawlinks = driver.find_elements_by_xpath("//*[@id='gs_body']/div/div[4]/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li/a")

	#Appending rawlinks to list links to format it later
	for link in rawlinks:
		links.append(link.get_attribute("title"))
	
	del button[:] #button has to be found new every time, otherwhise selenium is unable to click it

	#looking for "forward" button on every page except the last one
	if i < endpage:
		button = driver.find_elements_by_css_selector("#gs_body > div > div.row-fluid.gs_inhalt > div.span-fluid-wide.tl-mitte > div.gs_paginierung_wrapper.gs_paginierung_erste > div.gs_seite_vor_wrapper > a > button")
		button[0].click()
	
	print "Currently crawling page:", i
	i = i + 1

links_sauber = list(set(links)) #delete the double entries


with open('websites_demo.csv', 'wb') as myfile: #create and open csv file to save the output
    wr = csv.writer(myfile)
    for link in links_sauber:
    	wr.writerow([link.encode('ascii','ignore'), ])

print "Success, check vagrant Folder!"