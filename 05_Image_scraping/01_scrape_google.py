from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

search_queries = ['horse', 'lion']


def download_images(query):
    arguments = {
        'keywords': query,
        'format': 'jpg',
        'limit': '101',
        'print_urls': True,
        'size': 'medium',
        'aspect_ratio': 'square',
        'chromedriver': r'F:\Chromdriver\chromedriver_win32\chromedriver.exe'
    }
    try:
        response.download(arguments)
    except FileNotFoundError:
        arguments = {
            'keywords': query,
            'format': 'jpg',
            'limit': '101',
            'print_urls': True,
            'size': 'medium',
            'chromedriver': r'F:\Chromdriver\chromedriver_win32\chromedriver.exe'
        }
        try:
            response.download(arguments)
        except:
            # print('Passed')
            pass


for query in search_queries:
    download_images(query)
    print()
