import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


# data url provided
url = "https://questionnaire-148920.appspot.com/swe/data.html"

# HTTP GET request to the URL
response = requests.get(url)

# if request successful
if response.status_code == 200:
    # use BeautifulSoup to parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # get the table data
    data = soup.find("table")

    # if table found
    if data:
        # get column data
        player = []
        salary = []
        year = []
        level = []

        # iterate over rows (skip the header row if it exists)
        for row in data.find_all("tr")[1:]:
            columns = row.find_all("td")
            # corresponding to the four categories
            if len(columns) == 4: 
                player.append(columns[0].text.strip())
                # cast salary values to integers rather than strings
                if columns[1].text.strip() != 'no salary data' and columns[1].text.strip() != '':
                    salary_str = columns[1].text.strip()
                    salary_val = int(salary_str.replace('$', '').replace(',', ''))
                    salary.append(salary_val)
                year.append(columns[2].text.strip())
                level.append(columns[3].text.strip())

        # find the max five player salaries
        print("Names:", player)
        print("Salaries:", salary)
        print("Years:", year)
        print("Levels:", level)

        salary = sorted(salary)
        num_salaries = 125

        max_salaries = salary[-num_salaries:]

        print("Max Salaries:", max_salaries)
    
        print("Average Salary:", sum(max_salaries) / num_salaries)


        
        # Create a histogram
        plt.hist(max_salaries, bins=10, color='skyblue', edgecolor='black')

        # Customize the histogram
        plt.title("Salary Distribution " + str(year[0]))
        plt.xlabel('Salary Range (1e7)')
        plt.ylabel('Frequency')

        # Show the histogram
        plt.show()


    else:
        print("Table not found on the webpage.")
else:
    print("Failed to retrieve data. Status code:", response.status_code)