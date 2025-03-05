import pdfplumber
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import AIMessage, HumanMessage
import gradio as gr

# import the model from langchain
model = OllamaLLM(model="llama3.1")
# define the model
workflow = StateGraph(state_schema=MessagesState)


# define the model
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}


# define the single state node in the graph
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)
# save the memory
memory_saver = MemorySaver()
aiapp = workflow.compile(checkpointer=memory_saver)
# config
config = {"configurable": {"thread_id": "abc123"}}


def extract_pdf_book(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text.strip()


# summerize the text using the model and context
def summary(text):
    query = "summarize this in a manageable chunks and help the user understand better and fast: {}".format(text)
    input_messages = [HumanMessage(query)]
    output = aiapp.invoke({"messages": input_messages}, config)
    return output["messages"][-1].content


def chat(user_input):
    input_messages = [HumanMessage(user_input)]
    output = aiapp.invoke({"messages": input_messages}, config)
    return output["messages"][-1].content


def asmain(file):
    # pages for the pdf and chatbot
    if not file:
        return "No file uploaded."
    if file.name.endswith(".pdf"):
        text = extract_pdf_book(file)
    else:
        return "Unsupported file type."
    print("Summarizing the file...")
    resposness = summary(text)
    return resposness


# gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# PDF Summarizer and Chatbot")
    gr.Markdown("by rohith gona (rohithgg)[https://rohithgg.github.io/rohithsresume]")
    gr.Markdown(
        "Upload a PDF file and the model will summarize it. The summarized text will help you understand the content quickly and efficiently. Simply upload your PDF file using the button below, and the model will process it to provide a concise summary.")
    gr.Markdown("- get your groq api key from [here](https://groq.com/)"
                "- run the model "
                "upload a PDF file (Supported file types: PDF)"
                "- and get summaries."
                "- you can also chat with the model using the chat interface below."
                )

    with gr.Tabs() as tabs:
        with gr.Tab("PDF Summarizer"):
            gr.Interface(
                fn=asmain,
                inputs=gr.File(file_types=[".pdf"]),
                outputs=[gr.Textbox(label="Summary")]
            )
        with gr.Tab("Chatbot"):
            gr.Interface(
                fn=chat,
                inputs=gr.Textbox(label="Chat with the model"),
                outputs=[gr.Textbox(label="Response")]
            )

demo.launch(share=True)