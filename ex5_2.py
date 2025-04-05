"""

Relatório:

Comando: python3 ex4_server_tcp.py

- Resposta do Servidor:

Bem vindo ('127.0.0.1', 60018)!

- cURL:

curl 127.0.0.1:65432
curl: (1) Received HTTP/0.9 when not allowed

O servidor até recebeu a requisição, mas por se uma requisição HTTP/0.9 (uma versão antiga a qual versão modernas do cURL não aceitam), o terminal cURL retornou com uma mensagem de aviso dizendo que o protocolo HTTP/0.9 não é permitido.

"""