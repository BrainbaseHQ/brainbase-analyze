import os

from langchain import ConversationChain, LLMChain, OpenAI, PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts.chat import (AIMessagePromptTemplate,
                                    ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.schema import AIMessage, HumanMessage, SystemMessage

def analyze(instruction, text):

    chat = ChatOpenAI(temperature=0)

    messages = [
        SystemMessage(
            content="""
      You are InformationExtractorGPT. Your job is to parse information out of the user's text based on the following instructions:

      Instructions: """ + instruction + """

      Respond only with markdown-formatted text. 
      """)
    ]

    messages.append(HumanMessage(content=text))

    res = chat(messages)

    return res.content
