from selenium import webdriver
import time

web = webdriver.Chrome()

#enter the data for a batch
data_tuple = (
    ("20BCS5064", "Vatsla", "CSE", "Res", "vats@", "9999"),
    ("20BCS0000", "Trish", "CSE", "Res", "trish@", "999")
)




for data in data_tuple:

    # put the link of the placement form
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSdrfsACGIRNG33kxgq9a6bmdslqne3HPkGNGIW84S3XET7uUg/viewform?usp=sf_link')
    time.sleep(10)


    UID1, Name1, Major1, Resume1, Email1, Contact1 = data 

    # change the xpath by inspecting the google form
    UID=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')          
    Name=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')          
    Major=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')          
    Resume=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')          
    Email=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')          
    Contact=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input') 

    UID.send_keys(UID1)
    Name.send_keys(Name1)
    Major.send_keys(Major1)
    Resume.send_keys(Resume1)
    Email.send_keys(Email1)
    Contact.send_keys(Contact1)



    Submit=web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')          
    Submit.click()

    web.back()



