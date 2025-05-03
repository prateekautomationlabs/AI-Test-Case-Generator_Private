from jira import JIRA
import config

def get_jira_client():
    jira_options = {"server": config.JIRA_SERVER}
    return JIRA(options=jira_options, basic_auth=(config.JIRA_USER, config.JIRA_API_TOKEN))

def fetch_story_details(story_id):
    jira = get_jira_client()
    story = jira.issue(story_id)
    print("printing all story fields")
    print(story.raw)
    story_description = story.fields.description
    acceptance_criteria = story.fields.customfield_10036  # Replace with actual field ID
    return f"Description: {story_description}\nAcceptance Criteria: {acceptance_criteria}"