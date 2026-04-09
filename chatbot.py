from responses import RESPONSES, FALLBACK

query_count = 0

def normalize(text):
    """Clean and standardize user input before matching."""
    return text.lower().strip()

def get_response(user_input):
    """
    Match user input against keyword dictionary.
    Priority: exact match first, then partial keyword match.
    Returns a string response.
    """
    global query_count

    cleaned = normalize(user_input)

    if not cleaned:
        return "Please type something. Try 'help' to see available commands."

    status_triggers = ["show-status", "show status", "showstatus", "status"]
    if cleaned in status_triggers:
        return (
            f"EduBot System Status\n"
            f"  Status        : Online\n"
            f"  Version       : 1.0.0\n"
            f"  Queries served: {query_count}\n"
            f"  Engine        : Python String Matching\n"
            f"  Server        : Flask 3.1.3"
        )

    if cleaned == "clear":
        return "__CLEAR__"

    query_count += 1

    if cleaned in RESPONSES:
        return RESPONSES[cleaned]

    for keyword in RESPONSES:
        if keyword in cleaned:
            return RESPONSES[keyword]

    return FALLBACK