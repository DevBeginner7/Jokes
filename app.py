from flask import Flask, render_template, request, jsonify
import pyjokes
import random

app = Flask(__name__)

# emojis for fun
EMOJIS = ["😂", "🤣", "😆", "😜", "🤡", "💀"]

# sarcasm responses
SARCASM_LINES = [
    "Oh wow, you again 🙄",
    "Let me guess... you want a joke? 😏",
    "I suppose I *have* to entertain you now 😒",
    "Alright... but don't laugh too hard 😑"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "").lower()
    sarcasm_mode = data.get("sarcasm", False)

    emoji = random.choice(EMOJIS)

    # choose joke category randomly
    category = random.choice(["neutral", "chuck", "all"])

    if "joke" in user_message:
        joke = pyjokes.get_joke(category=category)
        
        if sarcasm_mode:
            reply = f"{random.choice(SARCASM_LINES)}\n\n{joke} {emoji}"
        else:
            reply = f"{joke} {emoji}"

    elif "hi" in user_message or "hello" in user_message:
        if sarcasm_mode:
            reply = "Oh great, greetings 🙄 What do you want now?"
        else:
            reply = "Hey there 😄 Ask me for a joke!"

    else:
        if sarcasm_mode:
            reply = "I only tell jokes... not solve your life problems 😏"
        else:
            reply = "I only tell jokes 😂 Try asking for one!"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)