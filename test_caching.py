import pytest
import getURL, caching

def test_caching():
    url = "https://rtsfred3.github.io/echoo/"
    assert getURL.getURL(url) == caching.getHTML(url)

def test_caching2():
    url = "https://rtsfred3.github.io/echoo/index2.html"
    assert getURL.getURL(url) == caching.getHTML(url)

def test_caching3():
    url = "http://www.githubstat.us/"
    assert getURL.getURL(url) == caching.getHTML(url)

def test_caching4():
    url = "https://library.up.edu/"
    assert getURL.getURL(url) == caching.getHTML(url)

def test_caching5():
    url = "https://www.up.edu/"
    assert getURL.getURL(url) == caching.getHTML(url)
