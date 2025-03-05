#后端
from prompt_template import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
#PydanticOutputParser 是 langchain 中的一个输出解析器类，
#它的主要作用是将大语言模型（LLM）生成的输出解析为 pydantic 模型对象。
#pydantic 是一个用于数据验证和设置管理的 Python 库，通过定义数据模型可以对数据进行类型检查和验证。
#结合 PydanticOutputParser，可以确保大语言模型的输出符合我们预先定义的数据结构，
#将非结构化的文本输出转换为结构化的数据对象，便于后续的处理和使用。
from langchain.prompts import ChatPromptTemplate
from xiaohongshu_model import Xiaohongshu

import os
openai_api_key = os.getenv("OPENAI_API_KEY")
def generate_xiaohongshu(theme, openai_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key,openai_api_base="https://chatapi.littlewheat.com/v1/")
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    #PydanticOutputParser 是 langchain 中的一个类，用于将大语言模型的输出解析为 pydantic 模型对象。
#pydantic_object=Xiaohongshu：这里的 Xiaohongshu 应该是一个 pydantic 模型类,
    #通过将其传递给 PydanticOutputParser，告诉解析器按照 Xiaohongshu 模型的结构来解析大语言模型的输出。
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
#返回一段文本，描述了大语言模型输出应该遵循的格式，以确保输出能够被 PydanticOutputParser 正确解析为 Xiaohongshu 模型对象。
        "theme": theme
    })
    return result

#print(generate_xiaohongshu("大模型", os.getenv("OPENAI_API_KEY")))
