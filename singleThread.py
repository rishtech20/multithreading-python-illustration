import time
from utils import make_request, URL_LIST

t1 = time.time()

for i, url in enumerate(URL_LIST):
    make_request(url)
    print(
        f"Downloaded item \033[32m{i + 1} of {len(URL_LIST)}\033[m")

t2 = time.time()

print(f"---- Downloaded {len(URL_LIST)} items in {round(t2 - t1)} seconds----")
