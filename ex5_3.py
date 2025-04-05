"""

Relatório:

Primeiro comando: python -m http.server 8000
Segundo comando: curl 127.0.0.1:8000

- Comportamento do Servidor:

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
127.0.0.1 - - [05/Apr/2025 15:42:06] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Apr/2025 15:42:44] "GET / HTTP/1.1" 200 -

- Resposta do cURL:

<!DOCTYPE HTML>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Directory listing for /</title>
</head>
<body>
<h1>Directory listing for /</h1>
<hr>
<ul>
<li><a href=".git/">.git/</a></li>
<li><a href="ex1_1_2_3_4.py">ex1_1_2_3_4.py</a></li>
<li><a href="ex2_1_2_3_4.py">ex2_1_2_3_4.py</a></li>
<li><a href="ex3_1_2_3_4.py">ex3_1_2_3_4.py</a></li>
<li><a href="ex4_1_2_3_4.py">ex4_1_2_3_4.py</a></li>
<li><a href="ex4_client_tcp.py">ex4_client_tcp.py</a></li>
<li><a href="ex4_client_udp.py">ex4_client_udp.py</a></li>
<li><a href="ex4_server_tcp.py">ex4_server_tcp.py</a></li>
<li><a href="ex4_server_udp.py">ex4_server_udp.py</a></li>
<li><a href="ex5_1.py">ex5_1.py</a></li>
<li><a href="ex5_2.py">ex5_2.py</a></li>
<li><a href="ex5_3.py">ex5_3.py</a></li>
<li><a href="ex5_4.py">ex5_4.py</a></li>
<li><a href="tp4_docker">tp4_docker</a></li>
<li><a href="tp4_docker_intrucoes.txt">tp4_docker_intrucoes.txt</a></li>
</ul>
<hr>
</body>
</html>

Graças ao servidor HTTP, o terminal cURL conecta-se na porta do mesmo e recebe a página em HTML como resposta.

A página deste servidor mostra a estrutura da pasta onde o servidor foi inicializado (neste caso, o diretório com os arquivos do TP4) em formato HTML.

"""