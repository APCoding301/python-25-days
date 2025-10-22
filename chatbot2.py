from datetime import datetime
import re

"""
V2: Added history to chats and took an OOP approach
"""


# 1. Create a helper method for recognising terms
def contains(terms: list[str], content: str) -> bool:
    matches: list[bool] = []
    for term in terms:
        matches.append(term in content.lower())
    return any(matches)


# 2. Create the chatbot class
class ChatBot:
    def __init__(self, name: str) -> None:
        self.history: list[str] = []
        self.name = name

    # 3. Code the response functionality
    def response(self, text: str) -> str:
        text = text.lower()

        # 1. follow-up: if user says "tomorrow" right after asking about the weather
        if contains(['tomorrow'], text) and contains(['weather'], self.history[-1]):
            return 'Tomorrow looks sunny with a high of 25 °C.'

        # 2. normal intents
        if contains(['hello', 'hi'], text):
            #text += 'Hello there!'
            return 'Hello there!'
        elif contains(['goodbye', 'bye'], text):
            return 'Talk to you later!'
        elif contains(['what time is it', 'current time'], text):
            curr_time_str = datetime.now().strftime("%H:%M:%S")
            text += f' The time is -- {curr_time_str}'
            return text
        elif contains(['weather'], text):
            return "It’s partly cloudy and 22 °C right now."
        elif contains(['help', 'commands'], text):
            return (
                'I understand: hello/hi, goodbye/bye, what time is it/current time, '
                'weather, tomorrow (after weather), stopwatch (after time) and help/commands.'
            )

        # 3. follow-up: if user says "stopwatch" right after asking for the current time..
        # Return how much time has elapsed since the last "time request"
        if contains(['stopwatch'], text) and contains(['what time is it', 'current time'], self.history[-1]):
            timestamp_pattern = r"\d{2}:\d{2}:\d{2}"
            match = re.search(timestamp_pattern, self.history[-1])
            if match:
                timestamp_str = match.group(0)
                time_format = "%H:%M:%S"
                time_start_str = timestamp_str
                time_now_str = datetime.now().strftime(time_format)
                elapsed_time = datetime.strptime(time_now_str, time_format) - datetime.strptime(time_start_str, time_format)
                return f'Elapsed seconds between "time" and "stopwatch" requests: {elapsed_time.total_seconds():.2f}s.'
        
        return "Sorry... I can't answer that right now."

    # 4. Add memory to the bot
    def remember(self, text: str) -> None:
        self.history.append(text.lower())
        if len(self.history) > 2:
            # keep only most-recent 2 messages
            self.history.pop(0)

    # 5. Run the bot
    def run(self) -> None:
        print("Type 'help' for commands. Type 'bye' to quit.\n")
        while True:
            user_input: str = input('You: ')
            bot_reply: str = self.response(user_input)
            print(f'{self.name}: {bot_reply}')

            # exit if user said goodbye
            if contains(['bye', 'goodbye'], user_input):
                break

            # remember after responding
            # special case: for 'current time' and 'what time is it', remember both user request and the response.
            # This will enable the 'stopwatch' follow-up to work
            # In this particular case, bot_reply contains the timestamp as well as the user request input string.
            if contains(['what time is it', 'current time'], user_input):
                self.remember(bot_reply)
            else:
                self.remember(user_input)


def main() -> None:
    bot: ChatBot = ChatBot('Bob')
    bot.run()


if __name__ == "__main__":
    main()

# Homework:
# 1. Try creating more responses that use the chat history to ask follow-up questions.
# NAILED IT! --AP -- Oct 21, 2025
# I added a "stopwatch" follow-up that works after asking for the current time.
# When the user asks for the current time, the bot responds with the time and remembers that response.
# If the user then asks for "stopwatch", the bot calculates and returns the elapsed time since the last time request.