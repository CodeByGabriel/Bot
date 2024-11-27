# Bot
O bot é um automatizador para o Instagram desenvolvido com Selenium. Ele realiza as seguintes funções:

__Login Automático:__ Acessa o site do Instagram e faz login usando o nome de usuário e senha fornecidos.

**Busca por Hashtags:** Navega até uma página de hashtags específicas (no código atual, "culinaria").

**Coleta de Links:** Rastreia e coleta links de postagens associadas à hashtag.

**Comentários Automáticos:** Visita cada postagem coletada e deixa comentários pré-definidos de forma simulada, imitando a digitação humana.

**Fechamento Automático:** Fecha o navegador automaticamente quando o programa termina ou a instância do bot é destruída.
Acesse o Projeto para seguir o Tutorial.
Instalar python para sua plataforma www.python.org/downloads/ e marque a opção "adicionar ao PATH".

![image](https://github.com/user-attachments/assets/4f207dd9-530b-49db-bfbc-098f6b67cdb8)

Instale o selenium cmd como admin e rode "pip install selenium".
![image](https://github.com/user-attachments/assets/c5b8a905-4312-44cc-a3cd-453648d689b1)
(O Selenium é um framework gratuito, voltado aos testes de aplicações web pelo browser para automatização simulando a interação que o
usuário faria em um website)

Faça o download do geckodriver https://geckodriver.com/download/
![image](https://github.com/user-attachments/assets/9ce69636-a451-48a0-854d-ff3e79204f44)
(serve para executar os testes de aplicações Web de forma automatizada simulando as ações do usuário usando Selenium Web Driver)
Altere o endereço do geckodriver: ![image](https://github.com/user-attachments/assets/99c2f0fe-4ee9-45fe-b469-1e9175c2fa78)


Na metade do código você tem "self.comente_nas_fotos_com_a_hashtag", nesta area você podera colocar a hashtag desejada.

![image](https://github.com/user-attachments/assets/db5299e0-e2b9-426e-82d6-489e93a2fdc7)

Nos espaços de "usarname" e "password" do final do código, coloque seu usuário e sua senha, respectivamente.
![image](https://github.com/user-attachments/assets/a31c772a-7eb5-41b7-a2d0-f2bd27903e6f)
