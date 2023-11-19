from openai import OpenAI
import gradio as gr

openai = OpenAI(
   api_key= "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"
 )

messages = [
    {"role":"system", "content": "This is a chatbot that only answer questions related to Plants. For questions not related to Plants, reply with Sorry, I do not know."},
    {"role":"user","content": "What is a Plant?"},
    {"role":"assistant","content": "It is a living organism of the kind exemplified by trees, shrubs, herbs, grasses, ferns, and mosses, typically growing in a permanent site, absorbing water and inorganic substances through its roots, and synthesizing nutrients in its leaves by photosynthesis using the green pigment"}
]

def generate_response(prompt):
    if prompt == "Hello":
        reply = "Hello, I'm Tom! How can I help you?"
    
    else:
        messages.append({"role": "user", "content": prompt})
        chat = openai.chat.completions.create(
            model="gpt-3.5-turbo", max_tokens = 20, messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})

   
    return reply


def my_chatbot(input, history):
    history = history or []
    my_history = list(sum(history, ()))
    my_history.append(input)
    my_input = ' '.join(my_history)
    output = generate_response(my_input)
    history.append((input, output))
    return history, history

with gr.Blocks() as demo:
    gr.Markdown("""<h1><center>Plant Chatbot</center></h1>""")
    chatbot = gr.Chatbot()
    state = gr.State()
    text = gr.Textbox(placeholder="Explore the wonders of the plants! Ask me anything")  # Adjust width
    submit = gr.Button("SEND")
    submit.click(my_chatbot, inputs=[text, state], outputs=[chatbot, state])

demo.launch(share = True)