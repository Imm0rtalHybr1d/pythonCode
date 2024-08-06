import google.generativeai as genai

# Replace YOUR_API_KEY with your actual API key that you can get from https://cloud.google.com/
API_KEY: str = "your AI key"
genai.configure(api_key=API_KEY)
model: genai.GenerativeModel = genai.GenerativeModel('gemini-1.5-flash')

previous_prompt = ""

def get_prompt() -> None:
    global previous_prompt
    
   
    print('Enter a prompt (or type "exit" to quit):') #tell user to give us a promt
    user_prompt: str = input()
    print(f'{''}')
    
    full_prompt = f"i want you to provide information on diffrent exercises that a use will ask you, keep in mind that your answers should only included exercises that can be done with free weights as the user does not have gym machines the user looking for an informative and consise, yet easy to read and understand response.Be Clear and Concise.for example if a user asks 5 types of leg exercises, your answer should name the exercises, a step by step on how to do it, which muscle it affects and any relavant information to the user doing this exercise.Use numbered points for main headings e.g 1.barbell curl, bullet point for sub headings to organize your response.Consider that the user's main goal is to gain muscle and strength. User's prompt: {user_prompt}"

    #uses model.generate_content(full_prompt) to send the prompt thru to google gemini AI
    #stores google gemini AI response in the response variable
    response: genai.Response = model.generate_content(full_prompt)
    
    ai_response: str = response.text
    print(ai_response)
    
    print(f'{''}')
    save: str = input('Would you like to save the response to a Markdown file? y/n')    
    if save == 'y':
        save_response(ai_response)

def save_response(ai_response:str) -> None:
    #Creates a markdown file and writes the response to it 
    with open("output.md", "w") as file:
        for line in ai_response.splitlines():
            file.write(f"{line}\n")
        print('Info saved to output.md')
        
def main():
    get_prompt()
    save_response()

if __name__ == "__main__":
    main()
