# GI-DA

Genshin Impact - Data Analyst

Por [samuelfarrus](https://github.com/samuelfarrus)

## Descrição

Projeto para o Laboratório de Análise de dados com Python e Pandas, da plataforma [DIO.ME](https://www.dio.me/).

O GI-DA é uma espécie de simulação de terminal, desenvolvida em Python, que permite, de forma interativa, acessar algumas consultas de dados de um arquivo .csv que contém registros dos resultados de wishes Genshin Impact.

O arquivo .csv se encontra dentro da mesma pasta. Ele foi gerado a partir do [GIG-DSP](https://github.com/samuelfarrus/gig_dsp), um arquivo .py que atua como um gerador aleatório interativo, criando, a partir da inserção de uma data e da quantidade de wishes que se deseja, um arquivo .csv com todos os resultados desejados.

OBS: a pasta já contém um arquivo 'genshin_dataset.csv' por padrão, contendo 1674 registros, pronto para ser utilizado pelo GI-DA.

### Executando

Para executar o GI-DA, basta utilizar um terminal (ou até mesmo Git Bash) e inserir `py gi_da.py`, substituindo *gi_da.py* pelo caminho até o arquivo caso seja necessário.

### Abrindo um arquivo .csv

Ao executar o GI-DA, a primeira entrada demandada é o nome do arquivo .csv que se deseja abrir para analisar. Esse arquivo **deve obrigatoriamente estar dentro da mesma pasta**.

* Por padrão, o arquivo é nomeado 'genshin_dataset.csv'. Caso não seja inserido nenhum nome durante a requisição, o GI-DA assume que o arquivo possui o nome padrão.
* Não há a necessidade de se inserir '.csv' durante a requisição, o GI-DA automatucamente completa com a extensão se necessário.

* **Observação: *não foi inserido ainda um tratamento de erros para o caso da inserção de um nome de arquivo inexistente*. Recomenda-se, por enquanto, para evitar problemas maiores, a utilização do nome padrão**.

### Ajuda - Comandos aceitos pelo GI-DA.

	-help 					Ajuda, lista comandos e suas aplicações.

	-all	 				Lista todos os registros de wishes gerados.

	-amount [OPTION] 		Lista a quantidade de registros por tipo.

		-w 					Lista a quantidade de armas por raridade.

		-c 					Lista a quantidade de personagens por raridade.

	-allchars 				Lista todas as personagens obtidos.

	-allfive [OPTION] 		Lista todos os registros de personagens 5 estrelas.

		-list 				(Default) Lista todos os registros de personagens 5 estrelas.

		-count 				Mostra a quantidade de personagens 5 estrelas obtida.

	-allfour [OPTION] 		Lista todos os registros de raridade 4 estrelas.

		-list 				(Default) Lista todos os registros 4 estrelas.

		-chars 				Lista apenas as personagens de raridade 4 estrelas.

		-wp 				Lista apenas as armas 4 estrelas.

		-count 				Mostra a quantidade de personagens e de armas 4 estrelas.

	-sex [OPTION] 			Mostra a quantidade de personagens por sexo.

		-f 					Lista as personagens femininas.

		-m 					Lista as personagens masculinas.

	-charwp [OPTION] 		Mostra a quantidade de personagens por arma utilizada.

		-b 					Lista as personagens que usam arco.

		-ca 				Lista as personagens que usam catalisador.

		-cl 				Lista as personagens que usam \'Claymore\'.

		-p 					Lista as personagens que usam lança.

		-s 					Lista as personagens que usam espada.

	-charelem [OPTION] 		Mostra a quantidade de personagens por elemento/visão.

		-a 					Lista as personagens de visão Anemo.

		-c 					Lista as personagens de visão Cryo.

		-e 					Lista as personagens de visão Electro.

		-g 					Lista as personagens de visão Geo.

		-h 					Lista as personagens de visão Hydro.

		-p 					Lista as personagens de visão Pyro.

	-exit 					Encerra o GI-DA.