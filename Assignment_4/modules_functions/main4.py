# 3. External Modules (Third-party Libraries)

# External modules (also called third-party libraries) are packages that are not built into Python by default. You have to install them separately using a tool like pip.

import requests
import json

# Send a GET request to a public API
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("✅ Request Successful!")
    print(f"Status Code: {response.status_code}\n")

    # Convert JSON response to Python dictionary
    data = response.json()

    # Pretty print the JSON data
    print("📄 Response Data:")
    print(json.dumps(data, indent=4))
else:
    print(f"❌ Request Failed with Status Code: {response.status_code}")


print("**********************************")

#  numpy — For working with arrays and math
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr * 2)      # Output: [2 4 6 8]
print(np.mean(arr)) # Average: 2.5

print("**********************************")
import pandas as pd

data = {'Name': ['Ali', 'Sara'], 'Marks': [90, 85]}
df = pd.DataFrame(data)
print(df)

