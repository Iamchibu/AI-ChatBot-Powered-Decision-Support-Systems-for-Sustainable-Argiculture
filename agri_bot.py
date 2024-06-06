from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import requests

# Create a new instance of a ChatBot
bot = ChatBot(
    'AgriBot',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ]
)

trainer = ListTrainer(bot)

# Training the chatbot with sample data (NLP Methodologies)
trainer.train([
    "What is AI in agriculture?",
    "AI in agriculture involves using technologies such as machine learning and big data analytics to enhance productivity and sustainability.",
    
    "What are Decision Support Systems (DSS) in agriculture?",
    "Decision Support Systems (DSS) assist farmers in making informed decisions by leveraging historical data and statistical models, and now increasingly AI technologies.",
    
    "How can AI improve crop yields?",
    "AI can analyze vast amounts of real-time data to provide accurate predictions and recommendations, potentially increasing crop yields by up to 30% while reducing resource usage.",
    
    "What are the benefits of machine learning in agriculture?",
    "Machine learning can predict pest outbreaks, soil fertility levels, and optimal harvest times by analyzing patterns and anomalies in data.",
    
    "How can deep learning help in agriculture?",
    "Deep learning can identify crop diseases from images captured by drones or smartphones, providing immediate diagnostic feedback to farmers.",
    
    "What are the challenges in adopting AI in agriculture?",
    "Challenges include data quality, system interoperability, high costs, knowledge gaps among farmers, and ethical and privacy concerns.",
    
    "What future advancements are expected in AI for agriculture?",
    "Ongoing research focuses on improving AI algorithms and user interfaces, as well as policy interventions and educational programs to increase farmers' awareness and skills in using AI technologies."
])

# Function to fetch real-time weather data (Integration with External Systems)
def get_weather(location):
    api_key = "your_api_key_here"
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}"
    response = requests.get(url)
    data = response.json()
    if 'current' in data:
        return data['current']
    return "Weather data not available."

# Function to get a response from the chatbot
def get_response(user_input):
    if "weather" in user_input.lower():
        location = user_input.split()[-1]
        weather_info = get_weather(location)
        return f"The current weather in {location} is {weather_info['temperature']}°C with {weather_info['weather_descriptions'][0]}."
    else:
        response = bot.get_response(user_input)
        return response

# Example interaction
if __name__ == "__main__":
    print("Welcome to AgriBot! Ask me anything about AI in agriculture.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("AgriBot: Goodbye! Have a great day!")
                break
            
            response = get_response(user_input)
            print(f"AgriBot: {response}")
        
        except(KeyboardInterrupt, EOFError, SystemExit):
            break
