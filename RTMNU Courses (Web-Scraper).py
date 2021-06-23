# Getting Data of courses offered by RTMNU in Science and Technology

import pandas as pd
import requests
from bs4 import BeautifulSoup

# getting data from RTMNU site
url = 'https://www.nagpuruniversity.ac.in/v2/courses/Science_Courses.php'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

courses_list = []

table = soup.findAll('td')

for index in table:
    p = index.text
    courses_names = (' '.join(p.split()).replace('\\n', '').replace('\\r', '').replace('  ', ''))
    courses_list.append(courses_names)

# getting data into dictionary
data = {
    "Serial_no": courses_list[8:len(courses_list):8],
    "Post": courses_list[9:len(courses_list):8],
    "Requirements": courses_list[10:len(courses_list):8],
    "Duration": courses_list[11:len(courses_list):8],
    "Examination Held Once/Twice in a year": courses_list[13:len(courses_list):8],
}
# printing data
df = pd.DataFrame(data)
print(df)

# saving data  in csv file
df.to_csv("RTMNU Data.csv", index=False)
