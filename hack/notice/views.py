import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from urllib.parse import urljoin

def get_notices():
    base_url = 'https://en.knu.ac.kr'
    url = urljoin(base_url, '/board/notice01.htm')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        print(response.text)
        
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    notices = []

    rows = soup.find_all('tr')[1:]
    for row in rows:
        num_td = row.find('td', class_=['num notice', 'num'])
        subject_td = row.find('td', class_='subject')
        
        if num_td and subject_td:
            num = num_td.text.strip()
            title_a = subject_td.find('a')
            if title_a:
                title = title_a.text.strip()
                link = urljoin(base_url, title_a['href']) if 'href' in title_a.attrs else ''
                date_td = row.find('td', class_='date')
                date = date_td.text.strip() if date_td else ''
                hit_td = row.find('td', class_='hit')
                hit = hit_td.text.strip() if hit_td else ''
                
                notices.append({
                    'no': num,
                    'title': title,
                    'link': link,
                    'date': date,
                    'hit': hit
                })
    
    return notices

def notice_list(request):
    notices = get_notices()
    return render(request, 'notice/notice_list.html', {'notices': notices})

def get_notices_cn():
    base_url = 'https://cn.knu.ac.kr'
    url = urljoin(base_url, '/board/notice01.htm')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        print(response.text)
        
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    notices = []

    rows = soup.find_all('tr')[1:]
    for row in rows:
        num_td = row.find('td', class_=['num notice', 'num'])
        subject_td = row.find('td', class_='subject')
        
        if num_td and subject_td:
            num = num_td.text.strip()
            title_a = subject_td.find('a')
            if title_a:
                title = title_a.text.strip()
                link = urljoin(base_url, title_a['href']) if 'href' in title_a.attrs else ''
                date_td = row.find('td', class_='date')
                date = date_td.text.strip() if date_td else ''
                hit_td = row.find('td', class_='hit')
                hit = hit_td.text.strip() if hit_td else ''
                
                notices.append({
                    'no': num,
                    'title': title,
                    'link': link,
                    'date': date,
                    'hit': hit
                })
    
    return notices

def notice_list_cn(request):
    notices = get_notices_cn()
    return render(request, 'notice/notice_list_cn.html', {'notices': notices})

