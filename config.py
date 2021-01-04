import os, uuid

SERVICE_ACCOUNT_FILE = "Service account file"
PROJECT_ID = "project id"
LOCATION_ID = "id of the agent location"
AGENT_ID = "id of the agent"
LANGUAGE_CODE = "en-us"
TIME_ZONE="America/New_York"
DEFAULT_FLOW_ID = "00000000-0000-0000-0000-000000000000"

agentPath = f"projects/{PROJECT_ID}/locations/{LOCATION_ID}/agents/{AGENT_ID}"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE

AGENT_NAME = "mytestagent5"

TRAIN_FILE = "data/AskUbuntuCorpus_train.csv"
TEST_FILE = "data/AskUbuntuCorpus_test.csv"
INTENT_COLUMN = "intent"
TEXT_COLUMN = "input"
