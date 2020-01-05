import time
from concurrent.futures import ThreadPoolExecutor
from utils import make_request, URL_LIST

t1 = time.time()

with ThreadPoolExecutor() as executor:
    results = executor.map(make_request, URL_LIST)
    for result in results:
        print(type(result))

t2 = time.time()

print(f"---- Downloaded {len(URL_LIST)} items in {round(t2 - t1)} seconds----")
