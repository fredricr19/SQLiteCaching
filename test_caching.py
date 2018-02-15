import pytest
import getURL, caching

def test_caching():
    url = "https://rtsfred3.github.io/echoo/"
    assert getURL.getURL(url) == caching.getHTML(url)
    
def test_caching2():
    url = "https://rtsfred3.github.io/echoo/index2.html"
    assert getURL.getURL(url) == caching.getHTML(url)
    
def test_caching3():
    url = "http://www.githubstat.us/app/"
    assert getURL.getURL(url) == caching.getHTML(url)
