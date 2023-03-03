from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.action_chains import ActionChains




name=input("Enter username: ")
passw=input("Enter Password: ")
cmnt=input("Enter your comment: ")
ref=input("Enter refresh time in secs: ")

mobile_emulation = { "deviceName": "iPhone X" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

#C:\Users\hasna\OneDrive\Desktop\chromedriver.exe
#'C:\Users\iYlenol\Desktop\chromedriver.exe'

browser = webdriver.Chrome(executable_path=r'C:\Users\iYlenol\Desktop\chromedriver.exe',chrome_options=chrome_options)
browser.get("https://www.instagram.com/?variant=following")
sleep(12)

try:
 wait = WebDriverWait(browser, 30)
 login = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div/div/div[2]/div[3]/button[1]/div')))
 login.click()
except:
 print("login option at start.")

try:
 wait = WebDriverWait(browser, 30)
 username = wait.until(EC.visibility_of_element_located((By.NAME,'username')))
 username.send_keys(name)
except:
  print("entering username.")
 
try:
 wait = WebDriverWait(browser, 30)
 password = wait.until(EC.visibility_of_element_located((By.NAME,'password')))
 password.send_keys(passw)
except:
  print("entering password")

try:
 wait = WebDriverWait(browser, 30)
 login = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div/div/div[2]/form/div[1]/div[6]/button/div')))
 login.click()
except:
  print("login button st.")

try:
 wait = WebDriverWait(browser, 30)
 notNow = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div/div[2]/section/main/div/div/div/button')))
 notNow.click()
except:
  print("not now button.")

try:
 wait = WebDriverWait(browser, 30)
 cross = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Cancel']")))
 cross.click()
except:
  print("cancel button.")

try:
    wait = WebDriverWait(browser, 5)
    nn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Not Now']")))
    nn.click()
except:
     print("login button.")

try:
 wait = WebDriverWait(browser, 30)
 mode = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/div[1]/nav/div/header/div/h1/div/div/div[1]/div/div')))
 mode.click()
except:
  print("instagram logo.")



try:
 wait = WebDriverWait(browser, 30)
 opt = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/div[1]/nav/div/header/div/h1/div/div/div[2]/div/div/div[1]/div[1]/a/div/div[1]/div/div/div/div')))
 opt.click()
except:
  print("following opt.")




try:
    wait = WebDriverWait(browser, 5)
    nn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Not Now']")))
    nn.click()
except:
     print("notNow button.")

sleep(3)

count=0

start=time.time()
visited=[]


while True:
#     with open(r'C:\Users\iYlenol\Desktop\comments.txt', 'r') as f:
#     # Read the list of filenames into a list
#      com = f.read().splitlines()

# # Select a random filename from the list
#     cmnt = random.choice(com)

    if len(visited)>500:
      visited.clear()

    current=time.time()
    if int(current-start)>=int(ref)+4:
        start=current
        browser.refresh()
        count=0
        sleep(4)

    count+=1


    sleep(1)
    try:
        times = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div/div[2]/div/div/div[1]/div/article[{}]/div/div[3]/div/div/div[2]/div/div/a/div/time'.format(count))
    except:
       # print("indexing.")
        continue

    action_chains = ActionChains(browser)
    action_chains.move_to_element(times).perform()
    caption=browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div/div[2]/div/div/div[1]/div/article[{}]/div/div[3]/div/div/div[1]/div/div[1]/div/span[2]/h1'.format(count)).text

    if 'SECOND' in times.text or 'SECONDS' in times.text and caption not in visited:
      try:
        wait = WebDriverWait(browser, 30)
        comment = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div/div[2]/div/div/div[1]/div/article[{}]/div/div[3]/div/div/section[1]/span[2]/button".format(count))))
        comment.click()
      except:
        print("comment button")
      
      try:
        wait = WebDriverWait(browser, 30)
        text=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/section/div/form/div/textarea')))
        browser.execute_script("window.scrollTo(0,0)")
      except:
        print("delay")
        
      try:
        wait = WebDriverWait(browser, 30)
        text=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/section/div/form/div/textarea')))
        text.click()
      except:
          print("big click")

      sleep(1)
        
      try:  
        wait = WebDriverWait(browser, 30)
        text=wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/section/div/form/div/textarea')))
        text.send_keys(cmnt)
      except:
        print('writing comment')
      
      try:
        wait = WebDriverWait(browser, 30)
        post=wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/section/div/form/div/div/div')))
        post.click()
        visited.append(caption)
      except:
        print('post')
      
      


      sleep(1)
      browser.back()
      sleep(2)

    else:
        continue
        


            

        



