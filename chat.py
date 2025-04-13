# from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# from langchain_google_vertexai import GemmaChatLocalHF
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langgraph.checkpoint.memory import MemorySaver


load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

repo_id = "google/gemma-2-2b-it"
memory = MemorySaver()


class State(TypedDict):
    messages: Annotated[list, add_messages]


llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    max_new_tokens=1024,
    temperature=0.5,
    huggingfacehub_api_token=HUGGINGFACE_API_KEY,
)
chat_model = ChatHuggingFace(llm=llm)


def chatbot(state: State):
    return {"messages": [chat_model.invoke(state["messages"])]}


def chat_res(prompt: str):
    config = {"configurable": {"thread_id": "1"}}

    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot", chatbot)

    # Any time a tool is called, we return to the chatbot to decide the next step
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)

    graph = graph_builder.compile(checkpointer=memory)

    graph.invoke(
        {"messages": [{"role": "user", "content": prompt}]},
        config,
        # stream_mode="values",
    )

    final_state = graph.get_state(config)
    msg = final_state.values.get("messages")
    return msg[-1].content
