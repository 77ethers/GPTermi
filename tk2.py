import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import requests
from tkterminal import Terminal
import json


api_key="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"

def send_to_gpt():
    user_input = user_entry.get()
    user_entry.delete(0, tk.END)

    # Display user input in the terminal
    # terminal_display.insert(tk.END, f"User: {user_input}\n")

    # Prepare the payload for the API request
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role":"system", "content":"you are the most helpful command line assistant ever created by openAI. Your job is to provide maximum 3 sentance answers(in new lines) to the users who ask their doubts on linux terminal commands, shell programming, bash scripting commands, and topics related 'only' to them - mostly doubts on commands. You never switch context from linux terminal no matter however the user asks for."},
            {"role": "user", "content": user_input}
                     ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"  # Replace with your actual API key
    }

    # Send the input to the ChatGPT API and get the response
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    response = response.json()
    print(response)
    gpt_response = response['choices'][0]['message']['content']

    # Display GPT response in the GPT response display section
    gpt_response_display.config(state=tk.NORMAL)
    gpt_response_display.delete('1.0', tk.END)
    gpt_response_display.insert(tk.END, f"GPTermi: {gpt_response}\n")
    gpt_response_display.config(state=tk.DISABLED)

# Set up the main window
root = tk.Tk()
root.title("GPTermi")

# Create the terminal display area
terminal_display = Terminal(pady=10, padx=10)
terminal_display.pack(expand=True, fill='both')
terminal_display.shell = True
terminal_display.basename = "GPTermi$"
# terminal_display.insert(tk.END, "tkterminal$\n")
# terminal_display.config(state=tk.DISABLED)

# Create the user input area
user_entry = tk.Entry(root, width=100)
user_entry.insert(tk.END,"USER Input--> ")
user_entry.pack(padx=10, pady=5)
user_entry.bind("<Return>", lambda event: send_to_gpt())

# Create the GPT response display area (read-only)
gpt_response_display = ScrolledText(root, height=15, width=100)
gpt_response_display.pack(padx=10, pady=10)
gpt_response_display.config(state=tk.DISABLED)

root.mainloop()
