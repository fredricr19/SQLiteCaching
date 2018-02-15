import time, sqlite3
import getURL

db_file = "caching.db"

def search(c, url):
    c.execute("SELECT url FROM cache")
    for row in c:
        if row[0] == url:
            return False
    return True

def getAge(c, url, age=-1):
    c.execute("SELECT time FROM cache WHERE url='" + url + "'")
    for row in c:
        age = (time.time() - int(row[0]))/(60)
    return age

def saveURL(url):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS cache (url, html, time)")
    
    if search(c, url):
        html = getURL.getURL(url)
        insert = "'%s','%s','%s'" % (url, html, str(int(time.time())))
        
        c.execute("INSERT INTO cache VALUES (" + insert + ")")
        conn.commit()
    elif not search(c, url) and getAge(c, url) >= 10:
        html = getURL.getURL(url)
        c.execute("UPDATE cache SET html='" + html + "', time='" + str(int(time.time())) + "' WHERE url='" + url + "'")
        conn.commit()
    conn.close()

def getHTML(url, html=""):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS cache (url, html, time)")
    
    if not search(c, url):
        c.execute("SELECT html FROM cache WHERE url='" + url + "'")
        for row in c:
            html = row[0]
    if search(c, url):
        saveURL(url)
        html = getHTML(url)
    
    conn.close()
    return html

def main():
    url = "http://www.githubstat.us/"
    
    start = time.time()
    #saveURL(url)
    print(getHTML(url))
    print(round(time.time() - start, 5), "seconds")
