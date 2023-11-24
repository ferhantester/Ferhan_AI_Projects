from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os
os.environ['OPENAI_API_KEY'] = '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'
llm2 = OpenAI(temperature=0.7)


def generate_state_name_and_tourist_places(country_name):
    prompt_template_name1 = PromptTemplate(input_variables=['country_name'],
                                           template='Suggest me any one state of {country_name}')
    country = LLMChain(llm=llm2, prompt=prompt_template_name1, output_key='state_name')

    prompt_template_name2 = PromptTemplate(input_variables=['state_name'],
                                           template='Give a list of tourist places within {state_name}')
    state = LLMChain(llm=llm2, prompt=prompt_template_name2, output_key="tourist_places")
    chain = SequentialChain(chains=[country, state], input_variables=['country_name'], output_variables=[
     'state_name', 'tourist_places'])
    response = chain({'country_name': country_name})
    return response









