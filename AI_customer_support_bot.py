# import requests library for making GET/POST requests to Deepseek API
import requests
# import Gradio for creating interactive web interface
import gradio as gr

import re

# deepSeeek AI Url from local using ollama

OLLAMA_URL = "http://localhost:11434/api/generate"


# the database that the chat box produce response on 
FAQ_Database = {
    "orders": "To place an order, browse products, add them to your cart, and proceed to checkout. Fill in your shipping details and complete the payment process.",
    "shipping":"We offer standard (5–7 days), expedited (2–3 days), and overnight shipping. Availability depends on your location. After your order ships, you’ll receive a tracking number via email or SMS. You can also track it in your 'My Orders' section.",
    "payments": "We accept Visa, Mastercard, PayPal, Apple Pay, and Google Pay.",
    "return and refunds":"Items can be returned within 30 days of delivery. They must be unused and in original packaging.Go to 'My Orders', select the item, and click 'Return Item'. Follow the prompts to generate a return label. Refunds are processed within 5–10 business days after we receive your returned item.",
    "account":"Click the 'Sign Up' button on the homepage and fill in your email, password, and other details. Click 'Forgot Password?' on the login page and follow the steps to reset your password via email.",
    "products": "Our website reflects real-time stock levels. If a product is out of stock, you can sign up to get notified when it's back.",
    "contact us": "You can reach us via live chat, email at support@example.com, or call 1-800-123-4567 (Mon–Fri, 9 AM–6 PM EST)."
}

#Prompt to DeepSeek AI
def chat_bot(user_question):
    prompt = f"Find the best match from the FAQ database for this customer query:\n\n'{user_question}'\n\n" \
             f"Available FAQs: {list(FAQ_Database.keys())}\n" \
             f"Match the relevant query with FAQs and provide a response"
    
    data = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    ai_response = requests.post(OLLAMA_URL, json= data)
    #print("---------------------------------------")
    #print(ai_response.json().get("response"))
    #print("---------------------------------------")


    if ai_response.status_code == 200:
        response_key = ai_response.json().get("response", "Opps, I don't have a specific answer for that question.").lower() # Assuming the key is in the 'response' field
        return FAQ_Database.get(response_key, response_key)
    else:
        return "Unable to process your request"


if __name__ == "__main__":
    sample_query = "How can I return a product?"
    print("-------------------------------------------------------- ")
    print("---------------------Chatbot Response--------------------")
    print(chat_bot(sample_query))