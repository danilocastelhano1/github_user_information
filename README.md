# Script para obter dados de um usuário no Github

Script desenvolvido em python, para buscar informações 
de um determinado usuário no github usando a API pública deles, 
e salvar em um arquivo .txt


# Executando o arquivo

Para executar um arquivo é simples, em um terminal ou prompt de comando 
com python e o pip instalado, navegue até o diretório do arquivo main.py, 
e crie uma venv: `python -m venv nome_da_venv`, 
após isso, ative-a: `source nome_da_venv/bin/activate # no Windows use: nome_da_venv\Scripts\activate`,
depois disso, instale os requerimentos para o script funcionar: `pip install -r requeriments.txt`
agora só executar o comando usando: `python main.py --username nome_do_usuario_a_pesquisar` se tudo correu bem, no mesmo diretório do arquivo `main.py` aparecerá um arquivo txt com os dados do usuário pesquisado na API do github.

## Testando o script
Para testar o script, devemos seguir os passos:
Navegar até o diretório onde se encontra o arquivo `main.py` e executar: python -m unittest tests`