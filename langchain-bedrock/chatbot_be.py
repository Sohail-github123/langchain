import os
import boto3
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def demo_chatbot():
    demo_llm = Bedrock(
        credentials_profile_name='default',
        model_id='meta.llama2-70b-chat-v1',
        model_kwargs={
        "temperature": 0.9,
        "top_p": 0.5,
        "max_gen_len": 512})
    return demo_llm

#     return demo_llm.predict()
# response = demo_chatbot('hi, what is the temprature in Mumbai ?')
# print(response)

def demo_memory():
    llm_data=demo_chatbot()
    memory = ConversationBufferMemory(llm=llm_data, max_token_limit= 512)
    return memory

def demo_conversation(input_text,memory):
    llm_chain_data = demo_chatbot()
    llm_conversation= ConversationChain(llm=llm_chain_data,memory=memory,verbose=True)

    chat_reply = llm_conversation.predict(input=input_text)
    return chat_reply
