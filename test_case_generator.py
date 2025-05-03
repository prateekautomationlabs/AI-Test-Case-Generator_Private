import json
import csv
from langchain_google_genai import ChatGoogleGenerativeAI
import config
import jira_integration

llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        api_key=config.GEMINI_API_KEY)

def generate_test_cases(story_id):
    story_details = jira_integration.fetch_story_details(story_id)
    # Update the prompt to enforce a structured JSON response
    prompt = f"""
        Based on the following Jira story, generate API test cases in valid JSON format.
        Ensure the response follows this format:

        ```json
        [
            {{"test_case_id": "TC_001", "name": "Verify GET request", "url": "https://example.com/api", 
              "method": "GET", "headers": {{}}, "body": null, "expected_status_code": 200, 
              "expected_response": {{"key": "value"}} }}
        ]
        ```

        Consider above json values for example only, use actual values from user story.
        Do not include any explanation—return only the JSON array.

        Jira Story Details:
        {story_details}
        """
    generated_response  = llm.invoke(prompt)
    generated_test_cases = generated_response.content.strip()
    # Debugging step - print the response
    print(f"Generated Test Cases: {generated_test_cases}")
    # Remove any unnecessary markdown formatting (```json ... ```)
    cleaned_json = generated_test_cases.replace("```json", "").replace("```", "").strip()
    # Parse the cleaned JSON response
    try:
        test_cases = json.loads(cleaned_json)
        save_test_cases_to_csv(test_cases)
        return test_cases
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)
        raise ValueError("Invalid JSON received from Gemini API")

def save_test_cases_to_csv(test_cases, filename="test_cases.csv"):
    keys = test_cases[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(test_cases)