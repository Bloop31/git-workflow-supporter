from config import MIN_COMMIT_LENGTH
def analyze_commit(message):
    message=message.lower()
    if len(message)<10:
        return "Too short - make it descriptive"
    bad_words=["update", "fix", "changes"]
    if message in bad_words:
        return "Be specific"
    action_words=["add","fix","update", "remove", "refactor", "implement"]
    if not any(word in message for word in action_words):
        return "Use action verbs like 'add', 'fix', 'update'."
    return "Good commit message."