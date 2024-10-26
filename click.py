import time
from selenium import webdriver
def open_links(links):
    # browser configuration
    options = webdriver.EdgeOptions()
    options.binary_location = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    # create browser driver
    driver = webdriver.Edge(options=options)
    # use full screen windows
    driver.maximize_window()

    try:
        # used implicitly_wait for make delay on pages
        driver.implicitly_wait(180)  # 180 sec delayed

        while True:
            # open website links
            for link in links:
                driver.get(link)
                time.sleep(10)
            # reset browser for first link
            driver.get(links[0])
            time.sleep(90)

    except Exception as e:
        print("An error occurred:", e)

    finally:
        # close browser on end execution code
        driver.quit()


if __name__ == "__main__":
    # website links
    links = [
        "https://www.testweb1.com/",
        "https://www.testweb2.com/",
        "https://www.testweb3.com/",
        "https://www.testweb4.com/",
        "https://www.testweb5.com/",
        "https://www.testweb6.com/",

    ]

    open_links(links)