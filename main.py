import openai

# Pega a chave de api dentro do arquivo txt
with open("key.txt", "r") as key:
    chave = key.readlines()[0]


# Classe responsável por conctar ao chatGPT
class ChatGPT:
    
    
    openai.api_key = chave
    
    def __init__(self) -> None:
        while True:
            print('-'*30)
            print('ChatGPT\n')
            response = input(
                "Perguntar: Digite 1\n\
Sair: Digite 0\n\
                \nSua Reposta: "
                ).strip()
            
            if response == '0':
                print('\nChat encerrado!')
                break
            elif response == '1':
                try:
                    responseChatGPT = self.buscar()
                except Exception as e:
                    print(f'ERRO: {e}')
                    print('Tente novamente!')
                else:
                    print(f"\nR: {responseChatGPT}\n")
            else:
                print(
                    'Opção inválida!\n'
                )

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
        pergunta = input(
            '\nRealize sua pergunta ao ChatGPT: '
            ).lower().strip()
        return pergunta

if __name__ == "__main__":    
    ChatGPT()