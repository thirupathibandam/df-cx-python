import os, uuid

SERVICE_ACCOUNT_FILE = "Service account file"
PROJECT_ID = "project id"
LOCATION_ID = "id of the agent location"
AGENT_ID = "id of the agent"
LANGUAGE_CODE = "en-us"

agent = f"projects/{PROJECT_ID}/locations/{LOCATION_ID}/agents/{AGENT_ID}"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE

TRAIN_FILE = "data/AskUbuntuCorpus_train.csv"
TEST_FILE = "data/AskUbuntuCorpus_test.csv"
INTENT_COLUMN = "intent"
TEXT_COLUMN = "input"
