import openai

# Pega a chave de api dentro do arquivo txt
with open("key.txt", "r") as key:
    chave = key.readlines()[0]


# Classe responsável por conctar ao chatGPT
class ChatGPT:
    
    
    openai.api_key = chave
    
    def __init__(self) -> None:
        pass

    def buscar(self) -> str:
        
        busca = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.perguntar(),
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.5
        )
        
        resposta = busca.choices[0].text
        return resposta.strip()

    def perguntar(self) -> str:
        pergunta = input('Realize sua pergunta ao ChatGPT: ').lower().strip()
        return pergunta

if __name__ == "__main__":
    print(ChatGPT().buscar())