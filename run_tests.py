import argparse
import test_case_generator
import pytest
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--story_id", required=True, help="Specify the JIRA story ID")
    args = parser.parse_args()

    # Set the story_id as an environment variable
    os.environ["STORY_ID"] = args.story_id

    # Generate test cases dynamically
    test_case_generator.generate_test_cases(args.story_id)

    # Define the path for the HTML report
    html_report_path = os.path.join(os.getcwd(), "report.html")

    # Run pytest with both allure and pytest-html options
    pytest.main([
        f"--html={html_report_path}",  # For pytest-html report
        "--self-contained-html",
        "--log-cli-level=DEBUG"
    ])

if __name__ == "__main__":
    main()