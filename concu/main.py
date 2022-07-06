import threading
import time
import requests as req
import concurrent.futures

base_url = "https://restcountries.com/v3.1"
countries = tuple(map(lambda country: country["flags"]["png"],req.get(f"{base_url}/all").json()))

def download_flag(flag_url):
    flag = req.get(flag_url).content
    # file = open(f"flags/{flag_url[-7:-4]}.png", "wb")
    # file.write(flag)
    # file.close()
    # return True
# start_1 = time.perf_counter()

# for country in countries:
#     download_flag(country)

# finish_1 = time.perf_counter()
# print(finish_1-start_1)

print("".center(50, "-"))

start_2 = time.perf_counter()
# for country in countries:
#     t = threading.Thread(target=download_flag, args=[country])
#     t.start()



# t1 = threading.Thread(target=greeting, args=["Función 1"])


# greeting("Función 2")

with concurrent.futures.ThreadPoolExecutor() as executor:
    a = executor.map(download_flag, countries)
    
finish_2 = time.perf_counter()
print(finish_2-start_2)