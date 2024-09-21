import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv(r"D:\Data_analysis_System\Data_Analysis_System-20240921T023929Z-001\Data_Analysis_System\Backend\Titanic-Dataset.csv")
num_rows, num_columns = df.shape
# Display the first few rows of the DataFrame
column_names = df.columns.tolist()
print(column_names)
df_final=df.head(10)
# print(df_final)
Today_date="8-7-2024"
location= r"D:\Data_analysis_System\Data_Analysis_System-20240921T023929Z-001\Data_Analysis_System\Backend\Titanic-Dataset.csv"
location_1="D:\Data_analysis_System\Data_Analysis_System-20240921T023929Z-001\Data_Analysis_System\Backend\output_graph"
# num_rows=""
# """Prompt to generate Python code"""
# Today is {today_date}.
# You are provided with a pandas dataframe (df) with {num_rows} rows and {num_columns} columns.
# This is the result of `print(df.head({rows_to_display}))`:
# {df_head}.

# When asked about the data, your response should include a python code that describes the dataframe `df`.
# Using the provided dataframe, df, return the python code and make sure to prefix the requested python code with {START_CODE_TAG} exactly and suffix the code with {END_CODE_TAG} exactly to get the answer to the following question:
S_prompt=f"""
You are an Expert Python developer . Your role is to write python code using Dataframe and users questions. You just write python code, not included any text in your reponse.
Today is {Today_date}.You are provided with a pandas dataframe location is df={location} with {num_rows} rows and {num_columns} columns.This is the columns name: {column_names}. This is the first 10 data from dataset: {df_final}.
When asked about the data, your response should include a python code that describes the dataframe `df` and provide response for users question about data. Do not include any comment in your code.
Using the provided dataframe, df, return the python code. Output possible type is (possible values "string", "number", "dataframe", "plot"). You should to return output like this conversasional way in your code, You must provide conversational response while you provide output in your code,I want descriptive conversasional answer. in your code start add prefix "# Start" and when end add "# End", Do not include (```,python,```) within your code. All text you write must within code. Without code do not write any text in your response.
load the dataset like this format.
df = pd.read_csv(r'location')
When you have graph,plot or etc like image, you have saved that graph in this location={location_1} and image name must i want unique and use unique number with image. Without saved the plot, you don,t show the plot or images directly. 
"""
# print(S_prompt)
from groq import Groq
user_questions="Provide the five oldest people, who died in the dataset then provide plot of the ages vs number of people died. How many data in here? "
client = Groq(api_key="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")
completion = client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": S_prompt,
        },
        {
            "role": "user",
            "content": user_questions,
        }
    ],
    temperature=0,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)
import io
import sys

# Initialize an empty string to store the result
result = ""

for chunk in completion:
    content = chunk.choices[0].delta.content or ""
    
    # Print the content
    print(content, end="")
    
    # Append the content to the result variable
    result += content

# Initialize a variable to capture the exec() output
output = None
error_message = None

# Redirect stdout to capture print output
output_capture = io.StringIO()
sys.stdout = output_capture

try:
    # Execute the code stored in result
    exec(result)
    # Capture the output of the exec(result)
    output = output_capture.getvalue()

except Exception as e:
    # Capture the error message if there's an error
    error_message = str(e)

finally:
    # Reset stdout to its original state
    sys.stdout = sys.__stdout__

# Print or handle the output or error message
if error_message:
    print(f"Error found in this code: {error_message}")
else:
    print(f"Execution output: {output}")

