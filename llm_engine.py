from langchain import hub
from langchain_ollama.llms import OllamaLLM
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate

model = OllamaLLM(model='phi3')
bd = SQLDatabase.from_uri('mysql+pymysql://root:*****@localhost:3306/empresa_vendas')

descricao_schema = '''
O banco de dados empresa_vendas possui as seguintes tabelas e colunas:

- regioes:
    - id_regiao
    - nome_regiao

- clientes:
    - id_cliente
    - nome_cliente
    - id_regiao (referência informal para regioes)
    - data_cadastro

- produtos:
    - id_produto
    - nome_produto
    - categoria
    - preco
    - custo

- vendas:
    - id_venda
    - id_cliente (referência informal para clientes)
    - id_produto (referência informal para produtos)
    - quantidade
    - data_venda
'''

prompt = f'''
Você é um assistente especializado em responder perguntas relacionadas a vendas da empresa.
Use somente as ferramentas disponibilizadas para obter informações do banco de dados.
Não invente respostas nem faça suposições fora do que as ferramentas retornarem.
Responda sempre em português brasileiro de forma clara e objetiva.

Esquema do banco de dados:
{descricao_schema}

Siga estritamente o formato de interação do agente:
- Sempre descreva seu raciocínio com "Thought:"
- Para realizar uma ação, use "Action:" seguido do nome da ferramenta disponível
- Use "Action Input:" para enviar a entrada da ação
- Aguarde o resultado da ação em "Observation:"
- Após investigar, dê a resposta final com "Final Answer:"

Pergunta: {{input}}
'''


toolkit = SQLDatabaseToolkit(
    db=bd,
    llm=model
)

hub_prompt = hub.pull('hwchase17/react')

print(hub_prompt)

agent = create_react_agent(
    llm=model,
    tools=toolkit.get_tools(),
    prompt=hub_prompt
)

agent_instancia = AgentExecutor(
    agent=agent,
    tools=toolkit.get_tools(),
    verbose=True,
    # max_iterations= 5,
    handle_parsing_errors=True
)


prompt_template = PromptTemplate.from_template(prompt)

output = agent_instancia.invoke({
    'input': prompt_template.format(input='Quais são foram os clientes que mais venderam')
})


print(output.get('output'))
