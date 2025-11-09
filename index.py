from google import genai
from data import read_data
from datetime import datetime
from analysis import run_analysis
import pandas as pd


client = genai.Client()
data = read_data()
start_index = 0
input_data = data.loc[start_index:].copy()


def run(df):
    try:
        for i, row in input_data.iterrows():
            query = row["comment"]
            expected_output = row[i, "Validated_Labels"]

            prompt = f"""
            You are an experienced sentiment analyst studying students’ feedback on mental health services.
            Categorize the following response into one of these four labels: Satisfied, Dissatisfied, Mixed, Neutral.

            The specific criteria for each category are as follows. 
            (1) “Satisfied”: at least 75% of the language expressed satisfaction, with minimal suggestions for improvement. 
            (2) “Dissatisfied”: at least 75% of the language indicated discontent or suggestions for enhancement, with little mention of satisfaction. 
            (3) “Mixed”: expressions of satisfaction and dissatisfaction/suggestions were approximately evenly split, with each constituting about 50%. 
            (4) “Neutral”: no clear emphasis on satisfaction, dissatisfaction, or suggestions for improvement

            Question: “What mental health or wellness services and supports provided by your college are working well? What aspects need more attention?”
            Response: {query}

            Output: 
            """

            response = client.models.generate_content(
                model="gemini-2.5-flash", contents=prompt
            )
            response = response.text.strip().lower()
            df.loc[i, "Predicted_labels"] = response
            print(f"{i}. Model Output: {response}, Actual label = {expected_output}")

    except Exception as e:
        print("An error occurred")

    return df, start_index, i


output_df, start_idx, idx = run(input_data)
partial_output_df = input_data.loc[start_idx:idx]
print(f"writing csv from {start_idx} to {idx}")
partial_output_df.to_csv(f"Output_{datetime.now()}.csv")

run_analysis(df=output_df)
