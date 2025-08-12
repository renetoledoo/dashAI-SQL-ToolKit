# Insight ReAct Agents - Ollama + LangChain

Este é um projeto simples de demonstração para uso de agentes baseados em LLM (Language Models) com LangChain e Ollama local, aplicados a consultas em banco de dados MySQL.

> [!] Este é um projeto apenas para teste com Ollama local, com modelo simples.

---

## Sobre o Projeto

Este projeto demonstra como criar um agente conversacional que responde perguntas sobre dados de vendas de uma empresa, consultando diretamente o banco de dados via SQL. A consulta e a lógica são controladas por um modelo Ollama rodando localmente, integrado com LangChain.

### Objetivos principais

- Demonstrar integração LLM com banco de dados SQL via LangChain.  
- Mostrar fluxo básico de interação tipo REACT agent.  

---

## Tecnologias e Bibliotecas

- Python  
- LangChain  
- OllamaLLM (modelo local)  
- MySQL com PyMySQL  

---
<img width="804" height="290" alt="image" src="https://github.com/user-attachments/assets/91b25341-58c3-4600-a0a3-ea5ddc962670" />

## Como funciona o REACT Agents

1. **Thought:**  
   O agente pensa e descreve seu raciocínio para responder à pergunta ou resolver a tarefa.

2. **Action:**  
   O agente decide qual ferramenta (ex.: uma função, um banco de dados, uma API) usar para obter mais informações.

3. **Action Input:**  
   Fornece os dados necessários para executar essa ação.

4. **Observation:**  
   Recebe o resultado da ação executada.

5. O ciclo se repete várias vezes, permitindo que o agente faça consultas, filtre respostas e raciocine passo a passo.

6. Finalmente, o agente dá a **Final Answer**, uma resposta conclusiva e clara baseada nos dados obtidos.
